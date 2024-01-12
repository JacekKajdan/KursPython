def sortuj(tabela):
    kluby=["Cracovia", "Górnik Zabrze", "Jagiellonia Białystok", "Korona Kielce", "Lech Poznań", "Lechia Gdańsk", "Legia Warszawa", "Zagłębie Lubin", "Miedź Legnica", "Piast Gliwice", "Wisła Płock", "Pogoń Szczecin", "Radomiak Radom", "Raków Częstochowa", "Śląsk Wrocław", "Stal Mielec", "Warta Poznań", "Widzew Łódź"]
    koncowa=[]
    for i in range(18):
        koncowa.append([i,tabela[i]])
    koncowa.sort(key=lambda x: x[1], reverse=True)
    import random
    for i in range (17):
        if(koncowa[i][1]==koncowa[i+1][1] and random.uniform(0,1)<0.5):
            temp = koncowa[i]
            koncowa[i]=koncowa[i+1]
            koncowa[i+1]=temp
    return koncowa
