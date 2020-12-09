# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 09:57:38 2020

@author: tobias.grab
"""
from skimage.transform import downscale_local_mean
from keras.layers import Input, Dense, Conv2D, MaxPooling2D, UpSampling2D, BatchNormalization, Flatten, Reshape
from keras.models import Model
from keras import backend as K
from keras.callbacks import EarlyStopping
from keras.callbacks import ModelCheckpoint
import tensorflow as tf
from skimage import exposure
import matplotlib.pyplot as plt
import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
from os import listdir
import cv2
import numpy as np
from scipy import spatial

if __name__ == "__main__":
    
    data_path=r'C:\Users\tobias.grab\switchdrive\Schule\datax\projekt\database'
    files=listdir(data_path)
    nrOfFiles=len(files)
    shape0=int(1200)
    shape1=int(1600)
    createData=0
    
    if createData==1:
        images=[]
        for file in files[0:int(nrOfFiles/10)]:
            images.append(cv2.imread(data_path+'\\'+file,0))
                
        # images = [exposure.equalize_hist(i) for i in images]
        images=[i.astype('float32') for i in images]
            
        x_all= np.array(images[:])
        x_all = np.reshape(x_all, (len(x_all), shape0, shape1, 1))
        del images
        
        images=[]
        for file in files[int(nrOfFiles/10):]:
            images.append(cv2.imread(data_path+'\\'+file,0))
        images=[i.astype('float32') for i in images]
            
        x_all2= np.array(images[:])
        x_all2 = np.reshape(x_all2, (len(x_all2), shape0, shape1, 1))
        del images
        
        x=np.concatenate([x_all,x_all2],axis=0)
        del x_all 
        del x_all2
        x=np.squeeze(x)
    
    save_path_visual=r'C:\Users\tobias.grab\IWK_data\artificialVisual'
    for it in range(nrOfFiles):
        a = downscale_local_mean(x[it,:,:],(10,10))
        a = exposure.equalize_hist(a)
        a = a.astype('float32')
        cv2.imwrite(save_path_visual+'\\org_'+str(files[it]),a)
        for iterator in range(it,nrOfFiles):
            if it!=iterator:
                a=np.max([x[iterator,:,:],x[it,:,:]],axis=0)
                a=downscale_local_mean(a,(10,10))
                a = exposure.equalize_hist(a)
                a = a.astype('float32')
                cv2.imwrite(save_path_visual+'\\'+str(it)+'_'+str(iterator)+'.jpg',a)
                
    
    
    