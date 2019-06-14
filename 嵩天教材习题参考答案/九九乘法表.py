for i in range(1,10):
    for j in range(1,i+1):
        line = str(i) + '*' + str(j) + '=' + str(i*j)
        print(line, end=' ')
    print('\n')
