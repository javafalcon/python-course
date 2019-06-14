#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 16 08:06:28 2018

@author: weizhong
"""
#read data to a list from score.csv
fr = open('score.csv','r')
ls = []
for line in fr:
    line = line.replace("\n","")
    ls.append(line.split(","))
fr.close()

#statistic max_score, min_score, avg_score 
className = ls[0][1:]
max_score = [0,0,0]
min_score = [100,100,100]
avg_score = [0,0,0]

for stu in ls[1:]:
    for i in range(3):
        #i=1: language; i=2: mathmatic; i=3: english
        score = int(stu[i+1])
        if score > max_score[i]:
            max_score[i] = score
        elif score < min_score[i]:
            min_score[i] = score
        
        avg_score[i] += score

for i in range(3):
    avg_score[i] = avg_score[i]/( len(ls) - 1)
    
#output
for i in range(3):
    print(" {}的最高分是： {}，最低分是：{}， 平均分是：{}".format(className[i], max_score[i], min_score[i], avg_score[i]))

#calculate total score
ls[0].append("总成绩")
for i in range(1, len(ls)):
    total = 0
    for j in range(1, len(ls[i])):
        total += int(ls[i][j])
    ls[i].append(str(total))

#write data into newscore.csv
fw = open("newscore.csv","w")
for row in ls:
    fw.write(",".join(row) + "\n")
fw.close()


        
            


    