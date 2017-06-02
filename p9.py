#project euler problem 9
def py_try(*num):
    a,b,c=num
    print "%d %d %d"%(a,b,c)
    if a<b<c and (a*a)+(b*b)==(c*c):
        return True
        
        
while True:
    for c in range(1,1000,1):
        for b in range(1,c,1):
            for a in range(1,b,1):
              if a+b+c==1000 and py_try(a,b,c):
                      print str(a*b*c)
                      exit(0)
    
