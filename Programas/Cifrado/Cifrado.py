from os import system; system('cls');alpha='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
mensaje= input("Mensaje a cifrar/descifrar:\n>>")
def cifrado(a,y,x,o):
    x%=len(y)
    z=''
    for n in range(0,len(a)):
        if a[n] not in y: z+=a[n];continue
        for i in range(0,len((y))):
            if y[i] == a[n] and o==1:z+=y[(i+x)%len(y)]
            elif y[i] == a[n] and 2<=o<=3:z+=y[(i-x)%len(y)]
    return z
def cifrado2():
    while 1:
        try:
            if opt==1:x= int(input("Ingrese un numero entero para el Cifrado\n>>"))
            else: x= int(input("Ingrese un numero entero para el Descifrado\n>>"))
            if x<1: print("Error: El Valor tiene que ser positivo\n")
            else:return x
        except: print("Error: Ingrese un numero entero, no decimal, y que no sea un caracter no numerico\n")
while 1:
    try:
        opt= int(input("Desea:\n1)Cifrar\n2)Descifrar Manual\n3)Descifrar Auto\n>>"))
        if opt<1 or opt>3: print("Error: El Valor esta fuera del rango, por lo que es invalido\n")
        else: break
    except: print("Error: Ingrese un numero entero, no decimal, y que no sea un caracter no numerico\n")

if 1<=opt<=2:x=cifrado2(); men_c=cifrado(mensaje,alpha,x,opt)
else:
    for p in range(0,len(alpha)):
        men_c=cifrado(mensaje,alpha,p,opt)
        if p<=9 and p%2!=0 and p!=2: print(f"Intento #0{p}: {men_c}"+ " "*4, end='\t')
        elif p<=9 and p%2==0: print(f"Intento #0{p}: {men_c}"+ " "*4, end='\n')
        elif p%2!=0 and p>9:print(f"Intento #{p}: {men_c}"+ " "*4, end='\t')
        elif p%2==0 and p>9:print(f"Intento #{p}: {men_c}"+ " "*4, end='\n')
if opt==1:print(f"Mensaje Cifrado: {men_c}, Original: {mensaje}")
elif opt==2:print(f"Mensaje Descifrado: {men_c}, Cifrado: {mensaje}")