#Dodalem dodatkowy katalog Year, zeby wszystkie katalogi z zadania byly w jednym miejscu
from pathlib import Path
import csv
import random
import os
solutions = [["Model","Output Value", "Time of computation"],[0,0,0]]

abc=["A","B","C"]

months = ['January','February','March','April','May','June','July','August','September','October','November','December']
week = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']


for month in months:
    for day in week:
        path = f'Year/{month}/{day}'
        sciezka = Path(path)
        sciezka.mkdir(511,True,True)
        with open(os.getcwd()+"/"+path+"/Soultions.csv", 'w', newline='') as file:
            writer = csv.writer(file)
            solutions[1][0]=abc[random.randint(0,2)]
            solutions[1][1]=random.randint(0,1000)
            solutions[1][2]=str(random.randint(0,1000))+"s"
            writer.writerows(solutions)
