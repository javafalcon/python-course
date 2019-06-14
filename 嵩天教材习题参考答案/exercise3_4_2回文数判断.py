n = input("输入一个5位数字: ")
j = -1
f = 1
for i in range(5):
    if n[i]  != n[j]:
        f = 0
    j = j - 1

if f == 1:
    print("{}是回文数".format(n))
else:
    print("{}不是回文数".format(n))
