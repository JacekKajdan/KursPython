def get_matches():
    from urllib.request import urlopen

    def porwownaj(s,k,id):
        return k==s[id:id+len(k)]

    url = "http://www.90minut.pl/liga/1/liga12904.html"
    page = urlopen(url)
    html = page.read().decode("iso-8859-2")
    #pre = "<td width=\"180\" valign=\"top\" nowrap=\"\">"
    pre="width=\"180\""
    kluby=["Cracovia", "Górnik", "Jagiellonia", "Korona", "Lech", "Legia", "Zagłębie","ŁKS", "Piast", "Pogoń", "Puszcza", "Radomiak", "Raków","Ruch", "Śląsk", "Stal", "Warta", "Widzew"]
    matches=[]
    for i in range (1,35):
        kolejka = "Kolejka " + str(i)
        start_index = html.find(kolejka)
        match=[]
        for j in range (18):
            #if((j==0 or j==1 or j==16 or j==17)and i==33):
             #   continue
            while(porwownaj(html,pre,start_index)==False):
                start_index+=1

            start_index+=len(pre)+3 #xD
            klub=""
            while(html[start_index]!=' '):
                klub+=html[start_index]
                start_index+=1
            if klub==">":
                continue
            if j%2==0:
                match=[]
                match.append(kluby.index(klub))
                #print(klub, end=' : ')
            else:
                match.append(kluby.index(klub))
                matches.append(match)
                #print(klub)
        #print("\n\n")
    #for i in matches:
        #print(i)
    return matches


