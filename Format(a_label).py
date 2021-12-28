import os
from PIL import Image

def convert(box):
    dw = 1/227
    dh = 1/227
    x = box[0]
    y = box[1]
    w = box[2]
    h = box[3]
    x = round(x*dw,6)
    w = round(w*dw,6)
    y = round(y*dh,6)
    h = round(h*dh,6)
    return (x,y,w,h)




data_path = './a_label'
data = os.listdir(data_path)


for i in data:
    
    f_input = open( './a_label/'+i,'r')
    item=f_input.readline()
    data=item.split()
    b = (float(data[0]),float(data[1]),float(data[2]), float(data[3]))
    bb = convert(b)
    f = open('./format/'+i, 'w')
    f.write(str(2)+" "+" ".join([str(a) for a in bb]) + '\n')