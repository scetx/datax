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
    
    data_path=r'C:\Users\tobias.grab\switchdrive\Schule\datax\projekt\magnImg'
    
    files=listdir(data_path)
    nrOfFiles=len(files)

    
    #Image to match
    img1 = cv2.imread(r'C:\Users\tobias.grab\switchdrive\Schule\datax\projekt\MagnTestImg\Bauteil1.jpg',0)
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
        bf = cv2.BFMatcher()
        matches = bf.knnMatch(descs1,descs2, k=2)
        
        # Apply ratio test
        good = []
        for m,n in matches:
            if m.distance < 0.75*n.distance:
                good.append([m])
        
        nrOfGoodPerImage[bauteilnr]=len(good)
        bauteilnr=bauteilnr+1
    
    
    # cv2.drawMatchesKnn expects list of lists as matches.
    # img3 = cv2.drawMatchesKnn(img1,kps1,img2,kps2,good,None,flags=2)
    
    # plt.imshow(img3),plt.show()