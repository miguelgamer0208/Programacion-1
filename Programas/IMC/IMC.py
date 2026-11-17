import time
print("Calculadora de IMC")
nombre=input("¿Cual es tu nombre?* ")
if len(nombre)<=0:
    print("Error: No puedes dejar este espacio vacio")
else:
    edad= int(input("¿Cual es tu edad?[18,60 años]*: "))
    if edad<18 or edad>60:
        print("Error: Edad fuera del rango esperado o no valido")
    else:
        peso= float(input("¿Cual es tu peso?[40,90 kg]*: "))
        if peso <40 or peso>90:
            print("Error: Ese valor de peso no es valido")
        else:
            altura= float(input("¿Cual mides?[1.5,2.1 metros]: "))
            if altura<1.5 or altura>2.1:
                print("Error: Valor de altura no es valido")
            else:
                imc= peso/altura**2
                print(f"{nombre}, tus resultados dieron un indice de masa corporal de {imc:.2f}%,\nen base a los datos dados de edad({edad}),peso({peso}kg),altura({altura}mts)")
                time.sleep(2)
            if imc>=18 and imc<25:
                print("Estas con un peso normal segun tu indice de masa corporal")
            elif imc<18:
                print("Estas bajo de peso,segun tu indice de masa corporal")
            elif imc>=25:
                print("Estas con exceso de peso/sobrepeso, segun tu indice de masa corporal")