aktywnosci={}

def dodaj_aktywnosc(nazwa,czas):
    if nazwa in aktywnosci.keys():
        aktywnosci[nazwa].append(czas)
    else:
        aktywnosci[nazwa]=[czas]

def pokaz_czas(nazwa):
    if nazwa not in aktywnosci.keys():
        return 0
    return sum(aktywnosci[nazwa])

def pokaz_top_aktywnosci():
    lista=[]
    for akt in aktywnosci.keys():
        lista.append((pokaz_czas(akt),akt))
        
    lista=sorted(lista)
    lista = lista[::-1]
    
    for i in range(3):
        if(i==len(lista)):
            break
        print(f'{i+1}. {lista[i][1]} | Czas: {lista[i][0]}\n')
  
        
print("KOMENDY")
print("Dodaj aktywnosc - wpisz DODAJ")
print("Pokaz czas danej aktywnosci - wpisz POKAZ CZAS")
print("Pokaz top 3 aktywnosci - wpisz POKAZ TOP 3")
print("Wyjdz - wpisz WYJDZ")

while(True):
    decyzja = input("Podaj akcje: ").upper()
    
    if decyzja=="DODAJ":
        nazwa = input("Podaj nazwe aktywnosci: ")
        czas = int(input("Podaj czas aktywnosci: "))
        dodaj_aktywnosc(nazwa,czas)
        print("Aktywnosc dodana!")
        
    elif decyzja=="POKAZ CZAS":
        nazwa = input("Podaj nazwe aktywnosci: ")
        print(f'Na aktywnosci {nazwa} spedzono {pokaz_czas(nazwa)} czasu')
        
    elif decyzja == "POKAZ TOP 3":
        pokaz_top_aktywnosci()
        
    elif decyzja == "WYJDZ":
        print("Zakonczono program")
        break
    
    else:
        print("Nieznana komenda!")
        
    print("\n")