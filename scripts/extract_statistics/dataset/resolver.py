from html.parser import HTMLParser
from series_matching import importance_matching
from series_matching import  date_matching
from request_url import GetUrl
import pandas
import re
from concurrent.futures import ThreadPoolExecutor


class ExtractMessage(HTMLParser):
    def __init__(self,is_gcc:bool):
        self.end=0
        self.message=[]
        self.reported:str=''
        self.modified:str=''
        self.symptom:str=''
        self.importance:str=''
        self.inContent=False
        self.isKeywords=False
        self.isTitle=False
        self.title=""
        self.is_gcc=is_gcc
        super().__init__()

    def handle_starttag(self, tag: str, attrs) -> None:
        if len(attrs)>0 and tag=='table' and attrs[0][1].find("edit_form")!=-1:
            self.inContent=True
        if len(attrs)>1 and attrs[1][1]=="field_container_keywords":
            self.isKeywords=True
        if len(attrs)>0 and tag=='table' and attrs[0][1].find("bz_big")!=-1:
            self.inContent=False
        if len(attrs)>0 and attrs[0][1].find('short_desc_nonedit')!=-1:
            self.isTitle=True

    def handle_data(self, data: str) -> None:
        if self.isTitle==True:
            self.isTitle=False
            self.title=data.replace('\n','')
        if self.inContent== True:
            if self.isKeywords==True:
                self.isKeywords=False
                #parsing keywords to symptoms
                if data.find('hog')!=-1:
                    self.symptom='efficient/hang'
                elif data.find('accept')!=-1:
                    self.symptom = 'accepts_invalid'
                elif data.find('reject')!=-1:
                    self.symptom='rejects_valid'
                elif data.find('wrong')!=-1:
                    self.symptom='wrong_output'
                elif data.find('ice')!=-1:
                    self.symptom='crash'
                elif data.find('diagnostic')!=-1:
                    self.symptom='diagnostic'
                else:
                    self.symptom='others'

            if importance_matching(data,self.is_gcc):
                self.importance=data.replace('\n','')
                self.importance=re.sub(r"\s+"," ",self.importance)
            if self.end < 2:
                if self.is_gcc:
                    if date_matching('\d{2}:\d{2} UTC by',data):
                        self.reported=data[:data.find('UTC')]
                        self.end=self.end+1
                    else:
                        if date_matching('\d{2}:\d{2} UTC', data) and self.end==1:
                            self.modified=data[:data.find("UTC")]
                            self.end=self.end+1
                else:
                    if date_matching('\d{2}:\d{2} P[SD]T by',data):
                        self.reported=data[:data.find('P')]
                        self.end=self.end+1
                    else:
                        if date_matching('\d{2}:\d{2} P[SD]T', data) and self.end==1:
                            self.modified=data[:data.find("P")]
                            self.end=self.end+1

    def get_messages(self):
        self.message.append(self.reported[:self.reported.find(' ')])
        self.message.append(self.modified[:self.modified.find(' ')])
        self.message.append(self.importance)
        self.message.append(self.symptom)
        self.message.append(self.title)
        return self.message

class ReportTextParser:
    def __init__(self):
        self.is_gcc = True
        self.source=''
        self.statistic=pandas.DataFrame(columns=['bug_id','Creation Date','Last Modified Date','Importance','Symptom','Title'])
    def parse_description(self, no):
        try:
            addr = GetUrl(self.is_gcc)
            html = addr.request_url(no, '.', False)
        except Exception as e:
            print(e)
            return []
        else:
            #print(html)
            ps=ExtractMessage(self.is_gcc)
            ps.feed(html)
            return ps.get_messages()
        
    def parse_single(self, bugno):
        print(bugno)
        message = []
        message=self.parse_description(bugno)
        message.insert(0,bugno)
        if len(message) < 6:
            for i in range(5):
                message.append('')
        self.statistic.loc[len(self.statistic)]=message


    def parse(self):
         bugno_list=self.source.read().split('\n')
         self.source.close()
         with ThreadPoolExecutor(max_workers=20) as executor:
            res = [executor.submit(self.parse_single, bugno) for bugno in bugno_list]
         
    
    def set_target(self, source, is_gcc):
        self.source = open(source, 'r', encoding='utf-8')
        self.is_gcc = is_gcc


    def stat(self):
        self.statistic.to_csv('../dataset_TSE.csv', index=False, sep=',', encoding='utf-8')

    def launch(self):
        self.set_target('bugno_gcc.txt', True)
        self.parse()
        self.set_target('bugno_llvm.txt', True)
        self.parse()

        self.stat()









