a='one-four-four-nine-nine'
c=a.split('-')
tup={'one':1,'four':4,'nine':9}
le=len(c)
d=''
for i in range(0,le):
    c[i]=tup[c[i]]
    d=d.__add__(str(c[i]))    
print(d)
