# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 10:59:59 2020

@author: admin
"""

import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')

from os import listdir
import numpy as np
from scipy import ndimage
import skimage.io as io
import skimage
from skimage import feature
from skimage.color import rgb2gray
from skimage.transform import rescale
from skimage.transform import resize
from skimage.transform import downscale_local_mean
from skimage import transform as tf
from skimage import filters
from scipy import ndimage
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
    # im_color = cv.imread(r'C:\Users\tobias.grab\switchdrive\Schule\datax\projekt\input\try1.jpg')
    
    files=listdir(r"C:\Users\tobias.grab\switchdrive\Schule\datax\projekt\input")
    

    #Defining variables
    compression_factor=5
    canny_sigma=1
    
    #Importing and converting image
    im_color=io.imread(r'C:\Users\tobias.grab\switchdrive\Schule\datax\projekt\input\Testimage1.jpg')
    # im_color=io.imread("img\\IMG_20190312_183849.jpg")
    original=rgb2gray(im_color)
    bordersize=0.02;
    original=original[int(bordersize*original.shape[0]):int((1-bordersize)*original.shape[0]),
                      int(bordersize*original.shape[1]):int((1-bordersize)*original.shape[1])]
    print("original shape:", original.shape)
    print("original dtype:", original.dtype)
    
    #Making the image much smaller for comuptational reasons
    im=rescale(original,1/compression_factor, multichannel=False)
    print("rescaled size", im.shape)
    y_size=im.shape[0]
    x_size=im.shape[1]
    
    im=im>0.9
    
    #check the image
    plt.imshow(im)
    
    kernel = np.ones((10,10))==1
    im=skimage.morphology.binary_opening(im,kernel)
    plt.imshow(im, vmin=0, vmax=1,cmap="gray")
    plt.figure()
    
    
    #Filter the edges (Looking for the edges of the sheet)
    canny_sigma=1
    imedges=feature.canny(im,sigma=canny_sigma)
    plt.imshow(imedges)
    
    #Transfor into hough space for line detection
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
    
    #Plot everything 
    fig,(ax0,ax1) = plt.subplots(ncols=2, nrows=1, figsize=(15,8))
    ax0.imshow(imedges, cmap="gray")
    Himage = ax1.imshow(H,extent=(angles[0],angles[-1],distances[0],distances[-1]),origin="lower",aspect="auto")
    ax1.set(xlabel="angle [rad]", ylabel="d [pixels]", title="H: Hough space accumulator");
    plt.colorbar(Himage)
    
    # Plot a white rectangle over the maximum
    ax1.plot(theta, d, "ws", fillstyle="none")
    
    #Plot the lines in the normal space
    p0=np.zeros((2,4))
    p2=np.zeros((2,4))
    for i in range(0,4):
        ## Now we want to draw the line in image space
        # This is one point on the line
        p1 = np.array([d[0,i]*np.cos(theta[0,i]), d[0,i]*np.sin(theta[0,i])])
        # This is the unit vector pointing in the direction of the line (remember what theta means in Hough space!)
        linedir = np.array([np.cos(theta[0,i]+np.pi/2), np.sin(theta[0,i]+np.pi/2)])
        # These are two points very far away in two opposite directions along the line
        p0[:,i] = p1 - linedir * 1000
        p2[:,i] = p1 + linedir * 1000
        # We now draw a line through p0 and p2, without rescaling the axes.
        ax0.plot([p0[0],p2[0]],[p0[1],p2[1]], scalex=False, scaley=False)
    
    
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
    
    #Plot intersection points
    for i in range(0,4):
        ax0.plot(R[i][0,0],R[i][0,1],"ws", fillstyle="none", scalex=False, scaley=False)
    
    #Project the A4 Paper to bird's eye perspective and plot it
    ###########################################################
    dst_corners=np.squeeze(np.array([R[0],R[1],R[2],R[3]]))
    dst_sum=np.array([np.sum(dst_corners,axis=1)]).T
    dst_arr=np.concatenate((dst_corners, dst_sum),axis=1)
    sortedArr = dst_arr[np.argsort(dst_arr[:, 2])]*compression_factor
    
    if sortedArr[1,0]>sortedArr[2,0]:
        src = np.array([[0, 0], [0, 300*2], [400*2, 0],[400*2, 300*2]])
        # src = np.array([[0, 300*2],[0, 0],[400*2, 300*2],[400*2, 0]])
    else:
        src = np.array([[0, 0], [400*2, 0], [0, 300*2],[400*2, 300*2]])
        # src = np.array([[0, 300*2],[400*2, 300*2],[0, 0],[400*2, 0]])
        
    dst = sortedArr[:,:2]
    
    tform3 = tf.ProjectiveTransform()
    tform3.estimate(src, dst)
    warped = tf.warp(original, tform3, output_shape=(300*2,400*2))
    # warped=warped[100:400*2-100,100:300*2-100]
    # io.imsave(r'C:\Users\tobias.grab\switchdrive\Schule\datax\projekt\test\Testimg1.jpg',warped) 