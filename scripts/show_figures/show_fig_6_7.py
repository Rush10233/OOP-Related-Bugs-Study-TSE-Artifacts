from matplotlib import pyplot
import pandas
import numpy as np
from scipy.interpolate import interp1d

SOURCE_GCC_LINE='gcc_diff_distribution.csv'
SOURCE_LLVM_LINE='llvm_diff_distribution.csv'
SOURCE_GCC_FUNCTION='gcc_function_distribution.csv'
SOURCE_LLVM_FUNCTION='llvm_function_distribution.csv'

def my_round(data, pt_num = 2):
    return ('{:.'+str(pt_num)+'f}').format(data)

def extract_fraction(raw:list, pace=2, usepace=True):
    raw.sort()
    y_label=[]
    x_label=[]
    upper_bound = raw[-1]
    if usepace:
        for i in range((upper_bound // pace)+2):
            current = i * pace
            x_label.append(current)
            y_label.append(my_round((sum(j <= current for j in raw)) / len(raw)))
    else:
        for data in raw:
            if data in x_label:
                continue
            x_label.append(data)
            y_label.append(my_round((sum(j <= data for j in raw)) / len(raw)))
    return x_label, y_label

def plot2(x1, y1, x2, y2, figname, xlabel, legend=['LLVM','GCC']):
    #pyplot.axis([0, 410, 0, 1])
    #pyplot.plot(x1, y1)
    if len(x1) > len(x2):
        for j in range(len(x2), len(x1), 1):
            x2.append(x1[j])
            y2.append(1)
    else:
        for j in range(len(x1), len(x2), 1):
            x1.append(x2[j])
            y1.append(1)

    xnew = np.linspace(0, x1[-1], 5000)
    func_1 = interp1d(x1, y1, kind='cubic')
    func_2 = interp1d(x1, y2, kind='cubic')
    pyplot.figure(figsize=(9, 5))
    pyplot.gcf().subplots_adjust(bottom=0.2)
    pyplot.grid()
    pyplot.plot(xnew, func_1(xnew), color='r', linestyle='--', label=legend[0])
    pyplot.plot(xnew, func_2(xnew), color='b', label=legend[1])
    pyplot.legend(loc=4, prop = {'family':'Times New Roman','size':24})
    pyplot.xlabel(xlabel, fontdict={'family':'Times New Roman','size':28}, labelpad=15)
    pyplot.ylabel('Fraction of Bugs', fontdict={'family':'Times New Roman','size':28},labelpad=15)
    pyplot.xticks(fontproperties='Times New Roman', size=25)
    pyplot.yticks(fontproperties='Times New Roman', size=25)
    pyplot.savefig(figname)

def show(source_gcc:str, source_llvm:str, pace:int, y_label:str, figname:str):
    record_gcc = pandas.read_csv(source_gcc)
    record_llvm = pandas.read_csv(source_llvm)
    gcc_lines = []
    llvm_lines = []
    #print(record_gcc['gcc-add'])
    for row in record_gcc.itertuples():
        if(len(row)>3):
            total_row = row[2] + row[3]
        else:
            total_row = row[2]
        if total_row > 0:
            gcc_lines.append(total_row)
    for row in record_llvm.itertuples():
        if(len(row)>3):
            total_row = row[2] + row[3]
        else:
            total_row = row[2]
        if total_row > 0:
            llvm_lines.append(total_row)

    x1_label, y1_label = extract_fraction(llvm_lines, pace)
    x2_label, y2_label = extract_fraction(gcc_lines, pace)
    plot2(x1_label, y1_label, x2_label, y2_label, figname, y_label)


if __name__ == '__main__':
    show(SOURCE_GCC_LINE, SOURCE_LLVM_LINE, 10, 'Number of Lines of Code', 'fig_6.png')
    show(SOURCE_GCC_FUNCTION, SOURCE_LLVM_FUNCTION, 2, 'Number of Functions', 'fig_7.png')

