import random
p["1",1,"si","yes"," "]
repetir=True
def numrand():
    n=random.randint(1,100000000000000000000)
    print(n)
while 1:
    numrand()
    repetir2=int(input("Quieres repetirlo?\n>>"))
    if repetir2.lower in p:
        repetir = True