
import cv2
import numpy as np
import os
import random
# Read images : src image will be cloned into dst

data_path = './crop'

back_path = './pr'    


    # load file list
data = os.listdir(data_path)

back = os.listdir(back_path)

back_list = random.sample(back, len(data))

number = 0

for i in data:
    
    im = cv2.imread("pr/" + back_list[number])
    print(number)
    number = number + 1
    
    pp = "D:\crop" + "/" + i
    print(pp)
    obj= cv2.imread(pp)
    
    r_h, r_w, r_c = obj.shape
    
    if(r_w >= 100 or r_h >=100 or r_w <= 15 or r_h <=15):
        obj = cv2.resize(obj, dsize=(random.randrange(15,120),random.randrange(15,120)))
    
    width, height, channels = im.shape
    h, w, c = obj.shape
    # xmax = max((int(w/2)),(width - int(w/2)))
    # xmin = min((int(w/2)),(width - int(w/2)))
    
  
    x = random.randrange(60,170)
    # ymax = max((int(h/2)), (height - int(h/2)))
    # ymin = min((int(h/2)), (height - int(h/2)))
  
    y = random.randrange(60,170)
    # Create an all white mask
    mask = 255 * np.ones(obj.shape, obj.dtype)
    # The location of the center of the src in the dst
    
    center = (x,y)
    
    temp = str(x) + " " + str(y) + " "+ str(w) + " "+ str(h)
    f = open("./a_label/"+ i.split('.')[0] + '.txt', 'w')
    f.write(temp)
    mixed_clone = cv2.seamlessClone(obj, im, mask, center, cv2.MIXED_CLONE)
    
    cv2.imwrite('./ii/'+ i, mixed_clone)