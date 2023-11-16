dati_pluviometrici=(("Milano",[("Gennaio",1.0),("Febbraio", "N/D"),("Marzo", 0)]), 
                    ("Roma",[("Gennaio",1.5),("Febbraio", 1.3),("Marzo", 0)]))

cittaUtente=input("inserisci la città di cui vuoi calcolare i dati: ")

def calcoloCitta (cittaUtente,dati_pluviometrici):
    max=-1
    min=10000000
    meseMax=[]
    meseMin=[]
    cont=0
    sommaValori=0
    for citta,*dati in dati_pluviometrici:
        if cittaUtente==citta:
            for giorno in dati:
                for dato in giorno:
                    if dato[1]!="N/D":
                        sommaValori+=dato[1]
                        cont+=1
                        if dato[1]>max:
                            max=dato[1]
                            meseMax.clear()
                            meseMax.append(dato[0])
                        elif dato[1]==max:
                            meseMax.append(dato[0])
                        if dato[1]<min:
                            min=dato[1]
                            meseMin.clear()
                            meseMin.append(dato[0])
                        elif dato[1]==min:
                            meseMin.append(dato[0])
    return(sommaValori/cont,(max,meseMax),(min,meseMin))

datiPluviometrici=calcoloCitta (cittaUtente,dati_pluviometrici)

if datiPluviometrici ==None:
    print("dati non corretti (la tupla è vuota)")
else:
    print("i dati della città",cittaUtente,"sono:","media= ",datiPluviometrici[0],"valore massimo:",datiPluviometrici[1][0],"corrisponde al mese:",datiPluviometrici[1][1],"valore minimo:",datiPluviometrici[2][0],"corrisponde al mese:",datiPluviometrici[2][1])


