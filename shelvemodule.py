import random
with open('F:\shelve.txt','r') as f:
    txt1=str(f.read())
    print(txt1)
    txt2=txt1.split()
    print(txt2)
    print(len(txt2))
    print('随机抽取一个单词为',random.choice(txt2))
    print('随机抽取三个单词为',random.sample(txt2,3))
    


              
