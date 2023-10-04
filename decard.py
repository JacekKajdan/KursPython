import random as rd
all = 10000000
sum=0
for i in range(all):
    x=rd.uniform(-1,1)
    y=rd.uniform(-1,1)
    if(x*x+y*y<=1):
        sum+=1
print(sum/all*4)