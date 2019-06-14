for i in range(11):
    for j in range(11):
        if i%5 == 0:
            if j%5 == 0:
                print("+ ", end='')
            else:
                print("- ", end='')
        else:
            if j%5 == 0:
                print("| ", end='')
            else:
                print("  ", end='')
    print("\n")
