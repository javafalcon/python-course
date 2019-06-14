# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 11:18:58 2018

@author: Administrator
"""

def isRepetitive(nList:list):
    nSet = set(nList)
    if len(nList) > len(nSet):
        return True
    else:
        return False
    
list1 = [1,2,1,3,1]
if isRepetitive(list1):
    print("有重复元素")
else:
    print("没有重复元素")
    
list2 = ['china', 'chinese']
if isRepetitive(list2):
    print("有重复元素")
else:
    print("没有重复元素")
    