import sys
import os 
import matplotlib.pyplot as plt
import pandas as pd

def check_args(path:str, delimiter:str, x:str, y:str, *args):
    
    _delimiters = [',', ' ']
    _exists = os.path.exists(path)
    _valid = [d for d in _delimiters if d == delimiter.lower()]
    
    if not len(args) < 4:
        ERRMSG = 'The path, delimiter, x axis name and y axis name must be '\
               + 'passed as flags on program call.'
        raise UnboundLocalError(ERRMSG)
    elif not _exists:
        raise OSError(f'The data file {path} does not exist')
    elif not _valid:
        raise ValueError(f'The chosen delimiter {delimiter} is not supported')

    return

def find_cols(cols:list, data:pd.DataFrame) -> dict:
    
    name_map = dict()
    
    for col in cols:
        if not isinstance(col, str):
            print(f'{col} is not string...skipping')
            continue
        for c in data.columns:
            if c.lower() == col.lower():
                name_map[col] = c
            else:
                continue
    
    return name_map
         
def gen_title(path:str, axis_1:str, axis_2:str) -> str:

    file = os.path.basename(path)
    name = file.split('.')[0]
    header = name + '_' + axis_1 + '_v_' + axis_2

    return header
check_args(*sys.argv[1:])

path = sys.argv[1]
delimiter = sys.argv[2]
x_name = sys.argv[3]
y_name = sys.argv[4]

data = pd.read_csv(path, sep=",")
_cols = [col.lower() for col in data.columns]

if x_name.lower() not in _cols:
    raise ValueError(f'The data corresponding to {x_name} was not found')
elif y_name.lower() not in _cols:
    raise ValueError(f'The data corresponding to {y_name} was not found')

names = find_cols([x_name, y_name], data)
title = gen_title(path, x_name, y_name)

print(len(data[names[x_name]]))
print(len(data[names[y_name]]))
print(data[names[y_name]][49])
plt.plot(names[x_name], names[y_name], data=data)
plt.savefig('output/' + 'graphs/' + title + '.png')
plt.close()
