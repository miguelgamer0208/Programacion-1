import os
os.system("cls")

#De Miguel Angel Encinas Bustillos

print("Este programa dibuja triángulos con el símbolo que usted desee.\n")
while 1:
    try:
        a = int(input("Ingrese el número de filas (De preferencia mayor a 2): "))
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

for r in range (1,a+1):
    print(' '*(a-r),end="")
    print(s*(2*r-1),end="")
    print()
    
print('-'*(a+5))

for r in range (a,0,-1):
    print(' '*(a-r),end="")
    print(s*(2*r-1),end="")
    print()
    
print('-'*(a+5))

for r in range (1,a+1):
    print(' '*(a-r),end="")
    print(s*(2*r-1),end="")
    print()
for r in range (a-1,0,-1):
    print(' '*(a-r),end="")
    print(s*(2*r-1),end="")
    print()
    
print('-'*(a+5))
    
for r in range (a,1,-1):
    print(' '*(a-r),end="")
    print(s*(2*r-1),end="")
    print()
for r in range (1,a+1):
    print(' '*(a-r),end="")
    print(s*(2*r-1),end="")
    print()
    
        