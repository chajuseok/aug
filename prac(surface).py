import argparse
import os
import numpy as np
import json
from torch.utils.data import Dataset
import pickle
from tqdm import tqdm
import shutil
import copy
import random
from time import sleep

if __name__ == '__main__':
    
    

    data_path = './surface'
    


    # load file list
    data = os.listdir(data_path)
    
    t = 1
    for i in data:
        temp = i.split('.');
        if(temp[1] == 'jpg'):
            
            path = data_path + '/' + i
            shutil.copy2(path, "./pr"+ "/" + str(t) + '.jpg')
            t = t+1

    
         

    


