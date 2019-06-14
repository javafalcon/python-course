# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 13:06:11 2018

@author: Administrator
"""

from datetime import datetime
from random import *

# 随机生成n个人的生日，返回一个列表，列表中每一个元素的形如（月，日）
def generateSamples2(n:int):
    birthdays = []
    days = [31,28,31,30,31,30,31,31,30,31,30,31]
    
    for i in range(n): # 随机生成n个人的生日（月，日）
        year = randint(1950,2000)
        month = randint(1,12)
        if (year%400==0) and (year%4==0 and year%100 != 0):
            days[1] = 29
        else:
            days[1] = 28
        day = randint(1,days[month-1])
        
        someday = (month,day)
        birthdays.append(someday)
    
    return birthdays

# 计算在给定的样本列表birthdays中，23个人中至少有两人生日相同的概率
# 在函数中随机取23个人，计算是否有两人生日相同，重复n次来计算概率
# param n -- 计算概率时，事件的重复次数。n越大，计算的概率越接近真实值
def calSameBirthdayProb(n:int):
    num = 0
    for i in range(n):
        people = generateSamples2(23)
        pset = set(people)
        if len(pset) != len(people):
            num += 1
        
    return num/n

def main():
    while True:
        n = int(input("输入一个重复的次数："))
        if n<0:
            break
        print("重复{}次，23个人中至少有两人生日相同的概率是：{}".format(n, calSameBirthdayProb(n)))
    

main()   

    
