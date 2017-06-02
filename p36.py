from numpy import binary_repr
def is_palin(m):
    n=str(m)
    if n==n[::-1]:
        return True
#print binary_repr(585)
c=0
for i in range(1,1000000,1):
    if is_palin(i) and is_palin(binary_repr(i)):
            c=c+i
print str(c)            
