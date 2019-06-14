'''
4位水仙花数"是指一个四位整数，其各位数字的4次方和等于该数本身。例如：1634是一个"4位水仙花数"，因为1的4次方＋6的4次方＋3的4次方＋4的4次方 = 1634。
请按照从大到小的顺序输出所有的4位水仙花数，请用一个"逗号+空格"分隔输出结果。
'''

def daffodil(n:int):
    nlist = str(n)
    s = 0
    for a in nlist:
        s += pow(int(a),4)
    if s == n:
        return True
    else:
        return False

ds = []
for i in range(1000,10000):
    if daffodil(i):
        ds.append(i)
for n in ds[0:-1]:
    print(n, end=", ")
print(ds[-1])