import numpy as np
n = int(input("Enter an integer: "))
len = 2*n
x = ['']*(len+1)
x[0] = '@'
c = 0


def brackets( k):
    if k > len:
        output(x)
    else:
        for i in ['(', ')']:
            x[k] = i
            if legal(k):
                 brackets(k+1)


def output(x):
    global  c
    c = c + 1
    for i in range(1,len+1):
        print(x[i],end=' ')
    print('\n')


def legal(k):
    r = 0
    p = 0
    for i in range(1,k+1):
        if x[i] == '(':
            r = r + 1
            p = p + 1
        elif x[k] == ')':
            p = p - 1
    if r <= n and 0 <= p <= n:
        return True
    else:
        return False


brackets(1)
print("c={}".format(c))