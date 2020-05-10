class Mylist(list):
    def product(self):
        sum=1
        for i in range(0,len(self)):
            sum*=self[i]
        return sum

a=Mylist([1,2,3,4,5,6])
print('列表各项逐次乘积为',a.product())
