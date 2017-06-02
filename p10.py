import math
def is_prime(m):
    n=int(m)
    if n%2==0 or n%3==0:
        return False
    for i in range(5,int(math.sqrt(n))+1,6):
        if n%i==0 or n%(i+2)==0:
            return False    
    return True







inn=raw_input("> ")
fo=open(inn)
ele=[]

while True:
    data=fo.readline()
    if data=="":
        break
    ele=ele+data.split()
    #print ele
i=int(ele[-1])+1
while i<=2000000:
    if is_prime(i):
        ele.append(str(i))
    i=i+1    
c=0
  
#print ele
for i in ele:
    c=c+int(i)
print str(c)               
    
    
   
