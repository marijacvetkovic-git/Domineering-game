import copy

def main():   
    iks=True
    (vrste, kolone)=unesiBrojVrstaIKolona()
    matrica=kreirajMatricu(vrste, kolone)
    prviIgrac=izaberiKoIgraPrvi()
    prikaziTrenutnoStanje(matrica, kolone, vrste)
    while True:
        # kada prvi igra covek
        if prviIgrac:
            if iks:
                unesiPotez(vrste,kolone,matrica,iks)
            else:
                igraPotez=vrati_potez_racunara(matrica, vrste, kolone,iks)
                igraPotez1=(int(igraPotez[0][0][0]), igraPotez[0][0][1])
                igraPotez2=(int(igraPotez[0][1][0]), igraPotez[0][1][1])
                upisiPotez(iks, matrica, igraPotez1, igraPotez2)
            prikaziTrenutnoStanje(matrica, kolone, vrste)
            if proveriDaLiJeKraj(iks, vrste, kolone, matrica):
                break
            iks = not iks
            # kada prvi igra racunar
        else:
            if iks:
                igraPotez=vrati_potez_racunara(matrica, vrste, kolone,iks)
                igraPotez1=(int(igraPotez[0][0][0]), igraPotez[0][0][1])
                igraPotez2=(int(igraPotez[0][1][0]), igraPotez[0][1][1])
                upisiPotez(iks, matrica, igraPotez1, igraPotez2)
            else:
                unesiPotez(vrste,kolone,matrica,iks)
            prikaziTrenutnoStanje(matrica, kolone, vrste)
            if proveriDaLiJeKraj(iks, vrste, kolone, matrica):
                break
            iks = not iks     
         
    if iks==True:
        print("Dosli ste do kraja igre,pobednik je:oks")
    else:
        print("Dosli ste do kraja igre,pobednik je:iks")

def izaberiKoIgraPrvi():  
  prviIgra = input("Unesite ko igra prvi, covek ili racunar? ")
  if prviIgra=='covek':
      return True
  elif prviIgra=='racunar':
      return False
  else:
      print("Niste lepo uneli prvog igraca,molim vas unesite opet <3")
      return izaberiKoIgraPrvi()
  
def unesiBrojVrstaIKolona():
    vrste1 = input("Unesi m vrsta: ")
    
    if not vrste1 :
        print("Los potez, unesite ispravan")
        (vrste,kolone)= unesiBrojVrstaIKolona()
        return (vrste,kolone)
    vrste=int(vrste1)
    if(vrste > 9):
        vrste=9
        print("Nevalidan broj vrsta, postavljeno na max mogucu vrednost")
  
    elif(vrste<4):
        vrste=4
        print("Nevalidan broj vrsta, postavljeno na min mogucu vrednost")
     
    kolone1 = input("Unesi n kolona: ")
    if not kolone1 :
        print("Los potez, unesite ispravan")
        (vrste,kolone)= unesiBrojVrstaIKolona()
        return (vrste,kolone)
    kolone = int(kolone1)
    if(kolone>9):
        kolone=9
        print("Nevalidan broj kolona, postavljeno na max mogucu vrednost")
    elif(kolone<4):
        kolone=4
        print("Nevalidan broj kolona, postavljeno na min mogucu vrednost")
        

    return (vrste, kolone)

def kreirajMatricu(vrste, kolone):
    tablicaStanja= dict()
   
    for r in range(vrste):
      slovo= 97
      for c in range(kolone):
            kljuc= "%d%s" % (r+1,chr(slovo))
            slovo+=1
            tablicaStanja[kljuc]= " "
    return tablicaStanja        

def prikaziTrenutnoStanje(tablica,kolone,vrste):
    slovce= 65
    lista=[]   
    for i in range(vrste):
        slovo=97
        stringic=''
        for j in range(kolone):
            key='%d%s' % (vrste-i,chr(slovo))
            slovo+=1
            if tablica[key]=='X':
                stringic+='X|'
            elif tablica[key]=='O':
                stringic+='O|'
            else :
                stringic+=' |'
        dodatak= str(vrste-i)+ "ǁ" + stringic + "ǁ" + str(vrste-i)
        # dodatak= za printanje cele vrste
        lista.append(dodatak)
                
    jednako="= "
    vrstaJed=jednako*kolone
    jed="  "+ vrstaJed+ "  " 
    prikazKolona="  "
    minus=" -"
    minusVrsta=" "+ minus*kolone+ "  "
    for m in range(kolone):
        prikazKolona+= chr(slovce)+" "
        slovce+=1
    prikazKolona+="  "
    print(prikazKolona)
    print(jed)
    brojac=0
    for i in range(vrste*2-1):
        if i%2==0:
            print( lista[brojac])
            brojac+=1
        else:
            print(minusVrsta)    
    print(jed) 
    print(prikazKolona)
    print("////////////////////////////////////////////////////////////////////////////")

def pronadjiDruguPozicijuPoteza(iks,vrsta,kolona):
    if iks==True:
      pozicija2= (vrsta+1, kolona) 
    else:
      pozicija2= (vrsta, chr(ord(kolona)+1))  
    return pozicija2

def proveriPotez(pozicija1,pozicija2,vrste, kolone, tablica):
  if pozicija1[0]>vrste or pozicija1[0]<1 or ord(pozicija1[1])<97 or ord(pozicija1[1])>96+kolone:
    print ("Uneta pozicija je van opsega tabele!")
    return False
  elif pozicija2[0]>vrste or pozicija2[0]<1 or ord(pozicija2[1])<97 or ord(pozicija2[1])>96+kolone:
    print ("Plocica viri van table!")
    return False
  elif tablica["%d%s" % (pozicija1[0],pozicija1[1])] !=' ' or tablica["%d%s" % (pozicija2[0],pozicija2[1])] !=' ':
    print("Polje je zauzeto!")
    return False
  else:
    return True

def unesiPotez(vrste, kolone, tablica, iks):
    x1= input("Unesite vrstu: ")
    y= input ("Unesite kolonu: ")
    if len(x1)>1 or len(y)>1 or not y or not x1:
        print("Los potez, unesite ispravan")
        unesiPotez(vrste, kolone, tablica, iks)
        return
    x=int(x1);   
    pozicija2=pronadjiDruguPozicijuPoteza(iks,x,y)
    pozicija1=(x,y)
    if proveriPotez(pozicija1,pozicija2,vrste,kolone,tablica)==False:
        print("Los potez, unesite ispravan")
        unesiPotez(vrste,kolone,tablica,iks)   
    else:upisiPotez(iks,tablica,pozicija1,pozicija2) 
 
def proveriDaLiJeKraj(iks,vrste,kolone, tablica):
    brXPoteza=len(formirajMogucaStanja(True,vrste, kolone,tablica))
    brOPoteza=len(formirajMogucaStanja(False,vrste, kolone,tablica))
    if(brXPoteza == 0):
        return -10
    elif brOPoteza == 0:
        return 10
    else:
        return 0
        
def upisiPotez(iks,tablica,pozicija1,pozicija2):
    kljuc1= "%d%s" % (pozicija1[0],chr(ord((pozicija1[1]))))
    kljuc2= "%d%s" % (pozicija2[0],chr(ord((pozicija2[1]))))
    if(iks==True):
        tablica[kljuc1]="X"
        tablica[kljuc2]="X"
    elif iks==False:
        tablica[kljuc1]="O"
        tablica[kljuc2]="O" 
    else:
        tablica[kljuc1]=" "
        tablica[kljuc2]=" "   
    return tablica   

def upisiPotezMinmax(iks,tablica,pozicija1,pozicija2):
    RezTabla=copy.deepcopy(tablica)
    kljuc1= "%d%s" % (pozicija1[0],chr(ord((pozicija1[1]))))
    kljuc2= "%d%s" % (pozicija2[0],chr(ord((pozicija2[1]))))
    if(iks==True):
        RezTabla[kljuc1]="X"
        RezTabla[kljuc2]="X"
    elif iks==False:
        RezTabla[kljuc1]="O"
        RezTabla[kljuc2]="O" 
    else:
        RezTabla[kljuc1]=" "
        RezTabla[kljuc2]=" "   
    return RezTabla   

def formirajMogucaStanja(iks,vrste,kolone, tablica):
    mogucaStanja= list()
    if iks==True:
        for i in tablica:
            if int(i[0])!=vrste:
                key= "%d%s" % (int(i[0])+1,i[1])
                if i[1]==key[1]:
                    if tablica[i]==" " and tablica[key]==" ":
                        mogucaStanja.append((i,key))

    else:
        for i in tablica:
            if (ord(i[1]))!=kolone+96 :
                key= "%d%s" % (int(i[0]),chr(ord(i[1])+1))
                if i[0]==key[0]:
                    if tablica[i]==" " and tablica[key]==" ":
                        mogucaStanja.append((i,key)) 
    return mogucaStanja

def minimax_alpha_beta(tablica, vrste, kolone,dubina, iks, alpha=((None, None), -10), beta=((None, None), 10)):
    if iks:
        return max_value(tablica,vrste, kolone, dubina, alpha, beta)
    else:
        return min_value(tablica,vrste, kolone, dubina, alpha, beta)

def max_value(tablica,vrste, kolone, dubina, alpha, beta, potez=None):
    if proveriDaLiJeKraj(True, vrste, kolone, tablica) ==- 10:
        return(potez, -10)
    listaPoteza=formirajMogucaStanja(True , vrste, kolone, tablica)
    if listaPoteza is None or dubina==0 or len(listaPoteza)==0:
        return (potez, heuristika(tablica, vrste, kolone))
    else:
        for p in listaPoteza:
            p1=(int(p[0][0]), p[0][1])
            p2=(int(p[1][0]), p[1][1])
            alpha=max(alpha, min_value(upisiPotezMinmax(True, tablica, p1, p2), vrste, kolone, dubina - 1, alpha, beta, p if potez is None else potez), key=lambda x: x[1])
        if alpha[1] >= beta[1]: 
                return beta
    return alpha

def min_value(tablica, vrste, kolone,dubina, alpha, beta, potez=None):
    if proveriDaLiJeKraj(False, vrste, kolone, tablica) == 10:
        return(potez, 10)
    listaPoteza=formirajMogucaStanja(False, vrste,kolone, tablica)
    if listaPoteza is None or dubina==0 or len(listaPoteza)==0:
        return (potez, heuristika(tablica, vrste,kolone))
    else:
        for p in listaPoteza:
            p1=(int(p[0][0]), p[0][1])
            p2=(int(p[1][0]), p[1][1])
            beta=min(beta, max_value(upisiPotezMinmax(False, tablica,p1, p2), vrste, kolone, dubina - 1, alpha, beta, p if potez is None else potez), key=lambda x: x[1])
        
        if beta[1] <= alpha[1]:
            return alpha
    return beta

def heuristika(tablica, vrste, kolone):
        pomTabla=copy.deepcopy(tablica)
        brXPoteza=len(formirajMogucaStanja(True,vrste, kolone,pomTabla))
        brOPoteza=len(formirajMogucaStanja(False,vrste, kolone,pomTabla))
        return brXPoteza - brOPoteza

def vrati_potez_racunara(tabla, vrste, kolone, iks):
        tablica= copy.deepcopy(tabla)
        rezultat = minimax_alpha_beta(tablica,vrste, kolone, 2, iks, alpha=((None,None), -10), beta=((None,None), 10))
        if(rezultat[0][0] == None):
            rezultat = minimax_alpha_beta(tablica,vrste, kolone, 1, iks, alpha=((None,None), -10), beta=((None,None), 10))
       
        return rezultat
 
 
 
def covekCovek():
    iks=True
    (vrste, kolone)=unesiBrojVrstaIKolona()
    matrica=kreirajMatricu(vrste, kolone)
    prikaziTrenutnoStanje(matrica, kolone, vrste)

    while True:
        print("Na redu je igrac X, unesite potez:")
        unesiPotez(vrste,kolone,matrica, iks)
     
        prikaziTrenutnoStanje(matrica, kolone, vrste)
        if proveriKraj(iks, vrste, kolone, matrica):
                print("Pobednik je X")
                return 
        iks= not iks 
        print("Na redu je igrac O, unesite potez: ")
        unesiPotez(vrste,kolone,matrica, iks)
        prikaziTrenutnoStanje(matrica, kolone, vrste)
        if proveriKraj(iks, vrste, kolone, matrica):
                print("Pobednik je O")
                return
        iks= not iks 

def proveriKraj(iks,vrste,kolone,tablica):
    if len(formirajMogucaStanja(not iks, vrste,kolone,tablica))==0:
        return True
    else:
        return False   
# main()
covekCovek()


