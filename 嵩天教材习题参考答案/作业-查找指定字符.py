'''
编写程序，从用户给定字符串中查找某指定的字符。
'''


def query(s:str, ch:chr)->int:
    ind = -1
    for i in range(len(s)):
        if s[i] == ch:
            ind = i
    return ind


s=input("请输入字符串：")
ch=input("请输入要查找的字符：")
print("index={}".format(query(s,ch)))