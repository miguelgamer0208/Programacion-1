while 1:
    c=1
    try:
        n=int(input("Escribe un numero entero "))
    except ValueError:
        print("Por favor, escribe un numero entero.\n")
        continue
    while c<=10:
        print(f"{n}*{c}={n*c}")
        c+=1
    print("\n")