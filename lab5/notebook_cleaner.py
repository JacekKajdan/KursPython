import sys
import json
from functools import reduce

def del_code_output(dc):
    dc = dict(dc)
    if('outputs' in dc.keys()):
        dc['outputs'].clear()
    return dc

def del_code_after_cwiczenie(x,y):
    x=list(x)
    if len(x)>0 and "# Ćwiczenie" in str(x[len(x)-1]) and y['cell_type']=='code':
        y['source'].clear()
        x.append(y)
    else:
        x.append(y)
    return x
        

if(len(sys.argv)==1):
    print("Podaj nazwe pliku")
    sys.exit(0)
    
file_path = sys.argv[1]

with open(file_path, 'r') as file_in:
    
    dc = json.load(file_in)
    
    dc['cells'] = list(map(del_code_output,dc['cells']))
    
    dc['cells'] = reduce(del_code_after_cwiczenie,dc['cells'],[])
    
    with open(file_path[:len(file_path)-6] + "_clear.ipynb", 'w') as file_out:
        json.dump(dc, file_out)
    
