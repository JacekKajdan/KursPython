def league_simulation(mecze,tabelap,tabela_elo):
    from sortuj import sortuj
    from simulate_match import simulate
    from temp import elo
    #print(tabela)
    for mecz in mecze:
        szanse = elo(tabela_elo[mecz[0]],tabela_elo[mecz[1]])
        wynik = simulate(szanse[0],szanse[1])
        if(wynik==1):
            tabelap[mecz[0]]+=3
            delta = (1-szanse[2])*20
            tabela_elo[mecz[0]]+=delta
            tabela_elo[mecz[1]]-=delta
        elif(wynik==2):
            tabelap[mecz[1]]+=3
            delta = (-szanse[2])*20
            tabela_elo[mecz[0]]+=delta
            tabela_elo[mecz[1]]-=delta
        else:
            tabelap[mecz[0]]+=1
            tabelap[mecz[1]]+=1
            delta = (0.5-szanse[2])*20
            tabela_elo[mecz[0]]+=delta
            tabela_elo[mecz[1]]-=delta
    koncowa = sortuj(tabelap)
    return koncowa
    #for poz in koncowa:
        #print(poz[0],poz[1])
