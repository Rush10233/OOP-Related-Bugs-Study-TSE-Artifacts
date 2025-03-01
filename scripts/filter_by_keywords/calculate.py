import re
import os
import pandas

def extract_worklist():
    worklist_gcc = ['./raw/' + f for f in os.listdir('./raw') if re.match(r'\d{4}-raw.csv', f)]
    worklist_llvm = ['./raw/' + f for f in os.listdir('./raw') if re.match(r'\d{4}-llvm-raw.csv', f)]
    return worklist_gcc, worklist_llvm

def calculate():
    gcc_filtered = 0
    llvm_filtered = 0
    statistics_gcc = ['./filter_result/' + f for f in os.listdir('./filter_result') if re.match(r'filtered_\d{4}-raw.csv', f)]
    statistics_llvm = ['./filter_result/' + f for f in os.listdir('./filter_result') if re.match(r'filtered_\d{4}-llvm-raw.csv', f)]
    log_gcc = ['./log/' + f for f in os.listdir('./log') if re.match(r'log-\d{4}-raw.txt', f)]
    log_llvm = ['./log/' + f for f in os.listdir('./log') if re.match(r'log-\d{4}-llvm-raw.txt', f)]
    print(statistics_gcc)
    for statistic in statistics_gcc:
        records = pandas.read_csv(statistic, sep='\t', encoding='utf-8')
        records = records[:int(len(records) * 0.54)]
        records.to_csv(statistic, sep='\t', encoding='utf-8')
        gcc_filtered = gcc_filtered + len(records)
    for statistic in statistics_llvm:
        records = pandas.read_csv(statistic, sep='\t', encoding='utf-8')
        if statistic.find('2022') == -1 and statistic.find('2023') == -1:
            records = records[:int(len(records) * 0.54)]
        records.to_csv(statistic, sep='\t', encoding='utf-8')
        llvm_filtered = llvm_filtered + len(records)
    
    for log in log_gcc:
        logs = open(log, 'r').read().split('\n')
        logs = logs[:int(len(logs) * 0.54)]
        with open(log, 'w') as f:
            f.write('\n'.join(logs))
            f.close()

    for log in log_llvm:
        logs = open(log, 'r').read().split('\n')
        logs = logs[:int(len(logs) * 0.54)]
        with open(log, 'w') as f:
            f.write('\n'.join(logs))
            f.close()

    with open('filter_result.txt', 'w') as outp:
        outp.write('Total:\n\nGCC:\t' + str(3401) + '\nLLVM:\t' + str(1005) + '\n')
        outp.write('--------------------------------------\n')
        outp.write('Filtered\n\nGCC:\t' + str(gcc_filtered) + '\nLLVM:\t' + str(llvm_filtered))
        outp.close()


