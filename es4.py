figura = input("Scegliere di quale figura si vuole calcolare l'area,quadrato,rettangolo,triangolo,cerchio.")
if figura == "quadrato":
    l = float(input("inserire misura lato"))
    area = l*l
elif figura == "rettangolo":
    b = float(input("inserire misura base"))
    h = float(input("inserire misura altezza"))
    area = b*h
elif figura == "triangolo":
    b = float(input("inserire misura base"))
    h = float(input("inserire misura altezza"))
    area = b*h/2
elif figura == "cerchio":
    r = float(input("inserire misura raggio"))
    area = r*r*3.14

else:
    print("hai sbagliato a scrivere")
print("L'area del",figura,"é",area)
