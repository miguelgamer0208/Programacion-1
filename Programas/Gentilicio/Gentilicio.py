import time
print("Programa de Gentilicio")
time.sleep(1)

print("1) Sonora. \n2) Chihuahua. \n3) Sinaloa. \n4) Baja Calif. \n5) Baja Calif.Sur")
e=int(input("En cual de los Previos nacistes? "))

if 1<=e<=5:
    match e:
        case 1:
            e2="Sonora"
            g="Sonorense"
        case 2:
            e2="Chihuahua"
            g="Chihuahense"
        case 3:
            e2="Sinaloa"
            g="Sinaloense"
        case 4:
            e2="Baja California"
            g="Bajacaliforniano"
        case 5:
            e2="Baja California Sur"
            g="Sudbajacaliforniano"
    time.sleep(1)        
    print(f"\nNaciste en {e2}, asi que eres {g}")
else:
    print("Opcion Invalida")