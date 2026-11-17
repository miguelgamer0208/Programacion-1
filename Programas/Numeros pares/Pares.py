
try:
    n=int(input("Escribe un numero entero "))
except ValueError:
    print("Por favor, escribe un numero entero.\n")

for c in range(1,n+1):
    if c%2==0 and c%20!=0:
        print(c,end='\t')
    elif c%2==0 and c%5==0:
        print(c)