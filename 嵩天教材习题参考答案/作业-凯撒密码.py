'''
编写一个变种的恺撒密码程序，字母表的对应关系如下：
原文：A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
密文：M N O P Q R S T U V W X Y Z A B C D E F G H I J K L
假设用户可能使用的输入包含大小写字母a~zA~Z、空格和特殊符号，请编写一个程序，对输入字符串进行凯撒密码加密，直接输出结果，其中空格和特殊符号不用进行加密处理。
'''
def caesarCode(plainCode):
    sa = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    pa = 'MNOPQRSTUVWXYZABCDEFGHIJKL'
    pwCode=[]
    for p in plainCode:
        if ord("a") <= ord(p) <= ord("z") or ord("A") <= ord(p) <= ord("Z"):
            p = p.upper()
            i = sa.index(p)
            pwCode.append(pa[i])
        else:
            pwCode.append(p)
    return "".join(pwCode)


plainText = input("请输入明文：")
print("密文是：{}".format(caesarCode(plainText)))

