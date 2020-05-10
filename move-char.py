a=list(input('请输入字符串：\n'))
step=int(input('请输入向右循环移动步数：\n'))
le=len(a)
b=a[le-step:le]+a[0:le-step]
b=''.join(b)
"""print('%s循环右移%d步后变为:%s 'b)
"""
print(b) 

