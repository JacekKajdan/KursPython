def get_table():
    tabela = [21,26,38,18,33,32,25,10,24,30,20,24,32,13,41,22,19,22] #dopisane
    return tabela
    from urllib.request import urlopen

    kluby=["Cracovia", "Górnik", "Jagiellonia", "Korona", "Lech", "Legia", "Zagłębie","ŁKS", "Piast", "Pogoń", "Puszcza", "Radomiak", "Raków","Ruch", "Śląsk", "Stal", "Warta", "Widzew"]
    tabela=[-1]*18
    url = "https://gol24.pl/ekstraklasa/tabela/"
    page = urlopen(url)
    html = page.read().decode("utf-8")
    id=52500
    for i in range (18):
        id = html.find("title=",id)
        nazwa=html[id+7:id+10]
        for j in range (18):
            if nazwa in kluby[j]:
                id = html.find("pkt",id)+5
                k=id
                while html[k]!='<':
                    k+=1
                #print(j, html[id:k])
                tabela[j]=(int(html[id:k]))
    
    return tabela
#print(get_table())