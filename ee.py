#!/usr/bin/python3
import numpy as np
import pandas as pd

cc=pd.read_csv('abc.csv')
hh=cc.as_matrix()
print(hh)
print(type(hh))
ct=lambda x : pd.Series(1, index=x[pd.notnull(x)])
bb=map(ct, hh) # use line not coluen
for i in bb:
    print(i)
'''
print(bb)
for i in bb:
    print(i)
    dt=pd.DataFrame(i).fillna(0)
    print(dt)
'''