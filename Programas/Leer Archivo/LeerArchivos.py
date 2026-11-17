from os import system
from pathlib import Path
system('cls')

def analyze_file(filename):
    try:
        with open(filename, "r") as f:
            lines = f.readlines()

        print("Total de líneas:", len(lines))
        word_count = sum(len(line.split()) for line in lines)
        print("Total de palabras:", word_count)

        longest = max(lines, key=len)
        print("Línea más larga:", longest.strip())
    except FileNotFoundError:
        print("El archivo no existe.")
        return False
    except PermissionError:
        print("No tienes permiso para leer el archivo.")

# Main
print("Programa Dedicado a leer archivos, puede que con algunos no sea posible leerlos")
filename = input("Nombre del  archivo: ")
if len(filename)<=0 or filename=="":
    print("No es posible leer un archivo sin nombre")
else:
    with open (filename,"r") as f:
        while 1:
            analyze_file(filename)
            leer= input("¿Quieres ver el archivo? [y/n]\n>>").lower()
            if leer in ["y","n"]:
                if leer=="y":
                    print(f.read())
                break