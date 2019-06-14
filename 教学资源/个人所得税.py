salary = eval(input(""))
base = 5000
taxR = [0.03, 0.1, 0.2, 0.25, 0.3, 0.35, 0.45]
#taxF = [0, 1500, 4500, 9000, 35000, 55000, 80000]
taxF = [0, 3000, 12000, 25000, 35000, 55000, 80000]
salary = salary - base
t = 0
i = 6
while i >= 0:
    if salary > taxF[i]:
        t = t + (salary-taxF[i])*taxR[i]
        salary = taxF[i]
    i = i - 1
print(t)
