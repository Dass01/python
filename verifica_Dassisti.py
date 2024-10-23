class Articolo:
  def __init__(self, codice, fornitore, marca,prezzo, quantita):
    #1 Implementa il costruttore
    self.codice=codice
    self.fornitore=fornitore
    self.marca=marca
    self.prezzo=prezzo
    self.quantita=quantita

  def scheda_articolo(self):
    #2 Ritorna una stringa contenente gli attributi dell'articolo
    return f"Codice: {self.codice}\nFornitore: {self.fornitore}\nMarca: {self.marca}\nPrezzo: {self.prezzo}\nQuantita: {self.quantita}"

  def modifica_scheda(self):
    #3 Permette di modificare gli attributi dell'articolo
    print("MENU' MODIFICA:")
    print("1. Fornitore")
    print("2. Marca")
    print("3. Prezzo")
    print("4. Quantita")
    scelta=int(input("Inserisci cosa vuoi modificare:"))
    if scelta==1:
      self.fornitore=input("Inserisci nuovo fornitore: ")
    elif scelta==2:
      self.marca=input("Inserisci nuova marca: ")
    elif scelta==3:
      self.prezzo=float(input("Inserisci il nuovo prezzo: "))
    elif scelta==4:
      self.quantita=int(input("Inserisci nuova quantita: "))
    else:
      print("Scelta non valida!")

#ora: 9:27  INVERNIZZI




class Televisore(Articolo):
    def __init__(self, codice, fornitore,marca,prezzo,quantita,pollici,tipo):
      #4 Implementa il costruttore
      super().__init__(codice,fornitore,marca,prezzo,quantita)
      self.pollici=pollici
      self.tipo=tipo

    def scheda_articolo(self):
      #5 Ritorna una stringa contenente gli attributi del televisore
      return super().scheda_articolo()+f"\nPollici: {self.pollici}\nTipo: {self.tipo}"
    
#ora: 9:33 SPINARELLI




class Frigorifero(Articolo):
  def __init__(self, codice, fornitore, marca, prezzo, quantita,dimensioni,modello):
    #6 Implementa il costruttore
    super().__init__(codice,fornitore,marca,prezzo,quantita)
    self.dimensioni=dimensioni
    self.modello=modello

  def scheda_articolo(self):
    #7 Ritorna una stringa contenente gli attributi del frigorifero
    return super().scheda_articolo()+f"\nDimensioni: {self.dimensioni}\nModello: {self.modello}"


#ora: 9:36 INVERNIZZI

t1 = Televisore(1,"Fornitore 1","Sony",700,10,40,"Schermo piatto")
print(t1.scheda_articolo())
print()

t1.modifica_scheda()
print(t1.scheda_articolo())
print()

class Ordine():
  def __init__(self,codice,data, piva,indirizzo):
    #8 Implementa il costruttore
    self.codice=codice
    self.data=data
    self.piva=piva
    self.indirizzo=indirizzo
    self.lista_articoli=[]

  def aggiungi_articolo(self,articolo):
    if isinstance(articolo,Televisore):
      tipo_articolo="televisore"
      self.lista_articoli.append(articolo)
      print(f"{tipo_articolo} aggiunto all'ordine' {self.codice} del giorno {self.data}")

    elif isinstance(articolo,Frigorifero):
      tipo_articolo="frigorifero"
      self.lista_articoli.append(articolo)
      print(f"{tipo_articolo} aggiunto all'ordine' {self.codice} del giorno {self.data}")
    #9 Completa il metodo aggiungendo l'oggetto alla lista e stampando il messaggio opportuno

  def rimuovi_articolo(self,articolo):
    #10 Implementa il metodo
    if articolo in self.lista_articoli:
      if isinstance(articolo,Televisore):
        tipo_articolo="televisore"
        self.lista_articoli.remove(articolo)
        print(f"{tipo_articolo} rimosso alla vendita {self.codice} del giorno {self.data}")
      elif isinstance(articolo,Frigorifero):
        tipo_articolo="frigorifero"
        self.lista_articoli.remove(articolo)
        print(f"{tipo_articolo} rimosso alla vendita {self.codice} del giorno {self.data}")
    else:
      print("Articolo non trovato")


  def importo_ordine(self):
    #11 Stampa il numero di articoli e per ogni articolo l'importo (prezzo*quantita)
    nArticoli=len(self.lista_articoli)
    importo=0
    for i in range(nArticoli):
      importo+=self.lista_articoli[i].prezzo*self.lista_articoli[i].quantita
    return f"Il numero di articoli dell'ordine con codice {self.codice} è di {nArticoli} per un prezzo totale di {importo}"

  def dettaglio_ordine(self):
    #12 Stampa i dettagli dell'ordine e restituisce una lista contenente
    # [somma importi televisori, somma importi frigoriferi, somma importi totali ]
    #...
    nArticoli=len(self.lista_articoli)
    sommaT=0
    sommaF=0
    for i in range(nArticoli):
      if isinstance(self.lista_articoli[i],Televisore):
        sommaT+=self.lista_articoli[i].prezzo*self.lista_articoli[i].quantita
        print(self.lista_articoli[i].scheda_articolo())
        print()
      elif isinstance(self.lista_articoli[i],Frigorifero):
        sommaF+=self.lista_articoli[i].prezzo*self.lista_articoli[i].quantita
        print(self.lista_articoli[i].scheda_articolo())
        print()

    return([sommaT,sommaF,sommaT+sommaF])

#ora: 10:20 INVERNIZZI


t2 = Televisore(2,"Fornitore 2","Samsung",1000,5,80,"Schermo curvo")
f1 = Frigorifero(3,"Fornitore 3","Bosch",750,12,'790x2000x600','Ultra')
f2 = Frigorifero(4,"Fornitore 4","Ariston",550,10,'590x1600x500','Medium')

ordine1=Ordine(1,"24/02/2022",'213143','Via della consegna 1')
ordine1.aggiungi_articolo(t1)
ordine1.aggiungi_articolo(t2)
ordine1.aggiungi_articolo(f1)
ordine1.aggiungi_articolo(f2)
print()

ordine1.rimuovi_articolo(f2)
ordine1.rimuovi_articolo(f2)
print()

#13 Risposta al Punto 1 : Per un ordine: il numero di articoli presenti e
# l'importo totale senza distinguere il tipo di articolo
print(ordine1.importo_ordine())
print()

#14 Risposta punto 2.   Per un ordine: il dettaglio degli articoli, l'importo totale,
# l'importo dei televisori e l'importo dei frigoriferi.
importi=ordine1.dettaglio_ordine()
print("--------------------------")
print(f"\nImporto televisori= {importi[0]}")
print(f"\nImporto frigoriferi= {importi[1]}")
print(f"\nImporto totale= {importi[2]}")
print()


class Ordini():
  def __init__(self,nome_negozio,codice_negozio):
    #16 Implementa il costruttore
    self.nome_negozio=nome_negozio
    self.codice_negozio=codice_negozio
    self.lista_ordini=[]

  def aggiungi_ordine(self,ordine):
    #17 Implementa il metodo
    if ordine in self.lista_ordini:
        print(f"Ordine {ordine.codice} già presente")
    else:
        self.lista_ordini.append(ordine)
        print(f"Ordine {ordine.codice} aggiunto alla lista degli ordini")
      

  def rimuovi_ordine(self,ordine):
    #18 Implementa il metodo
    if ordine in self.lista_ordini:
      self.lista_ordini.remove(ordine)
      print(f"Ordine {ordine.codice} rimosso dalla lista degli ordini")
    else:
      print(f"Ordine {ordine.codice} non presente")

  def totale_ordini(self):
    #19 Implementa il metodo
    #...

    totT=0
    totF=0
    tot=0
    for i in range(len(self.lista_ordini)):
      importi=self.lista_ordini[i].dettaglio_ordine()
      totT+=importi[0]
      totF+=importi[1]
      tot+=importi[2]
    return ([totT,totF,tot])

#ora: 10:51 SPINARELLI


ordini_negozio=Ordini("Megastore vendita ",1)
ordini_negozio.aggiungi_ordine(ordine1)
ordini_negozio.rimuovi_ordine(ordine1)
ordini_negozio.rimuovi_ordine(ordine1)
print()


ordini_negozio.aggiungi_ordine(ordine1)
print()


t3 = Televisore(5,"Fornitore 5","LG",600,4,70,"Schermo curvo")
f3 = Frigorifero(6,"Fornitore 6","Bosch",450,10,'490x1000x400','Small')
ordine2=Ordine(2,"25/02/2022",'213113','Via della consegna 2')
ordine2.aggiungi_articolo(t3)
ordine2.aggiungi_articolo(f3)
print()


ordini_negozio.aggiungi_ordine(ordine2)
print()

# 20 Riposta punto 3: Per tutti gli ordini del negozio mostra
# il dettaglio degli articoli, l'importo totale,
# l'importo dei televisori e l'importo dei frigoriferi.
importiTotali=ordini_negozio.totale_ordini()
print("--------------------------")
print(f"\nImporto totale televisori= {importiTotali[0]}")
print(f"\nImporto totale frigoriferi= {importiTotali[1]}")
print(f"\nImporto totale tutti gli ordini= {importiTotali[2]}")