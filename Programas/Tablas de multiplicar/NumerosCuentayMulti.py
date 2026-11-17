n=int(input("Dime un numero: "))

for i in range(1,n+1):
    if i%5!=0 and i<n:
        print(i,end=',')
    else:
        print(i)
print('\n')

for i in range(1,11):
    if i%3!=0:
        print(f"{n}*{i}= {n*i}",end='\t')
    else:
        print(f"{n}*{i}= {n*i}")