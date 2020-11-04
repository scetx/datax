# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 08:20:39 2020

@author: tobias.grab
"""
from skimage.transform import downscale_local_mean
from os import listdir
import cv2


if __name__ == "__main__":
    
    data_path=r'C:\Users\tobias.grab\switchdrive\Schule\datax\projekt\artificial'
    save_path=r'C:\Users\tobias.grab\IWK_data\compressedData'
    
    files=listdir(data_path)
    nrOfFiles=len(files)
    shrinkFactor=10
    shape0=int(1200/shrinkFactor)
    shape1=int(1600/shrinkFactor)
    

    img=[]
    for file in files:
        img=(downscale_local_mean(cv2.imread(data_path+'\\'+file,0),(shrinkFactor,shrinkFactor)))
        img=img.astype('float32')
        cv2.imwrite(save_path+'\\'+str(file), img)
        