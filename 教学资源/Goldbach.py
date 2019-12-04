def prime(n):
    flag=1
    for i in range(2,n):
        if n%i==0:
            flag=0
            break
    return flag

x=int(input(""))
for m in range(x//2,x):
    if prime(m):
        n = x-m
        if prime(n):
            print("{}={}+{}".format(x,n,m))
            break
        
