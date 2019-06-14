# -*- coding: utf-8 -*-
"""
Created on Tue May  8 13:25:35 2018

@author: Administrator
"""
import keyword

kws = keyword.kwlist



file = input("读取的文件：")
fr = open(file,'r',encoding='utf-8')
wline = ''
for line in fr:
    wline += '\n'
    if 'import' in line:
        wline += line
  
    else:
        j = 0
        while line[j] == ' ': 
            wline += ' '
            j += 1
        sline = line.split()
        for w in sline:
            if w in kws:
                wline += w
            elif '.' in w: #包含.操作符
                wline += w
            elif '(' in w:#没有.操作符，但是函数调用
                wline += w
            else:
                wline += w.upper()
            wline += ' '
   
fr.close()

fw = open(file,'w',encoding='utf-8')
fw.write(wline)
fw.close()
              

        