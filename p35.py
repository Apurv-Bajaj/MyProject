from collections import deque
import bisect
ele=[]
def palin(n):
    return n[::-1]

def binary_search(item_list,item):
	first = 0
	last = len(item_list)-1
	found = False
	while( first<=last and not found):
		mid = (first + last)//2
		if item_list[mid] == item :
			found = True
		else:
			if item < item_list[mid]:
				last = mid - 1
			else:
				first = mid + 1	
	return found
        
def is_cir_prime(n):
    if len(n)==1:
        #print n+" "+str(len(n))+"#####"
        return True
    elif len(n)==2:  
        #print n+" "+str(len(n)) 
        dt=palin(n)
        return binary_search(int_list,int(dt))
    else:
        d=deque(n)
        for i in range(0,len(n)-1,1):
            s=''.join(map(d.rotate(-1),d))
            if binary_search(int_list,int(s))==False:
               return False              
        return True

n=raw_input("> ")
data=" "
fp=open(n)
while data!="":
    data=fp.readline()
    ele=ele+data.split(',')
c=0    
int_list=[]
for i in ele:
    if i!='\n' and i!='':
        int_list.append(int(i))
for i in int_list:
    if is_cir_prime(str(i)):
     print str(i)
     c=c+1
print str(c)             
#print int_list        
#print ele         
