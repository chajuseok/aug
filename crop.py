import numpy as np # linear algebra
import matplotlib.pyplot as plt # to show images
from PIL import Image # to read images
import os
import glob
import cv2
from PIL import Image

root_images="./prac"
root_label="./prac_label/"

all_images=os.listdir(root_images)

def convert(size, box):
    x = box[0]
    y = box[1]
    w = box[2]
    h = box[3]   
    w = w*size[0]
    h = h*size[1]
    x = x*size[0]
    y = y*size[1]  
    
    xmin = round(x - w/2,6)
    ymin = round(y - h/2,6)
    xmax = round(x + w/2,6)
    ymax = round(y + h/2,6)

    return(int(xmin),int(ymin),int(xmax),int(ymax))


def bounding_box(image):
  
    im = image.split('.')[0]
    im = im + '.txt'
    
    
    with open(root_label + im, 'r') as f:
        b =[]
        for i in f.readlines():
            temp = i.split(" ")
            if(temp[0] == '2'):
                b.append(temp[1] + " " + temp[2] + " " + temp[3] + " " + temp[4].split('\n')[0])
    return b    


for image in all_images:
    bbox = bounding_box(image)
    
    im=Image.open(os.path.join(root_images,image))
    q = 1
    for i in bbox:
        width = int(im.size[0])
        height = int(im.size[1])
        
        k = i.split(" ")
        bb = (float(k[0]),float(k[1]),float(k[2]),float(k[3]))
        vocbb = convert((width, height), bb)
        
        # print(vocbb[2] - vocbb[0])
        # print(vocbb[3] - vocbb[1])
        # print("##############")
        if((vocbb[2] - vocbb[0]) >= 10 and (vocbb[3]- vocbb[1]) >= 10):   
            print(vocbb)
            im = im.crop(vocbb)
            t = image.split('.')
            name = './crop/'+ t[0] + str(q)
            im.save(name+ ".jpg")
            q = q+1
        
                
    