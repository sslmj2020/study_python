from PIL import Image,ImageDraw,ImageFont,ImageFilter
img=Image.open('mama.jpg')
om=img.filter(ImageFilter.CONTOUR)
font=ImageFont.truetype('simsun.ttc',50)
draw=ImageDraw.Draw(om)
draw.text((50,50),'泡\n面\n真\n好\n吃',(0,255,0),font=font)
om=om.rotate(45)
om.save('mama1.jpg','jpeg')          
