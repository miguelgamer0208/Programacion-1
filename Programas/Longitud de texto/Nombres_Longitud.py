print ("Este programa lee el nombre y apellido del usuario")
nombre = input("Tu Primer nombre: ")
nombre1 = input("Tu Segundo nombre: ")
apellido = input("Tu Primer apellido: ")
apellido1 = input("Tu Segundo apellido: ")
nc= nombre + " " +nombre1 + " "+ apellido + " "+ apellido1
print(nc.upper())
numc = len(nc)
print(f"Numero total de Caracteres es = {numc}")