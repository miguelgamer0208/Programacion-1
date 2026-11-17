import time; from os import system; system('cls')
def romano(m,c,d,u):
    r=""
    match m:
        case 1|2|3: r+= "M"*m
    match c:
        case 1|2|3: r+= "C"*c
        case 4: r+= "CD"
        case 5|6|7|8: r+= "D" + "C"*(c-5)
        case 9: r+= "CM" 
    match d:
        case 1|2|3: r+= "X"*d
        case 4: r+= "XL"
        case 5|6|7|8: r+= "L" + "X"*(d-5)
        case 9: r+= "XC"
            
    match u:
        case 1|2|3: r+= "I"*u
        case 4: r+= "IV"
        case 5|6|7|8: r+= "V" + "I"*(u-5)
        case 9: r+= "IX"  
    return r
repetir = True; continuar = True
while repetir:
    try:
        n = int(input("Dime un numero[1,3999]:\n>>"))
        if n<1 or n>3999: print("Error: Valor no puede ser menor a 1 o mayor a 3999\n")
    except ValueError: print("Error:Pon un numero entero/no pongas caracteres no numericos\n")
    m = n // 1000; c = (n // 100)%10; d = (n // 10)%10; u = n%10
    
    r = romano(m,c,d,u);print("Tu numero en Romano seria: ",r);    time.sleep(1)
    continuar = input("Quieres repetir el programa? (y/n):\n>>"); continuar = continuar.lower()
    if continuar == "n" or not continuar in("y",""):repetir = False
    elif continuar in("y",""): repetir = True;time.sleep(1);os.system('cls')