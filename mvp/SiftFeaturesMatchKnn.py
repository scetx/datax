# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 08:46:30 2020

@author: tobias.grab
"""
import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')

from os import listdir
import cv2
import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt
from skimage.transform import rescale


if __name__ == "__main__":
    
    data_path=r'C:\Users\tobias.grab\switchdrive\Schule\datax\projekt\output'
    
    files=listdir(data_path)
    nrOfFiles=len(files)

    
    #Image to match
    img1 = cv2.imread(r'C:\Users\tobias.grab\switchdrive\Schule\datax\projekt\test\Testimg1.jpg',0)
    # sift = cv2.xfeatures2d.SIFT_create()
    # (kps1, descs1) = sift.detectAndCompute(img1, None)
    
    
    surf = cv2.xfeatures2d.SURF_create()
    (kps1, descs1) = surf.detectAndCompute(img1, None)
    
    
    # kp_img1 = cv2.drawKeypoints(img1, kps1, None,
    #                            flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    # plt.figure()
    # io.imshow(kp_img1)
    
    nrOfGoodPerImage=np.zeros([nrOfFiles,1])
    
    bauteilnr=0
    for file in files:
        
        
        img_from_database = cv2.imread(data_path+'\\'+file,0)
        (kps2, descs2) = surf.detectAndCompute(img_from_database, None)
        # (kps2, descs2) = sift.detectAndCompute(img_from_database, None)
        
        # BFMatcher with default params
        FLANN_INDEX_KDTREE = 0
        index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
        search_params = dict(checks=50)   # or pass empty dictionary
        flann = cv2.FlannBasedMatcher(index_params,search_params)
        matches = flann.knnMatch(descs1,descs2,k=2)

        # Need to draw only good matches, so create a mask
        matchesMask = [[0,0] for i in range(len(matches))]
        
        # ratio test as per Lowe's paper
        for i,(m,n) in enumerate(matches):
            if m.distance < 0.75*n.distance:
                    matchesMask[i]=[1,0]
        
        nrOfGoodPerImage[bauteilnr]=np.sum(matchesMask[:])
        bauteilnr=bauteilnr+1
    print("The best match in the database is", files[np.argmax(nrOfGoodPerImage)])
    io.imshow(img1,cmap="gray")
    plt.figure()
    io.imshow(data_path+"\\"+files[np.argmax(nrOfGoodPerImage)])
    