def even_number(max):
    n=0
    while n<max:
        yield n
        n+=2
for i in even_number(15):
    print (i)
'''只有在用到哪个的时候才生成，所以开始不会占用大内存'''
