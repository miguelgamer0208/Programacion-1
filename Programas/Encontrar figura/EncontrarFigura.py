import numpy as np;from os import system
system('cls')

def p(x):
    while True:
        r = input(f"{x} 1) Sí | 2) No\n>> ").strip()
        if r in ("1", "2"):
            return r == "1"
        print("Opción no válida; escribe 1 o 2.")


figuras = np.array([
    ["Triangulo Verde", "Cuadrado Verde", "Circulo Verde", "Rombo Verde"],
    ["Triangulo Rojo", "Cuadrado Rojo", "Circulo Rojo", "Rombo Rojo"],
    ["Triangulo Azul", "Cuadrado Azul", "Circulo Azul", "Rombo Azul"],
])

# Primero se identifica el color, eligiendo entre las filas candidatas.
filas = np.arange(figuras.shape[0])

while filas.size > 1:
    i = int(np.random.choice(filas))
    c = figuras[i, 0].split()[-1]

    print(figuras[filas, :])
    if p(f"¿Tu figura es de color {c}?"):
        filas = filas[filas == i]
    else:
        filas = filas[filas != i]

# Después se identifica la forma entre las columnas candidatas.
columnas = np.arange(figuras.shape[1])

while columnas.size > 1:
    i = int(np.random.choice(columnas))
    f = figuras[filas[0], i].split()[0]

    print(figuras[filas[0], columnas])
    if p(f"¿Tu figura tiene forma de {f}?"):
        columnas = columnas[columnas == i]
    else:
        columnas = columnas[columnas != i]

print("Tu figura es:", figuras[filas[0], columnas[0]])