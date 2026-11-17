s = str(input("Escribe una Palabra: "))
print(f"{s} tiene { len(s)} caracteres")
c= int(0)
while (c < len(s)):
    print(f"la letra #{c+1} de {s}= {s[c]}")
    c += 1
    