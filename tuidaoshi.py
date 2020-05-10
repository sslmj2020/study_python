a={x+y for x in range(10) for y in range(x)}
print(a)
b={x*x for x in range(10)}
print(b)
c={'K%d'% x:x**3 for x in range(10)}
print(c)
d=[x**3 for x in range(10)]
print(d)
