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
    
    
for i in range(2,int(math.sqrt(600851475143))+1,1):
    if is_prime(i) and 600851475143%i==0:
        print i    
