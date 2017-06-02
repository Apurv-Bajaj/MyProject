s=2
a=1
b=2
c=0
while c<4000001:
   c=a+b
   if c%2==0 and c<4000001:
        s+=c  
   a=b
   b=c
print c
print s    
