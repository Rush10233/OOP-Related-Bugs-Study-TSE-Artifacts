import os
import subprocess
import pandas
import time
import json

with open('./setup/config.json', 'r', encoding='utf-8') as file:  
    data = json.load(file)  
INSTRUMENTOR_PATH = data["instrumentor_path"]
print("INSTRUMENTOR_PATH", INSTRUMENTOR_PATH)
assert(os.path.exists(INSTRUMENTOR_PATH) and "instrumentor_path don't exist!")
class InstrumentReporter:
    res = {}

    @staticmethod
    def addCase(mutator, status):
        if mutator not in InstrumentReporter.res:
            InstrumentReporter.res[mutator] = {}
            InstrumentReporter.res[mutator]['Fail'] = 0
            InstrumentReporter.res[mutator]['Success'] = 0

        InstrumentReporter.res[mutator][status]+=1

    def toString():
        total_fail = sum(mutator['Fail'] for mutator in InstrumentReporter.res.values())
        total_success = sum(mutator['Success'] for mutator in InstrumentReporter.res.values())

        ret = ""
        for mutator in InstrumentReporter.res:
            fail_count = InstrumentReporter.res[mutator]["Fail"]
            success_count = InstrumentReporter.res[mutator]["Success"]
            fail_percentage = 0 if total_fail == 0 else fail_count/total_fail*100
            success_percentage = 0 if total_success == 0 else success_count/total_success*100
            ret += "{:<10s} {:>10d}({:>5.2f}%) {:>10d}({:>5.2f}%)\n".format(mutator, success_count, success_percentage, fail_count, fail_percentage)
        return ret


options=pandas.read_csv('record.csv')
option_reference={}
tstnum=0
for index, row in options.iterrows():
    tstnum=tstnum+1
    option_reference[str(row['id'])]=str(row['options'])
 #   if tstnum<100:
 #       print(row['id']+'ddd')
error_log=open('./setup/reports_fail.csv','w')
report=open('./setup/reports.txt','w')
report_2=open('./setup/reports_success.csv','w')
count_succ=0
count_fail=0
count_skip=0
stat=""
candidates=[f for f in os.listdir('.') if f.find('.cpp')!=-1 and f.find('_')!=-1]
total=len(candidates)
count_num=0
t1=time.time()
for candidate in candidates:
    count_num=count_num+1
    print(candidate+'('+str(count_num)+'--'+str(total)+')')
    file=open(candidate,'r')
    origin=file.read()
    file.close()
    muts=candidate.split('_')
    if muts[0] in option_reference:
        option_sets=option_reference[muts[0]]
    else:
        option_sets=""
    muts[-1]=muts[-1][:muts[-1].find('.cpp')]
    target=muts[0]
    opt_set=option_sets.split()
    real=[]
    for opt in opt_set:
        opt.rstrip()
        if opt.startswith('-std') or opt.startswith('-f'):
            #print(opt)
            real.append(opt)
    for i in range(1,len(muts)):
        #print(muts[i])
        res=subprocess.Popen(['timeout','3',INSTRUMENTOR_PATH,candidate,'--mutator='+muts[i],'--sourcedir='+os.getcwd()+'/','--']+real,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        res_err=res.stderr.read().__str__()
        if res_err.find('[MUTATION ASSERT]') != -1:
            print(res_err)
        if res_err.find('error')!=-1:
            stat="fail"
            count_fail=count_fail+1
            error_log.write('source: '+candidate+'\tmutator: '+muts[i]+'\n')
            InstrumentReporter.addCase('mutator_'+muts[i], "Fail")
            #error_log.write('outp: '+res_err)
            break
    file=open(candidate,'r')
    brand=file.read()
    if brand==origin:
        stat="skip"
        count_skip=count_skip+1
        os.system('rm '+candidate)
    else:
        stat="success"
        count_succ=count_succ+1
        report_2.write('source: '+ candidate+'\tmutator: '+muts[i]+'\n')
        InstrumentReporter.addCase('mutator_'+muts[i], "Success")

t2=time.time()
run_time=round(t2-t1)
hour = run_time//3600
minute = (run_time-3600*hour)//60
second = run_time-3600*hour-60*minute
report.write('Total: '+str(total)+'\tSkipped: '+str(count_skip-count_fail)+'\n')
report.write('Succeed: '+str(count_succ)+'\tFailed: '+str(count_fail)+'\n')
report.write(f'Lasting: {hour} h :{minute} m : {second} s')

print(InstrumentReporter.toString())

report.close()
error_log.close()