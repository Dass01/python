#Esercizio 1 Versione 1

prezzi_prodotti = (("mela","lunedi",1.0), 
                   ("mela","martedi",1.2),
                   ("mela","mercoledi",1.1),
                   ("banana","lunedi",0.8),
                   ("banana","martedi",0.9),
                   ("banana","mercoledi",0.7))

giornoRic=input("inserisci il giorno della settimana in cui vuoi controllare il prezzo medio: ")
prodRic=input("inserisci il prodotto da cercare: ")



def prezzo_medio(prezzi_prodotti, giornoRic, prodRic):
    sommaCosto=0
    cont=0 
    for prodotto,giorno,costo in prezzi_prodotti:
        if giornoRic==giorno and prodRic==prodotto:
            sommaCosto+=costo
            cont+=1
        if cont>0:
            return (sommaCosto/cont)

if(prezzo_medio(prezzi_prodotti, giornoRic, prodRic)==None):
    print("dati inesistenti")
else:
    print("il prezzo medio è ",prezzo_medio(prezzi_prodotti, giornoRic, prodRic))