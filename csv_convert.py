import sys
import re

path = sys.argv[1]
newpath = sys.argv[2]

with open(path, 'r') as f:
    text = f.readlines()
    f.close()

#prepare header
text[0] = re.sub("[^\w\s0-9]", "", text[0])

i=0
while i < len(text):
    text[i] = re.sub("\s+", ",", text[i].strip())
    i += 1

with open(newpath, 'x') as f:
    i = 0
    while i < len(text):
        f.write(text[i] + '\n')
        i += 1
    f.close()
