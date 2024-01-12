from league_simulation import league_simulation
from elo_scrap import get_elo_table
from matches import get_matches
from table import get_table
from to_excel import to_excel

tabela_pkt_org = get_table()
tabela_pkt=tabela_pkt_org.copy()
tabela_elo_org = get_elo_table()
tabela_elo=tabela_elo_org.copy()
mecze = get_matches()
first=[0]*18
second=[0]*18
third=[0]*18
forth=[0]*18
spadek=[0]*18
exp_points=[0]*18
rep=10000
for i in range(rep):
    tabela = league_simulation(mecze,tabela_pkt,tabela_elo)
    for i in range(18):
        exp_points[i]+=tabela_pkt[i]
    tabela_pkt=tabela_pkt_org.copy()
    tabela_elo=tabela_elo_org.copy()
    #print(tabela)
    first[tabela[0][0]]+=1
    second[tabela[1][0]]+=1
    third[tabela[2][0]]+=1
    forth[tabela[3][0]]+=1
    spadek[tabela[15][0]]+=1
    spadek[tabela[16][0]]+=1
    spadek[tabela[17][0]]+=1
"""
print("Mistrzostwo")
decod(first,rep,True)
print("\n")
print("Wicemistrzostwo")
decod(second,rep,True)
print("\n")
print("3 miejsce")
decod(third,rep,True)
print("\n")
print("4 miejsce")
decod(forth,rep,True)
print("\n")
print("Spadek")
decod(spadek,rep,True)
print("\n")
print("Expected points")
decod(exp_points,rep,False)
print("\n")
"""
to_excel(first,second,third,forth,spadek,exp_points,rep)