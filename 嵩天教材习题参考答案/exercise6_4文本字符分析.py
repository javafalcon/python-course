# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 11:40:32 2018

@author: Administrator
"""
from operator import itemgetter

def analyseText(text):
    D = {}
    tlist = list(text)
    for e in tlist:
        if e in D:
            D[e] = D[e] + 1
        else:
            D[e] = 1
            
    return D
            
text="E:/Repoes/pythonProgram/TextbookExercise/exercise6_2重复元素判定.py"
D = analyseText(text)
'''
items = list(D.items())
items.sort(key=itemgetter(1), reverse=True)

for item in items:
    ch, count = item
    print("{0:<10}{1:>5}".format(ch,count))
    
'''
D = sorted(D.items(),key=itemgetter(1), reverse=True)
for d in D:
    ch, count = d[0],d[1]
    print("{0:<10}{1:>5}".format(ch,count))