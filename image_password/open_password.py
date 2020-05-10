from PIL import Image
im=Image.open('jiamilucky.bmp')
om=Image.open('lucky.bmp')
s=list()
p=list()
for h in range(8):
    for w in range(8):
        pixel=om.getpixel((w,h))
        s.append(pixel)
for h in range(8):
    for w in range(8):
        pixel=im.getpixel((w,h))
        p.append(pixel)        
#生成64个0的列表y
y=list()
y=[p[i][0]-s[i][0] for i in range(64)]
#print(y)
omg=Image.new('RGB',(8,8),(255,255,255))
q=0
for h in range(8):
    for w in range(8):
        omg.putpixel((w,h),(y[q]*255,0,0))
        q+=1
omg=omg.resize((256,256))        
omg.show()        
omg.save('love.bmp')
