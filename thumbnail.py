import os, sys
from PIL import Image
import time
path = "images/"
paths = "thumbnail_images"
if not os.path.exists(paths):
    os.makedirs('thumbnail_images')

dirs = os.listdir(path)
print "THUMBNAIL_CREATOR"
width = int(raw_input("enter the width in pixels: "))
height = int(raw_input("enter the height in pixels: "))
for file in dirs:
    image_path=path+file
    print image_path,"--thumbnail_created"
    im = Image.open(image_path)
    resize = im.resize((width,height),Image.ANTIALIAS)
    resize.save("thumbnail_images/resized"+file+".jpg")


t =  time.sleep(1)
print "finished"
    
    
    
    
