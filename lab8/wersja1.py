import math
import sys
import random
class Ułamek:
    
    # Wersja2 __slots__ = ('licznik','mianownik')
    
    def __init__(self, licznik, mianownik):
        assert mianownik !=0
        
        dziel = math.gcd(licznik,mianownik)
        licznik = int(licznik/dziel)
        mianownik = int(mianownik/dziel)
        
        if mianownik<0: 
            #1. Oba ujemne - usuwamy minusy
            #2. Mianownik ujemny, licznik nie - zamieniamy (liczba ujemna <=> licznik ujemny)
            mianownik*=-1
            licznik*=-1
        
        self.licznik = licznik
        self.mianownik = mianownik
    
    
    
    def __str__(self):
        return str(self.licznik) + "/" + str(self.mianownik)

    def __repr__(self):
        return str(self.licznik) + "/" + str(self.mianownik)
    
    
    def __add__(self, other):
        return Ułamek(self.licznik*other.mianownik+other.licznik*self.mianownik,self.mianownik*other.mianownik)
    
    def __sub__(self,other):
        return Ułamek(self.licznik*other.mianownik-other.licznik*self.mianownik,self.mianownik*other.mianownik)
    
    def __mul__(self,other):
        return Ułamek(self.licznik*other.licznik,self.mianownik*other.mianownik)
    
    def __truediv__(self,other):
        assert other.licznik != 0
        return Ułamek(self.licznik*other.mianownik,self.mianownik*other.licznik)
    
    
    def __eq__(self, other):
        return (self.licznik, self.mianownik)==(other.licznik,other.mianownik)


    def __ne__(self, other):
        return (self.licznik, self.mianownik)!=(other.licznik,other.mianownik)


    def __le__(self, other):
        return self.licznik*other.mianownik<=other.licznik*self.mianownik


    def __lt__(self, other):
        return self.licznik*other.mianownik<other.licznik*self.mianownik


    def __ge__(self, other):
        return self.licznik*other.mianownik>=other.licznik*self.mianownik


    def __gt__(self, other):
        return self.licznik*other.mianownik>other.licznik*self.mianownik
    
if(len(sys.argv)!=3):
    print("Zła liczba argumentów")
    exit(0)
n = int(sys.argv[1])
k = int(sys.argv[2])

tab = []
for i in range(n):
    u = Ułamek(random.randint(0,20),random.randint(1,20))
    tab.append(u)
    
for i in range(k):
    j = i%n
    tab[j]+=tab[(j+1)%n]


            