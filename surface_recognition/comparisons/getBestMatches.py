# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 09:40:29 2020

@author: tobias.grab
"""
from tensorflow import keras
import numpy as np
from scipy import spatial
from os import listdir
import matplotlib.pyplot as plt
import cv2
import pandas as pd

def checkSimilarityAutoenc(img_to_check,files,shape0,shape1,encoder,encoded_imgs):
    
        img_to_check=np.reshape(img_to_check, (1, shape0, shape1, 1))
        img_to_check_enc=encoder.predict(img_to_check)
        distances=[abs(spatial.distance.cosine(img_to_check_enc, encoded_imgs[i,:])) for i in range(len(encoded_imgs))]
        
        idx = np.argpartition(distances, -2)[:top_k]
        
        topk_scores=[]
        topk_names=[]
        for a in range(len(idx)):
            topk_scores.append(distances[idx[a]])
            topk_names.append(files[idx[a]])

        return topk_names,topk_scores


def getBestMatches(alg,test_img,top_k):
    ##### Init Params
    data_path=r"C:\Users\tobias.grab\IWK_data\test"
    files=listdir(data_path)  
    ##### Init matching Algorithm
    
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
        
    if alg=="autoencoder":
        path_to_model=r'C:\Users\tobias.grab\switchdrive\Schule\datax\projekt\kerasModels'
        autoencoder = keras.models.load_model(path_to_model+'\\full_autoencoder.h5')
        encoder= keras.models.load_model(path_to_model+'\\encoder.h5')
        category="novel"
    
    ###### Match test image with the chosen algorithm
    
    if category=="old but gold":
        nrOfFiles=len(files)
        # imgToMatch = cv2.imread(r'C:\Users\tobias.grab\switchdrive\Schule\datax\projekt\database_test\Nr384_2.jpg',0)
        # imgToMatch = cv2.imread(r"C:\Users\tobias.grab\IWK_data\test\org_Nr384_2.jpg",0)
        test_img
        
        (kps1, descs1) = ftAlg.detectAndCompute(test_img, None)
        
        nrOfGoodPerImage=np.zeros([nrOfFiles,1])
        DistPerImage=np.zeros([nrOfFiles,1])
        bauteilnr=0
    
        #For all images in the database...
        for file in files:
            img_from_database = cv2.imread(data_path+'\\'+file,0)    
            (kps2, descs2) = ftAlg.detectAndCompute(img_from_database, None)
        
            bf = cv2.BFMatcher()
            matches = bf.knnMatch(descs1,descs2,k=2)
            matchesMask = [[0,0] for i in range(len(matches))]
            
            for i,(m,n) in enumerate(matches):
                if m.distance < 0.75*n.distance:
                        matchesMask[i]=[1,0]
     
            nrOfGoodPerImage[bauteilnr]=np.sum(matchesMask[:])
            bauteilnr=bauteilnr+1
            

        #Get the best match and display it
        # print("The best match in the database is", files[np.argmax(nrOfGoodPerImage)])
        # bestMatch=cv2.imread(data_path+"\\"+files[np.argmax(nrOfGoodPerImage)],0)
        # fig,(ax0,ax1)=plt.subplots(ncols=1, nrows=2, figsize=(15,8))
        # ax0.imshow(test_img,cmap='gray')
        # ax1.imshow(bestMatch,cmap='gray')
        
        idx = np.argpartition(-nrOfGoodPerImage[:,0], top_k)
        topk_scores=abs(nrOfGoodPerImage[idx[:top_k]])
        topk_names=[files[idx[a]] for a in list(range(top_k))]
    
    elif category=="novel":
        shape0=120
        shape1=160
        
        images=[]
        for file in files:
            # images.append(downscale_local_mean(cv2.imread(data_path+'\\'+file,0),(shrinkFactor,shrinkFactor)))
            images.append(cv2.imread(data_path+'\\'+file,0))
        # images = [exposure.equalize_hist(i) for i in images]
        # images=[i.astype('float32') for i in images]
        
        x_all= np.array(images[:])
        x_train = np.array(images[:350])
        x_test = np.array(images[350:])
        x_all = np.reshape(x_all, (len(x_all), shape0, shape1, 1))
        x_train = np.reshape(x_train, (len(x_train), shape0, shape1, 1))
        x_test = np.reshape(x_test, (len(x_test), shape0, shape1, 1))
        
        encoded_imgs=encoder.predict(x_train)
        topk_names,topk_scores=checkSimilarityAutoenc(test_img,files,shape0,shape1,encoder,encoded_imgs)
    
    best_matches=pd.DataFrame({'name':topk_names,'score':topk_scores[:,0]})
    
    
    return best_matches

if __name__ == "__main__":
    alg="sift"
    test_img=cv2.imread(r"C:\Users\tobias.grab\IWK_data\test\org_Nr384_2.jpg",0)
    top_k=10
    best_matches=getBestMatches(alg,test_img,top_k)