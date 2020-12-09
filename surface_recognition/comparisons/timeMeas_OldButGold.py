# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 11:59:55 2020

@author: tobias.grab
"""

from skimage.transform import rotate
from skimage.transform import downscale_local_mean
import keras
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
import tensorflow_addons as tfa
import time
import pandas as pd


if __name__ == "__main__":
    
    top_k=5
    implemented_algos=["sift","surf","brisk","akaze","kaze"]
    # implemented_algos=["sift"]
    database_size=[100,200,400,800,1600,3200]
    # database_size=[100,200]

    data_path=r"C:\Users\tobias.grab\IWK_data\timetest"
    files=listdir(data_path)  
    
    path_testimgs=r"C:\Users\tobias.grab\IWK_data\test_testimgs"
    test_files=listdir(path_testimgs)
    test_imgs=[cv2.imread(path_testimgs + "\\" + filename,0) for ind,filename in enumerate(test_files)]
    
    alg="brisk"
    ##### Init matching Algorithm
    
    
    for alg in implemented_algos:
        print(alg)
        creation=[]
        mean_times=[]
        std_times=[]
        for database_size_now in database_size:    
            if alg=="sift":
                ftAlg = cv2.xfeatures2d.SIFT_create()
                category="old but gold"
                
            if alg=="surf":
                ftAlg = cv2.xfeatures2d.SURF_create()
                category="old but gold"
                
            if alg=="brisk":
                ftAlg = cv2.BRISK_create()
                category="old but gold"
                
            if alg=="akaze":
                ftAlg = cv2.AKAZE_create()
                category="old but gold"
                
            if alg=="kaze":
                ftAlg = cv2.KAZE_create()
                category="old but gold"
                
            bf = cv2.BFMatcher()
            
            start=time.time()
            
            
            nrOfFiles=len(files)
            
            precomputed_fts=[]
            start_creation=time.time()
            for file in files[:database_size_now]:
                img_from_database = cv2.imread(data_path+'\\'+file,0)    
                precomputed_fts.append(ftAlg.detectAndCompute(img_from_database, None))
            end_creation=time.time()-start_creation
            creation.append(end_creation)
            times=[]
            for ind, test_img in enumerate(test_imgs):
                name_testimg=test_files[ind]
                (kps1, descs1) = ftAlg.detectAndCompute(test_img, None)
                
                nrOfGoodPerImage=np.zeros([nrOfFiles,1])
                DistPerImage=np.zeros([nrOfFiles,1])
                bauteilnr=0
            
                start_matching=time.time()
                for kps2, descs2 in precomputed_fts:
                    matches = bf.knnMatch(descs1,descs2,k=2)
                    matchesMask = [[0,0] for i in range(len(matches))]
                    
                    for i,(m,n) in enumerate(matches):
                        if m.distance < 0.75*n.distance:
                                matchesMask[i]=[1,0]
             
                    nrOfGoodPerImage[bauteilnr]=np.sum(matchesMask[:])
                    bauteilnr=bauteilnr+1
                
                idx = np.argpartition(-nrOfGoodPerImage[:,0], top_k)
                topk_scores=abs(nrOfGoodPerImage[idx[:top_k]])
                
                stop_matching=elapsed=time.time()-start_matching
                # print(stop_matching)
                times.append(stop_matching)
            mean_times.append(np.mean(times))
            std_times.append(np.std(times))
    
        
        print(alg)
        print("mean\n")
        [print(t) for t in mean_times] 
        print("std\n")
        [print(t) for t in std_times] 
        print("create\n")
        [print(t) for t in creation] 
    
    