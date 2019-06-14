'''
我国身份证号码是18位数字和字母X的组合，其中前17位是数字，第18位是校验位，其值可以是数字或字母X。其中，第18位的校验方法如下：
1、将身份证号码前17位数分别乘以不同的系数：7 9 10 5 8 4 2 1 6 3 7 9 10 5 8 4 2
2、将上述17个相乘的结果求和，然后除以11，获得余数
3、余数0 1 2 3 4 5 6 7 8 9 10分别对应身份证号码的最后一位为1 0 X 9 8 7 6 5 4 3 2

例如：某身份证号码是210102198004256032，校验其正确性的过程如下：
首先：计算2*7+1*9+0*10+1*5+...+3*2，前17位的乘积和是230
然后：用230除以11余数为10
最后：余数10对应的校验位数字是2，因此，这是一个合格的身份证号码。
请编写一个程序，对用户输入的身份证号码进行校验，输出：合格或者不合格。
'''
def check(tid):
    alphabets='0123456789'
    clist = list(tid)
    # 身份证号码必须为18位
    if len(clist) != 18:
        return False

    # 验证身份证每个字符是否合法
    for c in clist[0:-1]: #前17位是数字
        if c not in alphabets:
            return False

    # 第18位是数字或字符
    if clist[-1] not in alphabets and clist[-1] != 'X':
        return False

    # 前17位乘以各自的系数
    w = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    s = 0
    for i in range(17):
        s += w[i]*( ord(clist[i]) - ord('0') )

    # 乘积和对11的余数
    r = s%11

    # 校验最后一位
    code = '10X98765432'
    if clist[-1] != code[r]:
        return False
    else:
        return True

while True:
    tid = input("请输入身份证号码：")
    if tid == "end":
        break
    if check(tid):
        print("{}是合法身份证号码".format(tid))
    else:
        print("{}不是合法身份证号码".format(tid))
