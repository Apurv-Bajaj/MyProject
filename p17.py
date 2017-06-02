import num2word
import re
#print num2word.to_card(15)
ele=[]
for i in range(1,1001,1):
    word=num2word.to_card(i)
    ele=ele+re.split('[-| ]',word)

print ele
c=0    
for i in ele:
    print i
    c=c+len(i)
print str(c)                     
