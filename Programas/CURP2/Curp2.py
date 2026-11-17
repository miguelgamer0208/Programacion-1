#De Miguel Angel Encinas Bustillos, con una funcion para ahorrarme lineas... y arreglos

import time
import os
os.system("cls")

i=int(0)
p=int(1)
d =0
def consonanteinterna(x):
    global p;p=1
    while p<=len(x):
        if x[p] not in v:return x[p];break
        elif (x[p] in v and p==len(x)-1) or x[p]=="Ñ" or p>=len(x):return "X";break
        p+=1

np=["LOCA","LOCO","BUEI","BUEY","CACA","CACO","CAGA","CAGO","CAKA","CAKO","COGE","COGI","COJA","COJE","COJI","COJO","COLA","CULO","FALO","FETO",
    "GETA","GUEI","GUEY","JOTO","KACA","KACO","KAGA","KAGO","KOGE","KOGI","KOJA","KOJE","KOJI","KOJO","KOLA","KULO",
    "LOCA","LOCO","LOKA","LOKO","MAME","MAMO","MEAR","MEAS","MEON","MIAR","MION","MOCO","MOKO",
    "MULA","MULO","NACA","NACO","PEDA", "PEDO", "PENE", "PIPI", "PITO", "POPO", "PUTA", "PUTO", "QULO",
    "RATA", "ROBA", "ROBE", "ROBO", "RUIN","SENO","TETA","VACA","VAGA","VAGO","VAKA","VUEI","VUEY","WUEI","WUEY"]
npr= ["LXCA","LXCO","BXEI","BXEY","CXCA","CXCO","CXGA","CXGO","CXKA","CXKO","CXGE","CXGI","CXJA","CXJE","CXJI","CXJO","CXLA","CXLO","FXLO","FXTO",
    "GXTA","GXEI","GXEY","JXTO","KXCA","KXCO","KXGA","KXGO","KXGE","KXGI","KXJA","KXJE","KXJI","KXJO","KXLA","KXLO",
    "LXCA","LXCO","LXKA","LXKO","MXME","MXMO","MXAR","MXAS","MXON","MXAR","MXON","MXCO","MXKO",
    "MXLA","MXLO","NXCA","NXCO","PXDA", "PXDO", "PXNE", "PXPI", "PXTO", "PXPO", "PXTA", "PXTO", "QXLO",
    "RXTA", "RXBA", "RXBE", "RXBO", "RXIN","SXNO","TXTA","VXCA","VXGA","VXGO","VXKA","VXEI","VXEY","WXEI","WXEY"]
nom=["JOSE","MARIA","MA.","MA","J","J."];v= ["A","E","I","O","U"]
sx="";c1="";c2="";c3="";c4=""


print("Bienvenido al generador de CURP, por favor llena los campos obligatorios")
print("Este programa muestra tu curp en base a los datos que ingreses")
time.sleep(2)
print("Programa de Miguel Angel Encinas Bustillos\n")
time.sleep(2)
while 1:
    a1=str(input("Primer Apellido*: "))
    a1=a1.upper()
    if len(a1)!=0:
        c1=c1 + a1[0]
        break
    else:
        print("Error:No dejar los espacios obligatorios en blanco\n")
while p < len(a1): 
    if a1[p] in v:
        c1 = c1 + a1[p]
        p = 1
        break
    p+=1
    if p >= len(a1):
        c1 = c1 + "X"
        p = 1
        break
    if p >= len(a1):
        c1 = c1 + "X"
        break
while len(a1)!=0:
    a2=str(input("Segundo Apellido: "))
    a2=a2.upper()
    if len(a2)==0:
        c1= c1 + "X"
        break
    else:
        c1 = c1 + a2[0]
        break
while len(a2)!=0:
    n1=str(input("Primer Nombre*: "))
    n1=n1.upper()
    n2=""
    if n1 in nom:
        print("Como tu primer nombre es muy comun, se tomara tu segundo nombre para la curp\n")
        n2=str(input("Segundo Nombre: "))
        n2=n2.upper()
    if len(n2)!=0 and len(n1)!=0:
            c1 = c1 + n2[0]
            break
    elif len(n1)!=0 and len(n2)==0:
            c1 = c1 + n1[0]
            break
    else:
        print("Error:No dejar los espacios obligatorios en blanco\n")
while i<len(c1):
    if c1[i] == "Ñ":
        c1 = c1.replace("Ñ", "X")
    i+=1
i=0

while i<len(c1):
    if c1 in np[i]:
        c1 = npr[i]
    i+=1
i=0
while 1:
    sx=str(input("Genero/Sexo*[H/M]: "))
    sx=sx.upper()
    if len(sx)!=0 and sx in("H","M"):
        c3= c3+ sx
        break
    print("Por favor, escribe H para hombre o M para mujer.\n")
while 1:
    try:
        a=int(input("¿Año de nacimiento?*[1900,2026]"))
        if a<1900 or a>2026:
            print("Error: año no valido/esperado, ingresa uno dentro del rango\n")
        else:
            c2 = c2 + str(a)[2:]
            break
    except:
        print("Error: año no valido/esperado, no dejar el espacio vacio/ no poner letras/ pon numeros enteros\n")
while 1:
    try:
        m=int(input("¿Mes de nacimiento?*[1,12]"))
        if m<1 or m>12:print("Error: mes no valido, ingresa uno dentro del rango\n")
        else:c2 = c2 + str(m).zfill(2);break     
    except:print("Error: mes no valido, pon un numero entero/no poner letras/ no dejar vacio\n")
match m:
    case 1|3|5|7|8|10|12:d=31
    case 4|6|9|11:d=30
    case 2:
        if (a%4==0 and a%100!=0) or a%400==0:d=29
        else:d=28
 
while 1:
    try:
        d1=int(input(f"¿Dia de nacimiento?*[1,{d}]"))
        if d1<1 or d1>d:
            print("Error: dia no valido\n")
        else:
            c2 = c2 + str(d1).zfill(2)
            break
    except:
        print("Error: dia no valido, ingresa un numero entero/no dejar vacio/ no uses letras\n")
while 1:
    l = ["Aguas Calientes","Baja California","Baja California Sur","Campeche","Coahuila","Colima","Chiapas","Chihuahua",
         "Distrito Federal","Durango","Guanajuato","Guerrero","Hidalgo","Jalisco","Mexico","Michoacan","Morelos","Nayarit",
         "Nuevo Leon","Oaxaca","Puebla","Queretaro","Quintana Roo","San Luis Potosi","Sinaloa", "Sonora","Tabasco","Tamaulipas",
         "Tlaxcala","Veracruz","Yucatan","Zacatecas"];z=0
    while z<32:
        if z>0 and z%3==0:
            print(str(z+1)+")"+l[z]);z+=1
        else:
            print(str(z+1)+")"+l[z],end='\t');z+=1
            
    l2= ["AS","BC","BS","CC","CL", "CM","CS","CH","DF","DG","GT","GR","HG","JC","MC","MN","MS","NT",
         "NL","OC","PL","QT","QR","SP","SL","SR","TC","TS","TL","VZ","YN","ZS"]
    try:
        e=int(input("\nEn cual de los Previos nacistes?* "))
        if e<=0 or e>32:
            print("Error: valor/estado no valido, Pon un estado/valor valido\n")
            time.sleep(2)
        else:c3=c3 + l2[e-1];break
    except:print("Error: valor/estado no valido, pon un numero entero/ no dejar vacio/ no uses letras\n")
if len(n2)!=0 and n1 in nom:c4=consonanteinterna(a1)+consonanteinterna(a2)+consonanteinterna(n2)
else:c4=consonanteinterna(a1)+consonanteinterna(a2)+consonanteinterna(n1)
c4=c4.replace("Ñ","X")
c=c1+c2+c3+c4
print(c)