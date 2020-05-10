class Student:
    def __init__(self,name,grade):
        self.name,self.grade=name,grade
    def __lt__(self,s2):
        if self.grade>s2.grade:
            return True
        elif self.grade==s2.grade:
            return self.name<s2.name
    def __str__(self):
        return '(%s,%d)' % (self.name,self.grade)
    __repr__=__str__
class High_student(Student):
    def __init__(self,name,grade,school):
        super().__init__(name,grade)
        self.school=school
s=list()
s.append(Student('Lilei',90))
s.append(Student('Hanmeimei',56))
s.append(Student('Zhangsan',99))
s.append(Student('Wangdehua',90))
s.append(Student('Guofucheng',80))
print('原始顺序\n',s)
s_sort=sorted(s)
print('排序后\n',s_sort)         
'''先按成绩从大到小排序，如果成绩相同按名字字母顺序先后排序'''
p=High_student('鹿鸣',100,'合肥工业大学')
print('姓名：%s\n成绩：%d\n学校：%s\n' % (p.name,p.grade,p.school))
