import pandas
from matplotlib import pyplot

SOURCE = 'datset_TSE.csv'

def show_barh(sym_gcc:dict, sym_llvm:dict, fig_name:str):
    value_1=[]
    value_2=[]
    for key in sym_gcc.keys():
        value_1.append(sym_gcc[key])
        if key in sym_llvm:
            value_2.append(sym_llvm[key])
        else:
            value_2.append(0)
    keys = list(sym_gcc.keys())
    pyplot.figure(figsize=(10, 6))
    pyplot.grid(axis='x')
    pyplot.gcf().subplots_adjust(left=0.2)
    bars = pyplot.barh(keys, value_1, height=0.4, label='GCC')
    for bar in bars:
        pyplot.text(bar.get_width()/2, bar.get_y(), s=bar.get_width(), ha='center', fontdict={'family':'Times New Roman','size':15})
    bars_2 = pyplot.barh(keys, value_2, height=0.4, left=value_1, label='LLVM')
    for bar, bar_2 in zip(bars, bars_2):
        pyplot.text(bar.get_width() + bar_2.get_width()/2, bar.get_y(), s=bar_2.get_width(), ha='center', fontdict={'family':'Times New Roman','size':15})
    pyplot.yticks(fontproperties='Times New Roman', size=15)
    pyplot.xticks(fontproperties='Times New Roman', size=15)
    pyplot.legend(loc=1, prop = {'family':'Times New Roman','size':15})
    pyplot.savefig(fig_name)

if __name__ == '__main__':
    records = pandas.read_csv(SOURCE, usecols=['Project', 'Symptom', 'Root Cause(patch)'], encoding='utf-8')
    symp_gcc={}
    symp_llvm={}
    rtc_gcc={}
    rtc_llvm={}
    for row in records.itertuples():
        if row[1] == 'GCC':
            if row[2] in symp_gcc:
                symp_gcc[row[2]] = symp_gcc[row[2]] + 1
            else:
                symp_gcc[row[2]] = 1
            if row[3] in rtc_gcc:
                rtc_gcc[row[3]] = rtc_gcc[row[3]] + 1
            else:
                rtc_gcc[row[3]] = 1
        else:
            if row[2] in symp_llvm:
                symp_llvm[row[2]] = symp_llvm[row[2]] + 1
            else:
                symp_llvm[row[2]] = 1
            if row[3] in rtc_llvm:
                rtc_llvm[row[3]] = rtc_llvm[row[3]] + 1
            else:
                rtc_llvm[row[3]] = 1
    symp_gcc = dict(sorted(symp_gcc.items(), key = lambda kv:(kv[1], kv[0]), reverse=True))
    symp_llvm = dict(sorted(symp_llvm.items(), key = lambda kv:(kv[1], kv[0]), reverse=True))
    rtc_gcc = dict(sorted(rtc_gcc.items(), key = lambda kv:(kv[1], kv[0]), reverse=True))
    rtc_llvm = dict(sorted(rtc_llvm.items(), key = lambda kv:(kv[1], kv[0]), reverse=True))
    show_barh(symp_gcc, symp_llvm, fig_name='fig_1.png')
    show_barh(sym_gcc=rtc_gcc, sym_llvm=rtc_llvm, fig_name='fig_2.png')
