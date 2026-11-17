import math

def ar(x,y):
    return x*y
def areacirculo(r):
    a= math.pi
    return a*(r**2)
def add(a,b):
    return a + b
def par(n):
    if n%2==0:
        return True
    else:
        return False
print("area")
x= float(input("Valor de x: "))
y= float(input("Valor de y: "))
print(f"{ar(x,y):.0f}\n")

print("suma")
a= float(input("Valor de a: "))
b= float(input("Valor de b: "))
print(f"{add(x,y):.0f}\n")

print("Area circulo")
z= float(input("Valor de z: "))
print(f"{areacirculo(z):.2f}\n")

L= []
rango= int(input("Hasta Donde quieres que sea el rango?: "))
for i in range (0,rango+1):
    if par(i):
        L.append(i)
    else:
        continue
print("Numeros pares de ese rango: ",L)
        
