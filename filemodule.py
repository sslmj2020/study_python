d=open('F:\shelve.txt','wt')
d.writelines(['bigapple\n','adadadadadpie\n','daddad垃圾\n'])
d.close()
f=open('F:\shelve.txt','rt')
print(f.readlines())
f.close()

              
