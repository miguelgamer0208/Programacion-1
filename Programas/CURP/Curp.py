import time
curp=""
print("CURP\nSi no tienes Segundo Apellido o Segundo Nombre, dejalos en blanco,\nlos otros dos si o si deben estar")
time.sleep(2)
n1=str(input("Primer Nombre*: "))
n1=n1.upper()
if len(n1)!=0:
    n2=str(input("Segundo Nombre: "))
    n2=n2.upper()
    a1=str(input("Primer Apellido*: "))
    a1=a1.upper()
    if len(a1)!=0:
        a2=str(input("Segundo Apellido: "))
        a2=a2.upper()
        if (len(n1)>0 and len(n2)>0 and len(a1)>0 and len(a2)>0) :
            curp= a1[0:2] + a2[0] + n1[0]
        elif (len(n1)>0 and len(n2)>0 and len(a1)>0) or (len(n1)>0 and len(a1)>0):
            curp= a1[0:2] + "X" + n1[0]
        elif len(n1)>0 and len(a1)>0 and len(a2)>0:
            curp= a1[0:2] + a2[0] + n1[0]
        print(curp)
    else:
        print("Error:No dejar los espacios obligatorios en blanco")
else:
    print("Error:No dejar los espacios obligatorios en blanco")
