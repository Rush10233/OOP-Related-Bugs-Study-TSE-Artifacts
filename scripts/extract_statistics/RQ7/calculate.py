import scipy.stats
import pandas

def calculate():
    source=open('RQ7_data.csv')
    tc_11=source.readline().strip().split(',')
    tc_12 = source.readline().strip().split(',')
    sym_1 = source.readline().strip().split(',')
    sym_2 = source.readline().strip().split(',')
    op_1 = source.readline().strip().split(',')
    op_2 = source.readline().strip().split(',')

    tc_11 =[int(x.strip()) for x in tc_11]
    tc_12 = [int(x.strip()) for x in tc_12]
    sym_1 = [int(x.strip()) for x in sym_1]
    sym_2 = [int(x.strip()) for x in sym_2]
    op_1 = [int(x.strip()) for x in op_1]
    op_2 = [int(x.strip()) for x in op_2]

    spearman=[0 for i in range(3)]
    spearman_p=[0 for i in range(3)]
    pearson=[0 for i in range(3)]
    pearson_p=[0 for i in  range(3)]
    spearman[0] = scipy.stats.spearmanr(tc_11,tc_12)[0]
    spearman[1] = scipy.stats.spearmanr(sym_1, sym_2)[0]
    spearman[2] = scipy.stats.spearmanr(op_1, op_2)[0]
    spearman_p[0] = scipy.stats.spearmanr(tc_11,tc_12)[1]
    spearman_p[1] = scipy.stats.spearmanr(sym_1, sym_2)[1]
    spearman_p[2] = scipy.stats.spearmanr(op_1, op_2)[1]
    pearson[0] = scipy.stats.pearsonr(tc_11,tc_12)[0]
    pearson[1] = scipy.stats.pearsonr(sym_1, sym_2)[0]
    pearson[2] = scipy.stats.pearsonr(op_1, op_2)[0]
    pearson_p[0] = scipy.stats.pearsonr(tc_11,tc_12)[1]
    pearson_p[1] = scipy.stats.pearsonr(sym_1, sym_2)[1]
    pearson_p[2] = scipy.stats.pearsonr(op_1, op_2)[1]

    outp=pandas.DataFrame(columns=['target','spearman','p_value_s','pearson','p_value_p'])
    outp['target']=['category','symptom','options']
    outp['spearman']=spearman
    outp['p_value_s']=spearman_p
    outp['pearson']=pearson
    outp['p_value_p']=pearson_p
    outp.to_csv('../RQ7_commonality.csv', index=False)
