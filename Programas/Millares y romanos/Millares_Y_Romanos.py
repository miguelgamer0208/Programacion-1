import time
import os

repetir = True
continuar = True
os.system('cls')
while repetir == True:
    n = int(input("Dime un numero: "))
    m = n // 1000
    r = n % 1000
    c = r // 100
    r = n % 100
    d = r // 10
    r = n % 10
    u = r // 1
    print(f"Ese numero tiene {m} millares, {c} centenas, {d} decenas y {u} unidades")
    time.sleep(1)
    
    if m >=1:
        m1 = str("M")*m
    
    if c == 9:
     c1 = str("CM")
    if c >= 5 and c < 9:
        c1 = str("D") + str("C")*(c-5)
    if c == 4:
        c1 = str("CD")
    if c >=1 and c < 4:
        c1 = str("C")*c
   
    if d == 9:
        d1 = str("XC")
    if d >= 5 and d < 9:
        d1 = str("L") + str("X")*(d-5)
    if d ==4:
        d1 = str("XL")
    if d >=1 and d < 4:
        d1 = str("X")*d

    if u == 9:
        u1 = str("IX")
    if u >=5 and u < 9:
        u1 = str("V") + str("I")*(u-5)
    if u == 4:
        u1 = str("IV")
    if u >=1 and u < 4:
        u1 = str("I")*u
        
    time.sleep(1)
    print(f"Tu numero en Romano seria: {m1}{c1}{d1}{u1}")
    time.sleep(1)
    continuar = input("Quieres repetir el programa? (y/n): ")
    continuar = continuar.lower()
    if continuar == "n" or not continuar in("y",""):
        repetir = False
    elif continuar in("y",""):
        repetir = True
        time.sleep(1)
        os.system('cls')