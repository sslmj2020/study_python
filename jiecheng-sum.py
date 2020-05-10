n=int(input('请输入大于2的整数\n' ))

sum=0
for i in range(1,n+1):
    temp=1
    for j in range(1,i+1):
        temp=temp*j
    sum=sum+temp
print('1!+...+%d!='% n,sum)

      
