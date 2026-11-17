for n in range(1,11):
    for c in range(1,11):
        if c%5==0:
            print(f"{n}*{c}={n*c}",end='\n')
        else:
            print(f"{n}*{c}={n*c}",end='\t')
    print("\n")
