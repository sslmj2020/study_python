from PIL import Image,ImageDraw,ImageFont,ImageFilter
import random
def rndChar():
    return chr(random.randint(65,90))
def rndColar():
    return (random.randint(100,255),\
            random.randint(100,255),\
            random.randint(100,255))
def rndColar2():
    return (random.randint(32,100),\
            random.randint(32,100),\
            random.randint(32,100))
width=240
height=60
for g in range(5):
    image=Image.new('RGB',(width,height),(255,255,255))
    font=ImageFont.truetype('simsun.ttc',36)
    draw=ImageDraw.Draw(image)
    for x in range(width):
        for y in range(height):
            draw.point((x,y),fill=rndColar())
    for t in range(0,4,1):
        draw.text((60*t+10,10),rndChar(),font=font,fill=rndColar2())
    image=image.filter(ImageFilter.BLUR)
    image.save('code%d.jpg' % g,'jpeg')
    
