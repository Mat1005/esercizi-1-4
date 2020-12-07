Vocali= [ "a", "e", "i" ,"o" , "u" ]
Traduzioni = []
parole = []
while True:
    parola = input("Inserire la parola che si desidera tradurre. ")
    parole.append(parola)
    Testo = ""
    for lettera in parola:
        if lettera.lower() not in  Vocali:
            Testo = Testo + lettera + "o" + lettera
            
        else:
            Testo = Testo + (lettera) 
    Traduzioni.append(Testo)        
    controllo = int(input("Se si vuole tradurre un altra parola inserire 1 altrimenti inserire 0."))
    if controllo == 0:
        break

print ("Ecco le traduzioni delle parole",parole)
print(Traduzioni)


