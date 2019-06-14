dayup, dayfactor = 1.0, 0.01
for i in range(365):
    if i % 7 not in [3,4,5,6]:
        dayup = dayup * (1 + dayfactor)
print("连续学习3天能力值不变，从第4天至第7天每天能力增长为前一天1%的力量: {:.2f}.".format(dayup))
