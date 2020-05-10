from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance
img = Image.open("mama.jpg")
print(img.format)		 # 输出图片基本信息
print(img.mode)
print(img.size)
img_resize = img.resize((256,256)) # 调整尺寸
img_resize.save("mamaresize.jpg")
img_rotate = img.rotate(45)         # 旋转
img_rotate.save("mamarotate.jpg")
om=img.convert('L')				# 灰度处理
om.save('mamagray.jpg')
om = img.filter(ImageFilter.CONTOUR)		# 图片的轮廓
om.save('mamacontour.jpg')
om = ImageEnhance.Contrast(img).enhance(20)		# 对比度为初始的10倍
om.save('mamaencontrast.jpg')
'''#更改图片格式：
from PIL import Image
import os
 
filelist =["dog.jpg",
           "dogcontour.jpg",
           "dogencontrast.jpg",
           "doggray.jpg",
           "dogresize.jpg",
           "dogrotate.jpg",
           ]
for infile in filelist:
  outfile = os.path.splitext(infile)[0] + ".png"
  if infile != outfile:
    try:
      Image.open(infile).save(outfile)
    except IOError:
      print ("cannot convert", infile)'''

