while 1:
    a=int(input("¿Año de nacimiento?[1900,2026]"))
    if a<1900 or a>2026:
        print("Error: año no valido/esperado\n")
    else:
        break
while 1:
    m=int(input("¿Mes de nacimiento?[1,12]"))
    if m<1 or m>12:
        print("Error: mes no valido\n")
    else:
        break
match m:
    case 1|3|5|7|8|10|12:
        dx=31
    case 4|6|9|11:
        dx=30
    case 2:
        if (a%4==0 and a%100!=0) or a%400==0:
            dx=29
        else:
            dx=28
while 1:
    d=int(input(f"¿Dia de nacimiento?[1,{dx}]"))
    if d<1 or d>dx:
        print("Error: dia no valido\n")
    else:
        break
a1=str(a)[2:]   
m1=str(m).zfill(2)
d1=str(d).zfill(2)
c1=d1+"/"+m1+"/"+a1
c=a1+m1+d1
print(c)
print(f"fecha normal= {c1}")