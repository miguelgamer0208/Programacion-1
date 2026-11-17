import numpy as np

edades= np.array([18,20,225], dtype=np.uint8)

print(edades.dtype)
print(edades)

a=np.array([120],dtype=np.int8)
b=np.array([10],dtype=np.int8)
print(a+b)

resultado=a.astype(np.int16) + b.astype(np.int16)
print(resultado)

r2= b.astype(np.float16)/ a.astype(np.float16)
print(r2)

for i in (np.float16, np.float32, np.float64):
    n= i(np.pi)
    print(i.__name__,float(n))
    
l=np.finfo(np.float64)
print(l.min);print(l.max)

c=np.array([1,2,3]);d=np.array([4,5,6])
suma=c+d;print(suma)
pc=c*2;print(pc)
c2=c-d;print(c2)
p= c.dot(d);print(p)
norma=np.linalg.norm(c);print(norma)
print(c@d)