from os import system;system('cls')

ec= ["'","!","@","#","$","%","&","*","=",">","<","}","{","¿","?","¡","!","-","_","+","/","~",".",",",":",";","^",
     "[","]","´","¨","♀","Æ","§","Ü","♪","►","☼","♫","◄","↕","‼","¶","↨","↑","↓","→","←",]
def segura(con):
    mayus=False; num=False; espcar=False; minus=False; minimo=False
    for caracter in con:
        if caracter.isalpha():
            if caracter.isupper():mayus=True
            else:minus=True
        else: 
            if caracter.isdigit(): num=True 
            elif caracter in ec or not(caracter.isdigit() and caracter.isalpha()):espcar=True
        if len(con)>=10 and minimo==False:minimo=True
    if mayus and minus and num and espcar and minimo:return True
    return False
print("Verificador de seguridad de contraseñas.\n")
while 1:
        con=str(input("Ingresa una Contraseña (Recomendado minimo de 10 Caracteres):\n>>"))
        if len(con)<1:print("Error: No dejar la contraseña vacia, Por favor de ingresar un minimo de 1 Caracter\n")
        else: break
if segura(con): print("Contraseña Segura: ",con)
else: print("Contraseña no segura: ",con); print("A la proxima intenta hacer que tenga:\nMayusculas, Minusculas, Numeros, Caracteres Especiales y Que sea mas larga que 10 Caracteres")