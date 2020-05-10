from PIL import Image
im=Image.open('lucky.bmp')
width=im.size[0]
height=im.size[1]
print('宽有%d' % (width,))
print('高有%d' % (height,))
s=list()
p=list()
y=list()
#取出左上角8*8个像素给列表s
for h in range(8):
    for w in range(8):
        pixel=im.getpixel((w,h))
        s.append(pixel)
print(s)
#将前64个像素的第一个通道的数值取出加入到p列表
for i in range(64):
        p.append(s[i][0])
print(p)
#生成64个0的列表y
for k in range(64):
    y.append(0)
#给特定位置赋值1（后面用到）
y[9]=1
y[14]=1
y[16]=1        
y[18]=1        
y[21]=1
y[23]=1
y[24]=1    
y[27]=1
y[28]=1
y[31]=1
y[33]=1
y[38]=1
y[42]=1
y[45]=1
y[51]=1
y[52]=1
print(y)
#利用生成器将p和y对应元素相加
c=[p[i]+y[i] for i in range(len(p))]
print(c)
q=0
for h in range(8):
    for w in range(8):
        pixel=im.getpixel((w,h))
        im.putpixel((w,h),(c[q],pixel[1],pixel[2]))
        q+=1
im.save('jiamilucky.bmp')        

            
    
    
        
        
