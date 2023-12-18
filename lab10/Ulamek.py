import math
import pytest
from unittest.mock import mock_open, MagicMock
class Ułamek:
    def __init__(self, licznik, mianownik):
        assert mianownik != 0

        self.licznik,self.mianownik = self.skróć(licznik,mianownik)
    
    def skróć(self,licznik,mianownik):
        dziel = math.gcd(licznik, mianownik)
        licznik = int(licznik / dziel)
        mianownik = int(mianownik / dziel)

        if mianownik < 0:
            # 1. Oba ujemne - usuwamy minusy
            # 2. Mianownik ujemny, licznik nie - zamieniamy (liczba ujemna <=> licznik ujemny)
            mianownik *= -1
            licznik *= -1
        return licznik, mianownik


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
    
    def zapisz(self,nazwa):
        with open(nazwa,'w') as plik:
            plik.write(f'{self.licznik}\n{self.mianownik}')

    def odczytaj(self, nazwa):
        with open(nazwa, 'r') as plik:
            l = plik.readline()
            m = plik.readline()
            self.licznik,self.mianownik = self.skróć(int(l), int(m))

    
@pytest.fixture
def simple_fractions():
    return Ułamek(2,4),Ułamek(1,-3)  ,Ułamek(0,3)


    

@pytest.mark.parametrize("a, b, c", [[Ułamek(1,2), Ułamek(2,4), Ułamek(3,3)],[Ułamek(1,-2), Ułamek(2,10), Ułamek(-3,10)]])
def test_dodawanie(a, b, c):
    assert a+b==c


def test_read_file(simple_fractions):
    mock_data = "-1\n2"
    m = mock_open(read_data=mock_data)

    with pytest.raises(FileNotFoundError):
        simple_fractions[0].odczytaj("brak_ulamka.txt")

    with pytest.MonkeyPatch.context() as mpatch:
        mpatch.setattr("builtins.open", m)
        u1 = Ułamek(0,1)
        u1.odczytaj("123.txt")

    m.assert_called_once_with("123.txt", 'r')

    assert u1 == Ułamek(1,-2)

def test_write_file(simple_fractions):
    simple_fractions[1].zapisz("moj_ulamek.txt")
    expected = f'{simple_fractions[1].licznik}\n{simple_fractions[1].mianownik}'
    with open("moj_ulamek.txt",'r') as plik:
        s=plik.read()
        assert s==expected

def test_dzialania(simple_fractions):
    u1=simple_fractions[0]
    u2=simple_fractions[1]
    u3=simple_fractions[2]
    assert u1 + u2 == Ułamek(1, 6)
    assert u1 - u2 == Ułamek(5, 6)
    assert u1 * u2 == Ułamek(-1, 6)
    assert u1 / u2 == Ułamek(-3, 2)
    assert u2 - u1 == Ułamek(-5, 6)
    assert u2 / u1 == Ułamek(-2, 3)

    assert (u1 == u2) == False
    assert (u1 != u2) == True
    assert (u1 <= u2) == False
    assert (u1 < u2) == False
    assert (u1 >= u2) == True
    assert (u1 > u2) == True

    assert (u1 == u1) == True
    assert (u1 != u1) == False
    assert (u1 <= u1) == True
    assert (u1 < u1) == False
    assert (u1 >= u1) == True
    assert (u1 > u1) == False

    assert u1+u3 == u1
    assert u1-u3 == u1
    assert u1*u3 == u3

    with pytest.raises(AssertionError):
        u1/u3
