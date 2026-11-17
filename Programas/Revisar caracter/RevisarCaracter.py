c=input("Escribe un Caracter: ")
while len(c)!=1 or c in '0123456789':
    print("Error:Debes escribir un Caracter.\n")
    c=input("Escribe un Caracter: ")
if c in 'aeiouAEIOU':
    print("Es una vocal")
elif c in '0123456789':
    print("Es un digito")
elif c in '0123456789':
    print("Es un Caracter Especial")
else:
    print("Es una consonante")
    