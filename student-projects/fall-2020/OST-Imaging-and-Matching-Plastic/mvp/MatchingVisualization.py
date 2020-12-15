# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 10:23:38 2020

@author: tobias.grab
"""

import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
import cv2
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":

    alg="surf"
    if alg=="sift":
        ftAlg = cv2.xfeatures2d.SIFT_create()
        
    if alg=="surf":
        ftAlg = cv2.xfeatures2d.SURF_create()
        
    if alg=="brisk":
        ftAlg = cv2.BRISK_create()
        
    if alg=="akaze":
        ftAlg = cv2.AKAZE_create()
        
    if alg=="kaze":
        ftAlg = cv2.KAZE_create()

    imgToMatch = cv2.imread(r'C:\Users\tobias.grab\switchdrive\Schule\datax\projekt\database\Nr384.jpg',0)
    (kps1, descs1) = ftAlg.detectAndCompute(imgToMatch, None)
    # img_from_database=cv2.imread(r'C:\Users\tobias.grab\switchdrive\Schule\datax\projekt\test\Testimg1.jpg',0)
    img_from_database = cv2.imread(
        r'C:\Users\tobias.grab\switchdrive\Schule\datax\projekt\database_test\Nr384_2.jpg',0)    
    (kps2, descs2) = ftAlg.detectAndCompute(img_from_database, None)
    img1 = cv2.drawKeypoints(imgToMatch, kps1, None)
    img2 = cv2.drawKeypoints(img_from_database, kps2, None)
    
    plt.figure()
    plt.imshow(img2)
    
    bf = cv2.BFMatcher()
    matches = bf.knnMatch(descs1,descs2,k=2)
    matchesMask = [[0,0] for i in range(len(matches))]
    
    good = []
    for m,n in matches:
        if m.distance < 0.75*n.distance:
            good.append([m])
    img3 = cv2.drawMatchesKnn(img1,kps1,img2,kps2,good,None,flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
    plt.figure()
    plt.imshow(img3),plt.show()
    
    # img4 = cv2.drawMatchesKnn(img1,[],img2,[],good,None,flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
    # plt.figure()
    # plt.imshow(img4),plt.show()
    
# # cv.drawMatchesKnn expects list of lists as matches.
    
#     for i,(m,n) in enumerate(matches):
#         if m.distance < 0.75*n.distance:
#             matchesMask[i]=[1,0]


    # fig,(ax0,ax1)=plt.subplots(ncols=1, nrows=2, figsize=(15,8))
    # ax0.imshow(imgToMatch,cmap='gray')
    # ax1.imshow(bestMatch,cmap='gray')
    