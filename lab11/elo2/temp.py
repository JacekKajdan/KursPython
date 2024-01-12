def elo(a,b):
    plock = a
    lodz = b
    hfa = 44.7
    dr=plock-lodz + hfa
    E = 1 / (pow(10,-dr/400) + 1)
    p1 = pow(E*E,1) #0.82   64
    draw= 1.8*(E-p1) #1.8   3.12
    p2=1-p1-draw
    #p2 = (1-E)*(1-E)
    #draw = 1-p1-p2
    #print((1-E)*20)
    #print((0.5-E)*20)
    #print((0-E)*20)
    return [p1,draw,1-p1-draw]
#print(elo(1435,1286))
