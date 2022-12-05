from PIL import Image
import os

#get all the files from current path
file_list = os.listdir(os.getcwd())
#get only'.jpeg' files
file_list_pic = [file for file in file_list if file.endswith('.jpeg')]

#from file_list_pic
for f in file_list_pic:
    img = Image.open(f)
    width, height = img.size
    TARGET_WIDTH = 50
    coefficient = width / 50
    new_height = height / coefficient
    img = img.resize((int(TARGET_WIDTH),int(new_height)),Image.ANTIALIAS)
    img.save(f,quality=95)
