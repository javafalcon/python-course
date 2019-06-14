'''
对于字符串S，求它的最长回文子串，如果有多个相同长度的回文子串，选择字符串S中最先出现的回文子串。
解题方法：使用递归
假设已求出s[:-1]（即除s最后一个字符外的字串）的最长回文字串s1,
找出最后一个字符是s[-1]的回文字串s2
如果len(s2)>len(s1)则最长回文字串为s2
否则最长回文字串为s1
'''


def fun(s: str) -> str:
    n = len(s)
    if n == 1:
        return s[0]
    else:
        for j in range(n):
            if s[j:] == s[:j-n-1:-1]:#s[:j-n-1:-1]是s[j:]的反转字符串
                sub = s[j:]
                if len(sub) > len(fun(s[:-1])):
                    return sub
                break

        return fun(s[:-1])


s = "abeteba1234321cv"
sh = fun(s)
print(sh)



