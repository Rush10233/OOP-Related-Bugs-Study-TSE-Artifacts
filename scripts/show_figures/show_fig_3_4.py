from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
from scipy.interpolate import interp1d
from matplotlib import patches

SOURCE_GCC=pd.read_csv('RQ7_option_distribution_gcc.csv')
SOURCE_LLVM=pd.read_csv('RQ7_option_distribution_llvm.csv')

def plot_curry(source, figname:str):
    x0=np.array([i+1 for i in range(len(source))])
    y0=np.array(source['occurrence'])
    #print(x0)
    #print(y0)
    front=int(len(y0)*0.2)
    percentage=sum(y0[:front-1])/sum(y0)
    #print(percentage)
    x1=np.linspace(x0.min(),x0.max(),200)
    func=interp1d(x0,y0,kind='cubic')
    y1=func(x1)
    x_scale=['' for i in range(len(x1))]
    x_scale[39]='20%'
    fig,ax=plt.subplots()
    plt.figure(figsize=(9, 5))
    plt.gcf().subplots_adjust(bottom=0.2)
    ax.set_ylim([0,65])
    plt.axvline(x=int(x0.max() * 0.2),linestyle='--',color='r')
    text_y=int(y0.max()/2)
    text_x=int(x0.max()/2)
    plt.text(0,text_y,"%.2f%%" % (percentage*100),color='b',fontdict={'family':'Times New Roman','size':28})
    plt.text(text_x,text_y,"%.2f%%" % ((1-percentage)*100),color='b',fontdict={'family':'Times New Roman','size':28})
    plt.plot(x1,y1,color='black')
    plt.xticks(x1,x_scale,fontproperties='Times New Roman', size=25)
    plt.yticks(fontproperties='Times New Roman', size=25)
    plt.tick_params(axis='y',labelsize=20)
    #plt.yticks(y1,y1,fontsize=15)
    plt.xlabel('Options',fontdict={'family':'Times New Roman','size':28}, labelpad=10)
    plt.ylabel('Frequence',fontdict={'family':'Times New Roman','size':28}, labelpad=10)
    plt.savefig(figname, dpi=100)

def plot_bar(source, ylim, figname:str):
    #source=pd.read_csv(file)
    x0=np.array(source['option'])[:12]
    y0=np.array(source['occurrence'])[:12]
    color_set=[]
    for option in x0:
        if option[2]=='s':
            color_set.append('#8C9DD5')
        if option[2]=='O':
            color_set.append('#E68D8D')
        if option[2]=='f':
            color_set.append('#8CCF8C')
        if option[2]=='W':
            color_set.append('#D8D898')
    plt.rcParams['figure.figsize']=(16,8)
    fig,ax=plt.subplots()
    plt.gcf().subplots_adjust(bottom=0.3)
    ax.set_ylim([0,ylim])
    plt.grid(axis='y')
    plt.bar(x0,y0,color=color_set, width=0.4)
    plt.xticks(x0,x0,fontproperties='Times New Roman', size=28)
    plt.yticks(fontproperties='Times New Roman', size=28)
    plt.tick_params(axis='y',labelsize=26)
    #plt.yticks(y0,y0,fontsize=15)
    for i in range(len(ax.xaxis.get_major_ticks())):
        ax.xaxis.get_major_ticks()[i].label.set_ha('right')
        ax.xaxis.get_major_ticks()[i].label.set_rotation(40)
    plt.ylabel('Frequency',fontdict={'family':'Times New Roman','size':28}, labelpad=10)
    #plt.title(title,y=-0.4)
    handles,labels=plt.gca().get_legend_handles_labels()
    label_1=patches.Patch(color='#8C9DD5',label='Language Standard')
    label_2=patches.Patch(color='#E68D8D',label='General')
    label_3=patches.Patch(color='#8CCF8C',label='Flag')
    label_4=patches.Patch(color='#D8D898',label='Warning')
    handles.extend([label_1,label_2,label_3,label_4])
    plt.legend(handles=handles,prop = {'family':'Times New Roman','size':24})
    plt.savefig(figname, dpi=100)

if __name__ == '__main__':
    plot_curry(SOURCE_GCC, figname='fig_3(a).png')
    plot_curry(SOURCE_LLVM, figname='fig_3(b).png')
    plot_bar(SOURCE_GCC, 65,  figname='fig_4(a).png')
    plot_bar(SOURCE_LLVM, 35, figname='fig_4(b).png')