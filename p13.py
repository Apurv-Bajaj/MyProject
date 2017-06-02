inn=raw_input("> ")
fp=open(inn)

c=0
ele=[]
ele=(fp.read()).split('\n')
print ele
for i in ele: 
    if i!='':       
        c=c+int(i)
            
print str(c)           
