import os
os.system("cls")

#De Miguel Angel Encinas Bustillos

print("Este programa dibuja triángulos vacios con el símbolo que usted desee.\n")
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
