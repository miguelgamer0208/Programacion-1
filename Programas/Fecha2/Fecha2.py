from os import system ; system('cls')
def ab(año):
  if año % 4==0 and año %100!=0 or año%400==0: return True
  else: return False
def nom_mes(mes):
    match mes:
        case 1: return "Enero"
        case 2: return "Febrero"
        case 3: return "Marzo"
        case 4: return "Abril"
        case 5: return "Mayo"
        case 6: return "Junio"
        case 7: return "Julio"
        case 8: return "Agosto"
        case 9: return "Septiempre"
        case 10: return "Octubre"
        case 11: return "Noviembre"
        case 12: return "Diciembre"
def diames(mes):
   match mes:
      case 1|3|5|7|8|10|12: return 31
      case 4|6|9|11: return 30
      case 2:
         if ab(año): return 29
         else: return 28
def nom_dia(redia):
   redia = redia%7
   match redia:
      case 0: return "Domingo"
      case 1: return "Lunes"
      case 2: return "Martes"
      case 3: return "Miercoles"
      case 4: return "Jueves"
      case 5: return "Viernes"
      case 6: return "Sabado"
      case _: return "Intenta con %7"
while 1:
    try:
        año= int(input("Elige/Di un año [Mayor a 1582]:\n>>"))
        if año<=1582: print("Error: Año fuera del rango\n")
        else: break
    except ValueError: print("Error: No son validos numeros que no sean enteros, ni el uso de caracteres no numericos\n")
while 1:
    try:
        mes= int(input("Elige/Di un mes [1,12]:\n>>"))
        if mes<1 or mes>12: print("Error: mes fuera del rango\n")
        else: break
    except ValueError: print("Error: No son validos numeros que no sean enteros, ni el uso de caracteres no numericos\n")
año_bisiesto=ab(año); nombre_mes=nom_mes(mes); limdia=diames(mes)
while 1:
    try:
        dia= int(input(f"Elige/Di un dia [1,{limdia}]:\n>>"))
        if dia<1 or dia>limdia: print("Error: dia fuera del rango\n")
        else: break
    except ValueError: print("Error: No son validos numeros que no sean enteros, ni el uso de caracteres no numericos\n")
a = (14 - mes) // 12; b = año - a; c = mes + 12*a - 2; redia = dia + b + b // 4 - b // 100 + b // 400 + 31*c // 12; nombre_dia= nom_dia(redia)
print (f"Ese dia es {nombre_dia} {dia} de {nombre_mes} del año {año}")