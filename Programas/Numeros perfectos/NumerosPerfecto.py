lm = int(input("Limite Maximo: "))
L= []
for n in range (1, lm-1):
    suma = 0
    for i in range(1, lm//2+1):
        if n % i == 0:
            suma += i
            if suma == n:
                L.append(n)
print("Numeros perfectos: ", L)