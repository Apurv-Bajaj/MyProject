def is_palindrome(n):
    if n == n[: :-1]:
        return True

elements=[]        
t=0
for i in range(999,100,-1):
    for j in range(999,100,-1):
        if is_palindrome(str(i*j)):
                #print str(i*j)
                elements.append(i*j)
                t=t+1     
elements.sort()
print elements                                              
