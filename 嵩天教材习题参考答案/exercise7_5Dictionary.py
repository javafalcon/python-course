#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 15 20:02:03 2018

@author: weizhong
"""
import os

def userOperateInterface():
    print("\n请选择词典功能")
    print("i: 添加单词")
    print("s: 查询单词")
    print("Q: 退出词典")
    print("请选择功能：")
    return input()

def addWord(wordDict:dict, fileName):
    str = input("您输入要加入的单词：")
    if str in wordDict.keys():
        print("该单词已添加到字典库\n")
        userOperateInterface()
    else:
        t = input("请输入此单词的中文释义：")
        wordDict[str] = t
        with open(fileName, 'a') as fw:
            fw.write(str + "  " + t + '\n')

def selectWord(wordDict:dict):
    str = input("请输入您要查询的单词：")
    if str not in wordDict.keys():
        print("字典库中未找到这个单词\n")
    else:
        print(wordDict[str])


def main():
    wordDict = {}
    if os.path.exists("dict.txt"):
        with open("dict.txt", 'r') as fr:
            for ln in fr:
                s = ln.split(" ")
                wordDict[s[0]] = s[1]
    else:
        fw = open("dict.txt",'w')
        fw.close()
    print("******欢迎使用简明英汉词典******")
    while True:
        op = userOperateInterface()
        if op == 'i':
            addWord(wordDict, 'dict.txt')
        elif op == 's':
            selectWord(wordDict)
        elif op == 'Q':
            break
        else:
            print("输入有误\n")


main()