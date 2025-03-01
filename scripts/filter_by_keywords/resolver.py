from html.parser import HTMLParser
from request_url import GetUrl
from concurrent.futures import ThreadPoolExecutor
import numpy
import pandas
import time

def filter_by_keywords(keywords:list, target:str):
    for keyword in keywords:
        if target.find(keyword) != -1:
            return True
    return False

class ParseDescription(HTMLParser):
    def __init__(self, *, keywords:list, convert_charrefs: bool = ...) -> None:
        self.context=False
        self.first_comment=False
        self.localize=False
        self.comment: str=""
        self.keywords = keywords
        super().__init__(convert_charrefs=convert_charrefs)
    def handle_starttag(self, tag: str, attrs) -> None:
        if tag=='div' and len(attrs)>0 and attrs[0][1]=='c0':
            self.first_comment = True
            #print(tag)
        if tag=='pre' and self.first_comment:
            self.first_comment=False
            self.context=True

    def handle_endtag(self, tag: str) -> None:
        if tag == 'pre':
            self.context=False

    def handle_data(self, data: str) -> None:
        if self.context:
            if filter_by_keywords(self.keywords, data):
                self.localize = True


    def get_localize(self):
        return self.localize

    def get_comment(self):
        return self.comment

class ReportTextParser:
    def __init__(self,bug_list:str,compiler:str):
        print(bug_list)
        if compiler == 'gcc':
            self.is_gcc=True
        else:
            self.is_gcc=False
        self.raw = pandas.read_csv(bug_list,sep='\t')
        self.record_source = self.raw.values.tolist()
        self.record_target = {}
        self.keywords = ['struct', 'class']
        self.list_name=bug_list[bug_list.rfind('/')+1:]
        self.log = './log/log-' + self.list_name.replace('.csv', '.txt')
        self.log_text=[]

    def parse_title(self, no, des):
        #print(no)
        #print(des)
        if filter_by_keywords(self.keywords, des):
            #print(des)
            result = str(no) + '\tkeyword in title'
            self.log_text.append(result)
            return True
        return False

    def parse_description(self, no):
        passed = False
        ps = ParseDescription(keywords=self.keywords)
        retry_times = 0
        while not passed:
            try:
                addr = GetUrl(self.is_gcc)
                html = addr.request_url(no, '.', False)
            except Exception as e:
                self.log_text.append(str(e))
                time.sleep(10)
                retry_times = retry_times + 1
                if retry_times == 3:
                    passed = True
                continue
            else:
                ps.feed(html)
                passed = True
        if ps.get_localize():
            result = str(no) + '\tkeyword in description'
            self.log_text.append(result)
            return True
        else:
            return False

    def parse(self, no, des):
        if self.parse_title(no, des) or self.parse_description(no):
            self.record_target[no] = des

    def stat(self):
        output = pandas.DataFrame.from_dict(self.record_target, orient='index', columns=['Title'])
        output = output.reset_index().rename(columns={'index':'Issue ID'})
        #output = output[: int(len(output) * 0.75)]
        output.to_csv('./filter_result/filtered_' + self.list_name, index=False, sep='\t')

    def launch(self):
        with ThreadPoolExecutor(max_workers=30) as executor:
           res = [executor.submit(self.parse, record[0], record[1]) for record in self.record_source]
        self.stat()
        #print(self.log_text)
        with open(self.log, 'w') as f:
            f.write('\n'.join(self.log_text)) 









