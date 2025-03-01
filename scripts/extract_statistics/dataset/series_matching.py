import re
import pandas as pd


def data_proceeding(df:pd.DataFrame,name:str,accessibility:str):
    lst=df[name].drop(df[df[accessibility]==0].index).dropna(axis=0).tolist()
    return lst


def date_matching(source:str,target:str):
    res=re.search(pattern=source,string=target)
    if res is not None:
        return True
    else:
        return False

def importance_matching(source:str,is_gcc:bool):
    #gcc
    if is_gcc:
        res=re.search(pattern=r'P\d',string=source)
    #clang

        if res is not None:
            return True
        else:
            return False
    else:
        if len(source)>2 and source[0]=='P' and (source[1]==' 'or source[1]=='\n'):
            return True
        else:
            return False