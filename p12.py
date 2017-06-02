import math
def gen_div(n):
    c=1
    for i in range(2,int(math.sqrt(n)),1):
        if n%i==0:
            c=c+1
    if math.sqrt(n)-int(math.sqrt(n))==0:
        return (c*2)+1        
    return (c*2)

a=1
i=2
#print str(gen_div(21232386))
while True:
   a=a+i
   if gen_div(a)>500:
     print str(a)
     break
   #print str(a)  
   i=i+1 
   
