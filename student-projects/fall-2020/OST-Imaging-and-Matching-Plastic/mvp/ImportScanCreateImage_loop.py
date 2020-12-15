# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 10:59:59 2020

@author: admin
"""

import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')

from os import listdir
import numpy as np
import skimage.io as io
import skimage
from skimage import feature
from skimage.color import rgb2gray
from skimage.transform import rescale
from skimage import transform as tf
import matplotlib.pyplot as plt
import skimage.transform.hough_transform as ht

#Produces coefs A, B, C of line equation by two points provided, A1 * x + B1 * y = C1
def line(p1, p2):
    A = (p1[1] - p2[1])
    B = (p2[0] - p1[0])
    C = (p1[0]*p2[1] - p2[0]*p1[1])
    return A, B, -C

#Finds intersection point (if any) of two lines provided by coefs.
def intersection(L1, L2, x_size, y_size):
    D  = L1[0] * L2[1] - L1[1] * L2[0]
    Dx = L1[2] * L2[1] - L1[1] * L2[2]
    Dy = L1[0] * L2[2] - L1[2] * L2[0]
    if D != 0:
        x = Dx / D
        y = Dy / D
        if x<0 or x>x_size or y<0 or y>y_size:
            x=0
            y=0
        
        return x,y
    else:
        return False

if __name__ == "__main__":
    
    compression_factor=5
    canny_sigma=1
    bauteilnr=0
    input_path=r'C:\Users\tobias.grab\switchdrive\Schule\datax\projekt\input'
    output_path=r'C:\Users\tobias.grab\switchdrive\Schule\datax\projekt\output'
    files=listdir(r"C:\Users\tobias.grab\switchdrive\Schule\datax\projekt\input")
    
    
    for file in files:
        bauteilnr=bauteilnr+1
        
        ######################################################################
        # Import image, binarize and find edges
        ######################################################################
        #Importing and converting image
        im_color=io.imread(input_path+'\\'+file)
        original=rgb2gray(im_color)
        bordersize=0.04;
        original=original[int(bordersize*original.shape[0]):int((1-bordersize)*original.shape[0]),
                          int(bordersize*original.shape[1]):int((1-bordersize)*original.shape[1])]
        
        #Making the image much smaller for comuptational reasons
        im=rescale(original,1/compression_factor, multichannel=False)
        print("rescaled size", im.shape)
        y_size=im.shape[0]
        x_size=im.shape[1]
        
        
        #Binarize the image and emphasize the plastic part with opening
        im=im>0.9    
        kernel = np.ones((10,10))==1
        im=skimage.morphology.binary_opening(im,kernel)
        
        
        #Filter the edges (Looking for the edges of the plastic part)
        canny_sigma=1
        imedges=feature.canny(im,sigma=canny_sigma)
        
        
        ######################################################################
        # Find most dominant lines using a hough transformation
        ######################################################################
        #Transfer the picture to hough space for line detection and delete some
        #of it in order not to get the same point twice (by using the same distance
        #and angle, but with the opposite sign)
        H,angles,distances = ht.hough_line(imedges)
        H[:int(H.shape[0]/2),:int(H.shape[1]/2)]=0
        
        
        #Find most dominant points in the hough space, once a dominant point is
        #detected, set points near it to zero
        d=[]
        theta=[]
        for i in range(0,4):
            (maxr, maxc) = np.unravel_index(np.argmax(H), H.shape)
            print(H.dtype)
            min_del_dist=maxr-20
            if min_del_dist<=0:
                min_del_dist=0;
            min_del_angle=maxc-5
            if min_del_angle<=0:
                min_del_angle=0;
            H[(min_del_dist):(maxr+20),(min_del_angle):(maxc+5)]=0;
            
            d.append(distances[maxr])
            theta.append(angles[maxc])
            print(d[i],theta[i])
        d=np.array([d])
        theta=np.array([theta])
        
        
        ######################################################################
        # Find lines and their intersections in the normal space
        ######################################################################
        
        #Get lines for the vertices
        p0=np.zeros((2,4))
        p2=np.zeros((2,4))
        for i in range(0,4):
            # This is one point on the line
            p1 = np.array([d[0,i]*np.cos(theta[0,i]), d[0,i]*np.sin(theta[0,i])])
            # This is the unit vector pointing in the direction of the line (remember what theta means in Hough space!)
            linedir = np.array([np.cos(theta[0,i]+np.pi/2), np.sin(theta[0,i]+np.pi/2)])
            # These are two points very far away in two opposite directions along the line
            p0[:,i] = p1 - linedir * 1000
            p2[:,i] = p1 + linedir * 1000

        #Find lines of the given code
        lines=[]
        for i in range(0,4):
            lines.append(line(p0[:,i].T, p2[:,i].T))
        #returns A, B and C of A1 * x + B1 * y = C1
        
        #Find intersection of all possible line combinations
        R=[]
        R.append(np.array([intersection(lines[0],lines[1], x_size, y_size)]))
        R.append(np.array([intersection(lines[0],lines[2], x_size, y_size)]))
        R.append(np.array([intersection(lines[0],lines[3], x_size, y_size)]))
        R.append(np.array([intersection(lines[1],lines[2], x_size, y_size)]))
        R.append(np.array([intersection(lines[1],lines[3], x_size, y_size)]))
        R.append(np.array([intersection(lines[2],lines[3], x_size, y_size)]))
        
        #Delete if no intersection
        for i in reversed(range(0,len(R))):
            if np.sum(R[i])==0:
                del R[i]
        
        
        
        ######################################################################
        # Create new image and save it
        ######################################################################
        #Get a new image with the plastic part in it and save it
        dst_corners=np.squeeze(np.array([R[0],R[1],R[2],R[3]]))
        dst_sum=np.array([np.sum(dst_corners,axis=1)]).T
        dst_arr=np.concatenate((dst_corners, dst_sum),axis=1)
        sortedArr = dst_arr[np.argsort(dst_arr[:, 2])]*compression_factor
        
        #Our plastic components have a shape of 30mm*40mm
        if sortedArr[1,0]<sortedArr[2,0]:
            src = np.array([[0, 0], [0, 300*2], [400*2, 0],[400*2, 300*2]])
        else:
            src = np.array([[0, 0], [400*2, 0], [0, 300*2],[400*2, 300*2]])
            
        dst = sortedArr[:,:2]
        
        tform3 = tf.ProjectiveTransform()
        tform3.estimate(src, dst)
        warped = tf.warp(original, tform3, output_shape=(300*2,400*2))
        io.imsave(output_path+'\\'+'Bauteil'+str(bauteilnr)+'.jpg',warped)    
    

    