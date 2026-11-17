import os
os.system("cls")

print("De Miguel Angel Encinas Bustillos")

print("Este programa dibuja triángulos con el símbolo que usted desee.\n")
while 1:
    try:
        a = int(input("Ingrese el número de filas: "))
        break
    except:
        print("Error: Por favor, ingrese un número entero.\n")
print()
while 1:
    s= input("Ingrese el símbolo que desea usar: ")
    if len(s) == 1:
        break
    else:
        print("Error: Por favor, ingrese solo un carácter.\n")
#1
for r in range(1, a+1):
    for c in range(1, r+1):
        print(s,end='')
    print()

print('-'*(a+5))
#2
for i in range(a, 0,-1):
    for m in range(1, i+1):
        print(s,end='')
    print()

print('-'*(a+5),end='\n')
#3
for r in range (1,a+1):
    print(' '*(a-r),end="")
    print(s*r,end="")
    print()

print('-'*(a+5))
#4
for j in range(a,0,-1):
    print(' '*(a-j),end="")
    print(s*j,end="")
    print()
    
print('-'*(a+5))
#5
for r in range (1,(a*2)+1):
    if r<=a:
        print(s*r)
    else:
        print(s*(2*a-r))
        
print('-'*(a+5))
#6
for r in range (1,a+1):
    print(' '*(a-r),end="")
    print(s*r,end="")
    print()
for j in range(a-1,0,-1):
    print(' '*(a-j),end="")
    print(s*(j),end="")
    print()
    
print('-'*(a+5))
#7
for r in range (1,a+1):
    print(' '*(a-r),end="")
    print(s*(2*r-1),end="")
    print()
    
print('-'*(a+5))
#8
for r in range (a,0,-1):
    print(' '*(a-r),end="")
    print(s*(2*r-1),end="")
    print()
    
print('-'*(a+5))

#9
for r in range (1,a+1):
    print(' '*(a-r),end="")
    print(s*(2*r-1),end="")
    print()
for r in range (a-1,0,-1):
    print(' '*(a-r),end="")
    print(s*(2*r-1),end="")
    print()

print('-'*(a+5))
#10
for i in range (1,a+1):
    if i==1:
        print((a-i)*" ",end="")
        print(s,end="")
        print()
    else:
        if i==a:
            print((2*a-1)*s)
        else:
            print((a-1*i)*" ",end="")
            print(s,end="")
            print((2*i-3)*" ",end="")
            if i !=a:
                print(s)
print("-"*(a+15))
print()
for i in range (a-1,0,-1):
        if i==(a-1):
            print((2*a-1)*s)
        else:
            print((a-i-1)*" ",end="")
            print(s,end="")
            print((2*i-1)*" ",end="")
            if i !=a:
                print(s)
            if i==1:
                print((a-i)*" ",end="")
                print(s,end="")
                print()

print("-"*(a+15))
print()

for i in range (1,a+1):
    if i==1:
        print((a-i)*" ",end="")
        print(s,end="")
        print()
    else:
        print((a-1*i)*" ",end="")
        print(s,end="")
        print((2*i-3)*" ",end="")
        if i !=a+1:
            print(s)
for i in range (a-2,0,-1):
    print((a-i-1)*" ",end="")
    print(s,end="")
    print((2*i-1)*" ",end="")
    if i !=a:
        print(s)
        if i==1:
            print((a-i)*" ",end="")
            print(s,end="")
            print()


