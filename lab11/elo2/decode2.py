def decode2(sortowane,sortuj_po):
    wynik=[]
    for i in range(18):
        wynik.append([sortowane[i],sortuj_po[i]])
    wynik.sort(key=lambda x: x[1], reverse=True)
    return wynik
