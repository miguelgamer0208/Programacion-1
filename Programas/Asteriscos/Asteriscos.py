import time as tm
while 1:
    try:
        m= int(input("Escribe un numero entero: "))
        break
    except:
        print("Por favor, escribe un numero entero.\n")
        continue

for i in range(1,8):
    print("*",end="")

print("\n")
tm.sleep(1)

for i in range(1,6):
    print("*")

print("\n")
tm.sleep(1)

for j in range(1,4):
    for i in range(1,5):
        print("*",end="")
    print()


print("\n")
tm.sleep(1)


for j in range(1,m+1):
    for i in range(1,j+1):
        print("*"*i)
    print("")

print("\n")
tm.sleep(1)


for j in range(m,0,-1):
    for i in range(1,j+1):
        print("*",end="")
    print("")
