import math
coef=input()
a,b,c=coef.split()
a = eval(a)
b = eval(b)
c = eval(c)
delta = b*b - 4*a*c
#如果方程无解
if delta < 0:
    print("方程无解")
#如果方程有一个解
elif delta == 0:
    x = -b/(2*a)
    print("方程有一个解:{:.2}".format(x))
#如果方程有两个解
else:
    x1 = (-b - math.sqrt(delta))/(2*a)
    x2 = (-b + math.sqrt(delta))/(2*a)
    print("方程有两个解:{:.2},{:.2}".format(x1,x2))
