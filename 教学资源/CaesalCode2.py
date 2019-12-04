alp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
s = input()
code = []
for i in range(len(s)):
    if 'A'<=s[i]<='Z' or 'a'<=s[i]<='z':
        c=s[i].upper()
        k = alp.index(c)
        k = (k+i+1)%26
        code.append(alp[k])
    else:
        code.append(s[i])
print("".join(code))
