import sys


skroty = ['pn','wt','sr','cz','pt','so','nd']
nazwy_dni = ['poniedzialek','wtorek','sroda','czwartek','piatek','sobota','niedziela']
counter=0

miesiace=[]
dni=[]
pory_dnia=[]

def pora():
    global counter
    if counter>=len(pory_dnia):
        return 'rano'
    
    if pory_dnia[counter]=='r':
        return 'rano'
    else:
        return 'wieczor'

def wypisz(miesiac, dzien):
    global counter
    miesiac[:1].upper()
    
    
    start_dzien = dzien[:2]
    koniec_dzien = dzien[len(dzien)-2:len(dzien)]
    id_start = skroty.index(start_dzien)
    id_koniec = skroty.index(koniec_dzien)
    while id_start<=id_koniec:
        
        
        print(f'{miesiac} {nazwy_dni[id_start]} {pora()}')
        id_start+=1
        counter+=1
        
        



i = 1
while sys.argv[i] not in skroty:
    miesiace.append(sys.argv[i])
    i+=1
for j in range(len(miesiace)):
    dni.append(sys.argv[i+j])
i+=len(dni)
while i<len(sys.argv):
    pory_dnia.append(sys.argv[i])
    i+=1

for j in range(len(miesiace)):
    wypisz(miesiace[j],dni[j])#https://www.geoguessr.com/pl/game/DAcUFlmfnBU7CTYz