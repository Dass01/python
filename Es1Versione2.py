prezzi_prodotti = (
    ("mela",("lunedi",1.0),("martedi",1.0),("mercoledi",1.3),("giovedi",1.0),("venerdi",2.0),("sabato",1.3)),
    ("banana",("lunedi",1.2),("martedi",1.1),("mercoledi",1.3),("giovedi",1.5),("venerdi",1.0),("sabato",1.7))
)

prodUtente=input("inserisci il prodotto di cui vuoi calcolare il prezzo medio: ")

def pMedioUtente (prodUtente):
    sommaPrezzo=0
    cont1=0

    for prodotto,* dati in prezzi_prodotti:
        if prodUtente==prodotto:
            for giorno,prezzo in dati:
                sommaPrezzo+=prezzo
                cont1+=1
            if cont1>0:
                return (sommaPrezzo/cont1)

def prezzoMedio ():
    sommaPrezzo=0
    cont2=0
    for prodotto,*dati in prezzi_prodotti:
        for giorno,prezzo in dati:
            sommaPrezzo+=prezzo
            cont2+=1
        if cont2>0:
            return(sommaPrezzo/cont2)

prodMaxUtente=input("inserisci il prodotto di cui vuoi visualizzare il prezzo massimo e i giorni: ")

def prezzoMax (prodMaxUtente):
    cont3=0
    for prodotto,* dati in prezzi_prodotti:
        if prodMaxUtente==prodotto:
            max=dati[1]
            giornoMax=dati[0]
            cont3+=1
            for giorno,prezzo in dati:
                if prezzo>max:
                    max=prezzo
                    giornoMax=giorno
            if cont3>0:
                return(max,giornoMax)
            



