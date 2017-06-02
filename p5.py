def is_div(n):
    for i in range(2,21,1):
        if n%i!=0:
            return False
    return True        

i=2520

while True:
    if is_div(i):
        break
    i=i+1    
print str(i)


    
