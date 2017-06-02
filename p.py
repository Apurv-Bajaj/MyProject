from collections import deque
import bisect
n=raw_input("> ")
d=deque(n)
for i in range(0,len(n)-1,1):
    print ''.join(map(d.rotate(-1),d))
ele=['2','3','5','7','11','13']
def index(x):
    'Locate the leftmost value exactly equal to x'
    i = bisect.bisect_left(ele, x)
    if i != len(ele) and ele[i] == x:
        return i
    return -1    
print str(index('12'))       
