import math
def is_prime(n):
 if n==2 or n==3:
    return True
 else:   
    if n%2==0 or n%3==0:
        return False
    for i in range(5,int(math.sqrt(n))+1,6):
        if n%i==0 or n%(i+2)==0:
            return False
    
    return True            
    
i=104730
while True:
    print i
    if is_prime(i):
        print str(i)
        break
    i=i+1         


    
