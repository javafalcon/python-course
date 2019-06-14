# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 14:51:17 2018

@author: Administrator
"""

import jieba

excludes = {'什么','一个','我们','你们','如今','说道','老太太','知道','姑娘','起来',
            '这里','出来','众人','那里','奶奶','自己','太太','一面','只见','两个',
            '没有','怎么','不是','这个','听见','这样','进来','咱们','就是','不知',
            '东西','告诉','回来','只是','大家','老爷','只得','丫头','这些','他们',
            '不敢','出去','所以','不过','不好','姐姐','的话','一时','过来'
            }


txt = open('红楼梦.txt','r', encoding='GB18030').read()
words = jieba.lcut_for_search(txt)
counts = {}
for word in words:
    if len(word) == 1:
        continue
    elif word == '凤姐' or word == '熙凤':
        rword = '凤姐'
    elif word == '元春' or word == '贵妃':
        rword = '元春'
    else:
        rword = word
    counts[rword] = counts.get(rword,0) + 1

for word in excludes:
    del(counts[word])   
     
items = list(counts.items())
items.sort(key=lambda x: x[1], reverse = True)
for i in range(50):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word, count))
    


'''
# 统计金陵十二钗正册和副册人物出场次数，另外加上几个重要丫鬟袭人，紫鹃
includes = {'宝钗','黛玉','凤姐','元春','探春','湘云','妙玉','迎春','惜春','巧姐','李纨','可卿'
            ,'香菱','宝琴','二姐','三姐','岫烟','李纹','李绮','宝珠','宝蟾','平儿','娇杏','瑞珠','袭人','紫鹃','晴雯'}
txt = open('红楼梦.txt','r', encoding='GB18030').read()
words = jieba.lcut(txt)
counts = {}
for word in words:
    if word in includes:
        if word == '凤姐' or word == '熙凤':
            rword = '凤姐'
        elif word == '元春' or word == '贵妃':
            rword = '元春'
        elif word == '宝姑娘' or word == '宝钗':
            rword = '宝钗'
        elif word == '林姑娘' or word == '黛玉':
            rword = '黛玉'
        else:
            rword = word
        
        counts[rword] = counts.get(rword,0) + 1

items = list(counts.items())
items.sort(key=lambda x: x[1], reverse = True)
for i in range(20):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word, count))
'''