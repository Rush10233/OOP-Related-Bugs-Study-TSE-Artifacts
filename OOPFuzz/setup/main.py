# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import os
import re
import sys
import time
import traceback
import subprocess
import json
from prettytable import PrettyTable
from utils.cmp_run_out import run_a_out, analyse_runout_differential
# Press the green button in the gutter to run the script.6
test_config:dict={}
all_version_gcc=['4.1.2','4.4.7','4.5.3','4.6.4','4.7.1','4.7.2','4.7.3','4.7.4','4.8.1',
                    '4.8.2','4.8.3','4.8.4','4.8.5','4.9.0','4.9.1','4.9.2','4.9.3','4.9.4','5.1','5.2',
                    '5.3','5.4','5.5','6.1','6.2','6.3','6.4','7.1','7.2','7.3','7.4','7.5','8.1','8.2',
                    '8.3','8.4','8.5','9.1','9.2','9.3','9.4','9.5','10.1','10.2','10.3','10.4','10.5',
                    '11.1','11.2','11.3','11.4','12.1','12.2','12.3','13.1','13.2']
sourcedir=""
total_times=0
'''
def collect_output(dr):
    outp_f=dr.find_elements(by=By.XPATH,value="//*[@class='content output-content']")[0]
    return outp_f.text

def load_test(dr,tstpath):
    time.
    
    
    (1.5)
    sl=dr.find_elements(by=By.XPATH,value="//*[@class='btn btn-sm btn-light load-save']")[0]
    #action.click(sl)
    #action.perform()
    sl.click()
    time.sleep(1.5)
    sl2=dr.find_element(by=By.XPATH,value="//*[text()='File system']")
    #action.click(sl2)
    #action.perform()
    sl2.click()
    time.sleep(1.5)
    sl3=dr.find_element(by=By.XPATH,value="//*[text()='Load from a local file']")
    inp=sl3.find_element(by=By.TAG_NAME,value='input')
    inp.send_keys(tstpath)

def select_options(dr,options:list):
    opt=dr.find_elements(by=By.XPATH,value="//input[@class='options form-control']")[0]
    sep=' '
    opt.clear()
    time.sleep(0.5)
    opt.send_keys(sep.join(options))
    time.sleep(0.5)

'''
time_stamp_str = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))
detaild_inf='detailed_tst_report_'+time_stamp_str
os.makedirs(detaild_inf, exist_ok=True)
detaild_inf_records_path = os.path.join(detaild_inf, "records")
detaild_inf_records = os.makedirs(detaild_inf_records_path, exist_ok=True)

diff_rec=os.path.join(detaild_inf_records_path, 'differential_record'+'.txt')

diff_runout_rec=os.path.join(detaild_inf_records_path, 'differential_runout_record'+'.txt')


with open('./setup/config.json', 'r', encoding='utf-8') as file:  
    data = json.load(file)  
gcc_path=data['gcc_path']
clang_path=data['clang_path']

def analyse_differential(tstname,copt1,copt2,eopt1,eopt2,versions,optlevel):
    #if copt1 != 'Compiler returned: 0' and copt2 != 'Compiler returned: 0':
    #    return False
    #if copt1==''or copt2==''or eopt1=='' or eopt2=='':
    #    return False
    res=open(diff_rec,'a+')
    doubted=tstname+'\n'+'Suspected symptom: '
    if copt1.find('nternal')!=-1 or copt1.find('crash')!=-1 or copt2.find('nternal')!=-1 or copt1.find('crash')!=-1:
        doubted=doubted+" crash\n"
    elif copt1.find('error')!=-1 and copt2.find('error')!=-1:
        res.close()
        return False
    elif copt1.find('error') ==-1 and copt2.find('error')==-1:
        res.close()
        return False       
    else:
        doubted=doubted+"different outp\n"
    doubted=doubted+'\n-------------------------\n'
    res.write(doubted)
    res.close()
    #res.write(tstname+'\n')
    #res.write('Suspected symptom: ')
    '''
    if copt1=='':
        if copt2=='':
            if eopt1.find('')==-1:
                res.write('wrong code\n')
            else:
                #res.write('nop\n')
                res.write('\n---------------------\n')
                res.close()
                return Falseg++ -std=c++11  -O0  19767_7_12.cpp

    else:
        res.write('accept invalid\n')
    res.write('Historical Versions: ')
    for version in versions:
        res.write(version+'\t')
    res.write('\nOptimization level: '+optlevel+'\n')
    res.write('---------------------\n')
    res.close()
    '''
    return True


def send_test(tstname,versions,options, need_runout):
    rec_flag = False
    #load_test(dr,tstpath)
    global total_times
    global gcc_path
    global clang_path
    #candidate_version=['x86-64 gcc 12.1','x86-64 clang 12.0.0']
    candidate_version = ['x86-64 gcc 13.2', 'x86-64 clang 17.0.1']
    stat=PrettyTable(['compiler config','Compiling  outp',"Executing outp"])
    #res="<Compiling Stage:>\n"
    #Handling candidate versions
    '''    for version in versions:
        get=False
        while True:
            print(version)
            for cv in all_version_gcc:
                if re.match(version,cv) is not None:
                    candidate_version.append('x86-64 gcc '+cv)
                    get=True
                    break
            if get:
                break
            if version.rfind('.')==-1:
                break
            version=version[:version.rfind('.')]'''
    #Handling candidate compiling options
    candidate_optimization=set(['-O0'])
    for option in options:
        if option.find('-O')==0:
            candidate_optimization.add(option)
            options.remove(option)
    for optimization_level in candidate_optimization:
        total_times=total_times+1
        copt1 = ""
        copt2 = ""
        eopt1 = ""
        eopt2 = ""
        print(options)
        current_options=options+[optimization_level]
        print(current_options)
        options_str='  '.join(current_options)
        bash1_gcc='g++ '+options_str+'  '+tstname
        print(bash1_gcc)
        bash1_clang='clang++ '+options_str+'  '+tstname

        if need_runout:
            runout1_exist = False
            runout2_exist = False
            runout1 = {}
            runout2 = {}

            if os.path.exists("a.out"):
                os.remove("a.out")
            out1=subprocess.Popen(['timeout','3',gcc_path]+current_options+[tstname],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            copt1=out1.stderr.read().decode('utf-8')

            if os.path.exists("a.out"):
                runout1 = run_a_out()
                runout1_exist = True

            if os.path.exists("a.out"):
                os.remove("a.out")
            out2=subprocess.Popen(['timeout','3',clang_path]+current_options+[tstname],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            copt2=out2.stderr.read().decode('utf-8')

            if os.path.exists("a.out"):
                runout2 = run_a_out()
                runout2_exist = True
            
            runout_cmp_res = analyse_runout_differential(diff_runout_rec, tstname, runout1_exist, runout2_exist, runout1, runout2)


            if len(copt2)>5000:
                copt2=copt2[:50]
            if len(copt1)>5000:
                copt1=copt1[:50]
                
            if copt1!=copt2 or eopt1!=eopt2 or runout_cmp_res:
                rec_flag=analyse_differential(tstname,copt1,copt2,eopt1,eopt2,versions=candidate_version,optlevel=optimization_level)
                if runout_cmp_res:
                    rec_flag = rec_flag or runout_cmp_res
                    stat.add_row(['gcc-13.2.0: '+options_str, copt1, runout1])
                    stat.add_row(['clang-17.0.1: '+options_str, copt2, runout2])
                else:
                    stat.add_row(['gcc-13.2.0: '+options_str, copt1, '--'])
                    stat.add_row(['clang-17.0.1: '+options_str, copt2, '--'])
        else:
            out1=subprocess.Popen(['timeout','3',gcc_path]+current_options+[tstname],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            #time.sleep(0.5)
            copt1=out1.stderr.read().decode('utf-8')
            #print(copt1)
            out2=subprocess.Popen(['timeout','3',clang_path]+current_options+[tstname],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            copt2=out2.stderr.read().decode('utf-8')
            if len(copt2)>5000:
                copt2=copt2[:50]
            if len(copt1)>5000:
                copt1=copt1[:50]
            #select_options(dr, current_options)
            if copt1!=copt2 or eopt1!=eopt2:
                rec_flag=analyse_differential(tstname,copt1,copt2,eopt1,eopt2,versions=candidate_version,optlevel=optimization_level)
                stat.add_row(['gcc-13.2.0: '+options_str, copt1, '--'])
                stat.add_row(['clang-17.0.1: '+options_str, copt2, '--'])
            

    return stat,rec_flag
    '''watch=dr.find_elements(by=By.XPATH,value="//*[@class='view-lines monaco-mouse-cursor-text']")[1]
    WebDriverWait(dr,timeout=20).until_not(expected_conditions.text_to_be_present_in_element(watch,'Compiling'))'''

def set_test(tstname:str,outp):
    
    try:
        content=open(tstname,'r')
        #if content.
        src=content.read()
        content.close()
    except:
        src=""
    
    if not os.path.exists(outp):
        os.makedirs(outp)
    if tstname.find('_')!=-1:
        search_key=tstname[:tstname.find('_')]
    else:
        search_key=tstname[:tstname.find('.cpp')]
    #versions=test_config[tstname[:tstname.find('.txt')]][0]
    #options=test_config[tstname[:tstname.find('.txt')]][1]
    if search_key in test_config:
        versions=test_config[search_key][0]
        options=test_config[search_key][1]
    else:
        versions=[]
        options=[]
    if src.find('main')==-1:
        options.append('-fsyntax-only')
    if tstname.find('_17')!=-1:
        options.append('-std=c++20')
    options=list(set(options))
    print(versions)
    print(options)
    #tstpath=os.path.join(os.path.abspath(sourcedir),tstname)
    need_runout = (src.find('main') != -1) and ('-fsyntax-only' not in options)
    res,flag=send_test(tstname,versions,options, need_runout)
    if flag:
        rec_file = open(os.path.join(outp, tstname)+'.txt', 'w', encoding='utf-8')
        res.align='l'
        rec_file.write(str(res)+'\n')

        rec_file.write(tstname)
        rec_file.write("\n============================\n")
        rec_file.write(src)
        rec_file.write("\n============================\n")
        rec_file.close()

    '''send_test(dr,tstpath,compiler_1)
    res=collect_output(dr)
    outp.write('Compiling stage: \n')
    outp.write(res+'\n')'''


if __name__ == '__main__':
    os.system('export LANG=en_US')
    #sourcedir=sys.argv[1]
    #tst_c=os.listdir('.//source1')
    tst_c=[f for f in os.listdir('.') if f.find('.cpp')!=-1]
    totalnum=len(tst_c)
    configs=open('consoles.txt')
    index=configs.readline()
    #Start timing
    t1=time.time()
    result=open(os.path.join(detaild_inf_records_path,'result_crosstexting.txt'),'w')
    while(index):
        bugno=index.rstrip()
        versions_inf=configs.readline()
        if versions_inf.isspace():
            versions=[]
        else:
            versions=versions_inf.split()
        option_inf=configs.readline()
        if option_inf.isspace():
            options=[]
        else:
            options=option_inf.split()
        test_config[bugno]=(versions,options)
        index=configs.readline()
    '''
    dr=webdriver.Edge()
    #dr.implicitly_wait(5)
    dr.get('https://godbolt.org/')
    time.sleep(1)
    #WebDriverWait(dr,timeout=10).until(expected_conditions.presence_of_element_located(('id','tomselect-1-ts-control')))
    close_alert=dr.find_element(by=By.XPATH,value="//*[@data-cy='close-alert-btn']")
    close_alert.click()
    time.sleep(0.8)
    open_output=dr.find_elements(by=By.XPATH,value="//*[@data-cy='new-output-pane-btn']")[0]
    open_output.click()
    '''
    collection=os.path.join(os.path.abspath('.'),detaild_inf)
    #print(collection)
    current=0
    for tst in tst_c:
        print(tst)
        print('(%d//%d)'%(current,totalnum))
        set_test(tstname=tst,outp=collection)
        #time.sleep(0.5)
        current=current+1
    #End timing
    t2=time.time()
    run_time = round(t2 - t1)
    hour = run_time // 3600
    minute = (run_time - 3600 * hour) // 60
    second = run_time - 3600 * hour - 60 * minute
    result.write("Total Tests: "+str(totalnum)+'\n')
    result.write("Total Execution Times: " + str(total_times) + '\n')
    result.write((f'Lasting: {hour} h :{minute} m : {second} s'))

    #collection.close()
    '''compiler_selection=dr.find_element(value='tomselect-2-ts-control')
    action=ActionChains(dr)
    action.click(compiler_selection)
    action.perform()
    version=dr.find_element(value='tomselect-2-opt--65')
    print(version.text)
    action.click(version)
    action.perform()
    sl=dr.find_elements(by=By.XPATH,value="//*[@class='btn btn-sm btn-light load-save']")[0]
    action.click(sl)
    action.perform()
    time.sleep(1)
    sl2=dr.find_element(by=By.XPATH,value="//*[text()='File system']")
    action.click(sl2)
    action.perform()
    time.sleep(1)
    sl3=dr.find_element(by=By.XPATH,value="//*[text()='Load from a local file']")
    inp=sl3.find_element(by=By.TAG_NAME,value='input')
    inp.send_keys("C:\\Users\\Rush\\PycharmProjects\\tst_framework\\tstf\\70259.cpp")
    watch=dr.find_elements(by=By.XPATH,value="//*[@class='view-lines monaco-mouse-cursor-text']")[1]
    print(watch.text)'''

    #input()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
