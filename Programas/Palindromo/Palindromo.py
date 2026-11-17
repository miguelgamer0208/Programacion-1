cce= input("Escribe una cadena/Frase: ")
cce2 = cce.replace(" ","")
print (f"Cadena Original: {cce}\nCadena sin espacios: {cce2}")

cce3 = ""
for i in range(len(cce2) - 1, -1, -1):
    cce3 += cce2[i]
    
cce4= cce.split()
print(f"La cadena tiene {len(cce4)} palabras\n")

print(cce3)

if cce3==cce2:
    print("Es palindroma")
else:
    print("No es palindroma")