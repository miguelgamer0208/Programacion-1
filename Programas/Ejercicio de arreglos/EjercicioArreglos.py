from random import randrange
Alumnos= [];AlumnosMayor=[];S=0
for i in range(10):
    while 1:
        try:
            nombre=input(f"Nombre del Alumno {i+1}:\n>>").strip()
            if len(nombre)<1: nombre=str(i+1).strip()
            C=float(input(f"Calificacion del Alumno/a {nombre}:\n>>"))
            S+=C
            Alumnos.append([nombre,C])
        except ValueError: print("Como dejaste la calificacion vacia, su valor sera aleatorio");C=randrange(50,100);S+=C;break
promedio= S/len(Alumnos)
print(f"Promedio General: {promedio:.2f}\n")

for nombre,C in Alumnos:
    if C>S/len(Alumnos): AlumnosMayor.append([nombre,C])
print("Alumnos encima del promedio:",AlumnosMayor)