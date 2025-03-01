import sys
import pandas

TOTAL_GCC = 586
TOTAL_LLVM = 202

def calculate(consoles, compiler):
    std_option={}
    level={}
    err_flag={}
    warning_flag={}
    long_tail={}
    input_f=open(consoles)
    message=input_f.readline()
    option_flag_amount_dis={}
    total_flags=0
    while message:
        if message[0]=='-':
            options=message.split()
            total_flags=total_flags+len(options)
            if len(options) not in long_tail:
                option_class=[0 for i in range(4)]
                long_tail[len(options)]=option_class
            option_amounts=len(options)
            for option in options:
                if option.find('-Wall')!=-1 or option.find('-Wextra')!=-1:
                    option_amounts=option_amounts-1
            #print(option_amounts)
            if option_amounts!=0:
                if option_amounts in option_flag_amount_dis:
                    option_flag_amount_dis[option_amounts]=option_flag_amount_dis[option_amounts]+1
                else:
                    option_flag_amount_dis[option_amounts]=1
            for option in options:
                option=' '+option
                if option.find('report-bug') != -1 or option.find('-Werror') != -1 or option.find('-Wpedantic') != -1:
                    continue
                if option.find('-std=')==1 and option.find('23')==-1:
                    if option.find('c++20')!=-1 or option.find('c++2a')!=-1:
                        option=' -std=c++20/2a'
                    elif option.find('c++17')!=-1 or option.find('c++1z')!=-1:
                        option=' -std=c++17/1z'
                    elif option.find('c++14')!=-1 or option.find('c++1y')!=-1:
                        option=' -std=c++14/1y'
                    if option in std_option.keys():
                        std_option[option]=std_option[option]+1
                    else:
                        std_option[option]=1
                    long_tail[len(options)][0]=long_tail[len(options)][0]+1
                if option.find('-O')==1:
                    if option in level.keys():
                        level[option]=level[option]+1
                    else:
                        level[option]=1
                    long_tail[len(options)][1] = long_tail[len(options)][1] + 1
                if option.find('-f')==1:
                    if option in err_flag.keys():
                        err_flag[option]=err_flag[option]+1
                    else:
                        err_flag[option]=1
                    long_tail[len(options)][2] = long_tail[len(options)][2] + 1
                if option.find('-W')==1:
                    if option in warning_flag.keys():
                        warning_flag[option]=warning_flag[option]+1
                    else:
                        warning_flag[option]=1

                    long_tail[len(options)][3] = long_tail[len(options)][3] + 1
        message=input_f.readline()
    if compiler == 'gcc':
        option_flag_amount_dis[0]=TOTAL_GCC-sum(list(option_flag_amount_dis.values()))
    else:
        option_flag_amount_dis[0]=TOTAL_LLVM-sum(list(option_flag_amount_dis.values()))
    option_flag_amount_dis = dict(sorted(option_flag_amount_dis.items(), key=lambda x: x[0], reverse=False))
    amount_calculate=pandas.DataFrame.from_dict(option_flag_amount_dis,orient='index',columns=['report number'])
    amount_calculate=amount_calculate.reset_index().rename(columns={'index':'option number'})
    amount_calculate.to_csv('../RQ6_option_num_distribution_'+ compiler + '.csv', index=False)
    option_distribution=pandas.DataFrame(columns=['option','occurrence'])
    std_option=dict(sorted(std_option.items(),key= lambda x:x[1],reverse=True))
    level = dict(sorted(level.items(), key=lambda x: x[1],reverse=True))
    err_flag  = dict(sorted(err_flag.items(), key=lambda x: x[1],reverse=True))
    warning_flag = dict(sorted(warning_flag.items(), key=lambda x: x[1],reverse=True))
    for std_op in std_option.items():
        option_distribution.loc[len(option_distribution)]=std_op
    for le in level.items():
        option_distribution.loc[len(option_distribution)]=le
    for err in err_flag.items():
        option_distribution.loc[len(option_distribution)] = err
    for wa in warning_flag.items():
        option_distribution.loc[len(option_distribution)]=wa
    option_distribution = option_distribution.sort_values(by='occurrence', ascending=False)
    option_distribution.to_csv('../RQ6_option_distribution_'+ compiler +'.csv', index=False) 