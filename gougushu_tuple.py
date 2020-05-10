def gougushu(max):
    for a in range(1,100,1):
        for b in range(1,100,1):
            for c in range(1,100,1):
                if a**2+b**2==c**2:
                    yield (a,b,c)
se=set(gougushu(max))                    
for i in se:
    print(i)
