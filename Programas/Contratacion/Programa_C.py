import time
print("Programa de Contratacion")
time.sleep(1)
c1=int(input("Calificacion del Examen 1:"))
c2=int(input("Calificacion del Examen 2:"))
time.sleep(0.5)

if c1>80 and c2>80:
    print("Contratado")
if c1<=80 or c2<=80:
    print("No Contratado")