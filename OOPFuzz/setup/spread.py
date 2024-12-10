import os
import json
with open('./setup/config.json', 'r', encoding='utf-8') as file:  
    data = json.load(file)  
number=data["mutator_number"]
active_mutators=data["active_mutators"]
#candidate_mutators=[]
useall=data['use_all_mutators']
if useall:
    candidate_mutators=[i+1 for i in range(number)]
else:
    candidate_mutators=active_mutators

origin_tst=[f for f in os.listdir('.') if f.find('.txt')!=-1]

for tst in origin_tst:
    for index in candidate_mutators:
        mutator=index
        target_outp=tst[:tst.find('.txt')]+'_'+str(mutator)+'.cpp'
        os.popen('cp '+tst+' '+target_outp)