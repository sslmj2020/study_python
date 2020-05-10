import time
t1=time.time()
a=0
for i in range(1,10000):
    a+=i
print(a)
time.sleep(15)
t2=time.time()
print(t2-t1)
