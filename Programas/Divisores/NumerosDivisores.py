import time
import math
time1 = time.time()
n = int(input("N = "))

L=[]
s=""
tm=float()
for i in range (1,int(math.sqrt(n))+1):
    if n%i==0:
        L.append(i)
        if i!=n//i:
          L.append(n//i)
L.sort()
print(f"Los divisores de {n} es:",L)
if time.time()-time1 <60:
    s="s"
    tm = time.time()-time1
elif time.time()-time1 >=60 and (time.time()-time1)/60< 60:
    s="m"
    tm = (time.time()-time1)/60
else:
    s="h"
    tm = (time.time()-time1)/(60**2)
print(f"tiempo transcurrido = {tm:.3f}{s}")