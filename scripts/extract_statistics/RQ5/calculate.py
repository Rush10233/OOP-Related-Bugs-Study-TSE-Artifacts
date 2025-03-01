
import pandas

def calculate(source, target):
    rtc = ['Member Access','Class Scope','Friends','Ctor & Dtor'
                                ,'Copy & Move','Overloading','Inherited Member Access','Multiple Inheritance'
                                ,'Inherited Ctor & Dtor','Override Control','Casting', 'Template Alias'
                                ,'Template Parsing','Constraint & Concepts','Template Specialization'
                                ,'Template Instantiation','Others']
    rtc_fullname=dict.fromkeys(rtc,'')
    col={}
    for i in range(len(rtc)):
        col[rtc[i]]=i
    symp=['Ac','Re','Cr','Wr','Ha','Ef','Di','Ot']
    symp_fullname=dict.fromkeys(symp,'')
    symp_fullname['Ef']='Efficiency'
    row={}
    for j in range(len(symp)):
        row[symp[j]]=j
    index=[[0 for i in range(len(symp))] for j in range(len(rtc))]
    source=open(source)
    pat=source.readline()
    while pat:
        messages=pat.split('\t')
        #category
        #c_rtc=messages[1][:2]
        #subcategory
        c_rtc = messages[1].strip()
        c_symp=messages[0][:2]
        if rtc_fullname[c_rtc]=="":
            rtc_fullname[c_rtc]=messages[1].strip()
        if symp_fullname[c_symp]=="":
            symp_fullname[c_symp]=messages[0].strip()
        #print(c_rtc+"---"+c_symp)
        index[col[c_rtc]][row[c_symp]]=index[col[c_rtc]][row[c_symp]]+1
        pat=source.readline()
    for rtc in index:
        sum_n=sum(rtc)
        '''for i in range(len(rtc)):
            rtc[i]=round((rtc[i]/sum_n),4)
            rtc[i]="%.2f%%" % (rtc[i]*100)'''
    print(rtc_fullname.values())
    outp=pandas.DataFrame(index,columns=list(symp_fullname.values()))
    outp.index=list(rtc_fullname.values())
    outp.to_csv(target)