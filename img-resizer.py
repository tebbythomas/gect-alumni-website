import os
from PIL import Image
from resizeimage import resizeimage

r=[]                        
subdirs = [x[0] for x in os.walk("media")]
for subdir in subdirs:
    files = os.walk(subdir).__next__()[2]
    if (len(files) > 0):
        for file in files:
            if '.DS_Store' not in file:
                with Image.open(subdir + "/" + file) as img:
                    try:
                        img = resizeimage.resize_width(img, 1300)
                        img.save(subdir + "/" + file, img.format)
                    except Exception as e: 
                        if 'Image is too small' in str(e):
                            pass