from time import sleep;from os import system;system('cls')
while 1:
    l = ["Aguas Calientes","Baja California","Baja California Sur","Campeche","Coahuila","Colima","Chiapas","Chihuahua",
         "Distrito Federal","Durango","Guanajuato","Guerrero","Hidalgo","Jalisco","Mexico","Michoacan","Morelos","Nayarit",
         "Nuevo Leon","Oaxaca","Puebla","Queretaro","Quintana Roo","San Luis Potosi","Sinaloa", "Sonora","Tabasco","Tamaulipas",
         "Tlaxcala","Veracruz","Yucatan","Zacatecas"]
    l2= ["AS","BC","BS","CC","CL", "CM","CS","CH","DF","DG","GT","GR","HG","JC","MC","MN","MS","NT",
         "NL","OC","PL","QT","QR","SP","SL","SR","TC","TS","TL","VZ","YN","ZS"]
    
    z=0
    while z<32:
        if z>0 and z%4==0 or z==6:print(str(z+1)+")"+l[z]);z+=1
        else:print(str(z+1)+")"+l[z],end='\t');z+=1
    try:
        e=int(input("\nEn cual de los Previos nacistes?* "))
        if e<=0 or e>32:print("Error: valor/estado no valido, Pon un estado/valor valido\n")
        else:break
    except:
        print("Error: valor/estado no valido, pon un numero entero/ no dejar vacio/ no uses letras\n")
print(f"Entonces naciste en {l[e-1]}, cual tiene una abreviacion: {l2[e-1]}")