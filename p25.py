def count(n):
    return len(str(n))
a=1
b=1
i=2
c=0
while count(c)!=1000:    
    c=a+b
    a=b
    b=c
    i=i+1
print str(i)    
