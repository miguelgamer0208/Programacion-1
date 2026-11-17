import math;import time
def perfecto(x):
    suma=1
    for i in range(2,int(math.sqrt(x)+1)):
        if x%i==0:suma+=i; suma+= x//i
    if suma==x: return True
    else: return False
    
def tiempoT(x):
    if time.time()-x <60:
        s="seg";tim =time.time()-x
    elif time.time()-x >=60 and (time.time()-x)/60< 60:
        s="min";tim = (time.time()-x)/60
    else:
        s="hr";tim = (time.time()-x)/(60**2)
    print(f"tiempo transcurrido = {tim:.3f}{s}")
    
def nprimo(x):
    if x != 2 and (x % 2 == 0 or (x % 5 == 0 and x != 5)):return False
    elif x!=2:    
        for i in range(3,int(math.sqrt(x)+1),2):
            if x%i==0:return False
    return True

def nom_mes(x):
    match x:
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

def ab(x):
  if x % 4==0 and x %100!=0 or x%400==0: return True
  else: return False

def diames(x):
   match x:
      case 1|3|5|7|8|10|12: return 31
      case 4|6|9|11: return 30
      case 2:
         if ab(x): return 29
         else: return 28
         
def nom_dia(a,b,c):
   p = (14 - b) // 12; q = c - p; k = b + 12*p - 2; x = a + q + q // 4 - q // 100 + q // 400 + 31*k // 12
   x = x%7
   match x:
      case 0: return "Domingo"
      case 1: return "Lunes"
      case 2: return "Martes"
      case 3: return "Miercoles"
      case 4: return "Jueves"
      case 5: return "Viernes"
      case 6: return "Sabado"
      case _: return "Null"
def cifrado(a,y,x,o):
    x%=len(y)
    z=''
    for n in range(0,len(a)):
        if a[n] not in y: z+=a[n];continue
        for i in range(0,len((y))):
            if y[i] == a[n] and o==1:z+=y[(i+x)%len(y)]
            elif y[i] == a[n] and 2<=o<=3:z+=y[(i-x)%len(y)]
    return z