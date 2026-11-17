L= []
print("Este programa calcula los números que son amigos hasta un límite máximo que usted desee.\n")
lm = int(input("Limite Maximo: "))

for n in range(0,lm+1):
    z=0
    for i in range(1,n//2+1):
        if n%i==0:
            z+=i
    L.append(z)
    
for n in range(0,lm):
    if L[n]<lm+1 and n!=L[n] and n==L[L[n]]:
        print(f"{n} es amigo de {L[n]}")
        L[L[n]]=0