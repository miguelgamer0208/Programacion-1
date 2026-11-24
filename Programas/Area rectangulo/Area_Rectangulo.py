from os import system as sys
sys('cls')

# No se hizo en si muchos cambios, mas solo se agregaron comprobaciones y se arreglo un error de texto que habia, para mayor certeza que el resultado fuera el correcto
while 1:
    try:
        ancho = float(input("¿Cual es el Ancho del rectangulo?\n>>"))
        if ancho!=None:
            break
    except:
        print("Ingrese un valor numerico/no vacio\n")

while 1:
    try:
        altura = float(input("¿Cual es la Altura del rectangulo?\n>>"))
        if altura!=None:
            break
    except:
        print("Ingrese un valor numerico/no vacio\n")
 
area = ancho * altura
print (f"El area del rectangulo en base a un ancho de {ancho},\n y una altura de {altura} es igual a {area}")