import math


i=11
while True:
    c=0
    for j in str(i):
        c=c+math.factorial(int(j))
    if c==i:
        print str(i)
    i=i+1        
