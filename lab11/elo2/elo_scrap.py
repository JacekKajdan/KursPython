from webbrowser import get


def get_elo_table():
    from urllib.request import urlopen
    url = "http://clubelo.com/POL"
    page = urlopen(url)
    html = page.read().decode("utf-8")
    kluby=["Cracovia", "Gornik", "Jagiellonia", "Korona", "Lech", "Legia", "Lubin","LKS", "PiastGliwice", "Pogon","PuszczaNiepolomice", "Radomiak", "Rakow", "Ruch", "Slask", "StalMielec", "Warta", "Widzew"]
    tabela=[]

    for klub in kluby:
        start_index = html.find(klub) #+ len(klub) + len(klub) + 25
        while html[start_index]!='1':
            start_index+=1
        end_index = start_index+4
        elo = html[start_index:end_index]
        #print(klub,elo)
        tabela.append(int(elo))
    #for i in range(18):
        #print(i,tabela[i])
    return tabela
