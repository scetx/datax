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

def checkSimilarityAutoenc(img_to_check,files,shape0,shape1,encoder,encoded_imgs,top_k):
    
        img_to_check=img_to_check.astype('float32')/255
        img_to_check=np.reshape(img_to_check, (1, shape0, shape1, 1))
        img_to_check_enc=encoder.predict(img_to_check)
        distances=[abs(spatial.distance.cosine(img_to_check_enc, encoded_imgs[i,:])) for i in range(len(encoded_imgs))]
        
        idx = np.argpartition(distances, 2)[:top_k]
        
        avg_score=np.mean(distances)
        topk_scores=[]
        topk_names=[]
        for a in range(len(idx)):
            topk_scores.append(distances[idx[a]])
            topk_names.append(files[idx[a]])

        return topk_names,topk_scores,avg_score
    
if __name__ == "__main__":
    
    top_k=5
    implemented_algos=["autoencoder"]
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
        
        if alg=="autoencoder":
            path_to_model=r'C:\Users\tobias.grab\switchdrive\Schule\datax\projekt\kerasModels'
            autoencoder = keras.models.load_model(path_to_model+'\\full_autoencoder.h5')
            encoder= keras.models.load_model(path_to_model+'\\encoder.h5')
    
        if alg=="invariant autoencoder":
            path_to_model=r'C:\Users\tobias.grab\switchdrive\Schule\datax\projekt\kerasModels'
            autoencoder = keras.models.load_model(path_to_model+'\\full_invariant_autoencoder.h5')
            encoder= keras.models.load_model(path_to_model+'\\invariant_encoder.h5')
        
        
        for database_size_now in database_size:    
            
            shape0=120
            shape1=160
            start=time.time()
            
            
            nrOfFiles=len(files)
            
            start_creation=time.time()
            images=[]
            for file in files[:database_size_now]:
                # images.append(downscale_local_mean(cv2.imread(data_path+'\\'+file,0),(shrinkFactor,shrinkFactor)))
                images.append(cv2.imread(data_path+'\\'+file,0))
            # images = [exposure.equalize_hist(i) for i in images]
            # images=[i.astype('float32') for i in images]
            # 
            x_all= np.array(images[:])
            x_all=x_all.astype('float32')/255
            # x_train = np.array(images[:350])
            # x_test = np.array(images[350:])
            x_all = np.reshape(x_all, (len(x_all), shape0, shape1, 1))
            
            start_creation=time.time()
            encoded_imgs=encoder.predict(x_all)
            end_creation=time.time()-start_creation
            creation.append(end_creation)
            
            times=[]
            for test_img in test_imgs:
                start_matching=time.time()
                topk_names,topk_scores,avg_score=checkSimilarityAutoenc(test_img,files,shape0,shape1,encoder,encoded_imgs,top_k)
                stop_matching=elapsed=time.time()-start_matching
                times.append(stop_matching)
        
            mean_times.append(np.mean(times))
            std_times.append(np.std(times))
            
            best_matches=pd.DataFrame({'name':topk_names,'score':topk_scores})
            best_matches=pd.DataFrame(np.array(best_matches.sort_values(by='score',ascending="False")),columns=["name","score"])
    
    
        
        
        print(alg)
        print("mean\n")
        [print(t) for t in mean_times] 
        print("std\n")
        [print(t) for t in std_times] 
        print("create\n")
        [print(t) for t in creation] 
    
    