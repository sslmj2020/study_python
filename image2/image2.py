from PIL import Image
import os
 
filelist =["mama.jpg",
           "mama.jpg",
           "mama.jpg",
           "mama.jpg",
           "mama.jpg",
           "mama.jpg",
           ]
for infile in filelist:
  outfile = os.path.splitext(infile)[0] + ".png"
  if infile != outfile:
    try:
      Image.open(infile).save(outfile)
    except IOError:
      print ("cannot convert", infile)
