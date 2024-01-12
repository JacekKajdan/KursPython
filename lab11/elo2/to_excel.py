def to_excel(first,second,third,forth,spadek,exp_points,rep):
    import xlsxwriter
    from decode2 import decode2
    workbook = xlsxwriter.Workbook('Esa.xlsx')
    worksheet = workbook.add_worksheet()
    bold = workbook.add_format({'bold': True})
    kluby=["Cracovia", "Górnik Zabrze", "Jagiellonia Białystok", "Korona Kielce", "Lech Poznań", "Legia Warszawa", "Zagłębie Lubin","ŁKS", "Piast Gliwice", "Pogoń Szczecin","Puszcza Niepołomice", "Radomiak Radom", "Raków Częstochowa","Ruch Chorzów", "Śląsk Wrocław", "Stal Mielec", "Warta Poznań", "Widzew Łódź"]
    tab=[]
    tab=decode2(kluby,exp_points)
    for i in range(18):
        worksheet.write(i+1,0,tab[i][0])
    tab=decode2(first,exp_points)
    for i in range(18):
        worksheet.write(i+1,1,tab[i][0]/rep)
    temp=first.copy()
    for i in range(18):
        temp[i]+=second[i]
        temp[i]+=third[i]
        temp[i]+=forth[i]
    tab=decode2(temp,exp_points)
    for i in range(18):
        worksheet.write(i+1,2,tab[i][0]/rep)
    tab=decode2(spadek,exp_points)
    for i in range(18):
        worksheet.write(i+1,3,tab[i][0]/rep)
    tab=decode2(exp_points,exp_points)
    for i in range(18):
        x=round(tab[i][0]/rep,1)
        worksheet.write(i+1,4,x,bold)
    worksheet.write(0,0,"Klub")
    worksheet.write(0,1,"Mistrzostwo")
    worksheet.write(0,2,"Puchary")
    worksheet.write(0,3,"Spadek")
    worksheet.write(0,4,"Exp Pts")
    percent_format = workbook.add_format({'num_format': '0.00%'})
    worksheet.set_column(0,0,17)
    worksheet.set_column(1,1,11,percent_format)
    worksheet.set_column(2,3,8,percent_format)
    worksheet.set_column(4,4,8)
    workbook.close()

