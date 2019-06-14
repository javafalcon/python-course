n = input("please enter an integer:")
m = n[::-1]
if n== m:
    print("{} 是回文".format(n))
else:
    print("{}不是回文".format(n))
