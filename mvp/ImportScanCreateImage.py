"""
@author: Tobias Grab
"""

###########################################################################
## Import the necessary functions
###########################################################################

import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
import numpy as np
import matplotlib.pyplot as plt

import skimage.io as io
import skimage
from skimage import feature
from skimage.color import rgb2gray
from skimage.transform import rescale
from skimage import transform as tf
import skimage.transform.hough_transform as ht



###########################################################################
## Definition of some helper functions
###########################################################################

#INPUT: two points
#OUTPUT: coefficients A, B, C of line equation that goes through the two input points, A1 * x + B1 * y = C1
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



###########################################################################
## Start of main program
###########################################################################
# We basically want to import the scanner image find the exact location of the
# plastic part on the image. Once we know the location, we want to create a
# new image (600*800) that only contains the plastic part
###########################################################################

if __name__ == "__main__":
    #######################################################################
    ## Preprocess image
    #######################################################################
    # Import the scanner image, convert the image from color to grayscale
    # since it is much easier to work with and remove the border of the image
    # (A rgb image consists of 3 layers, one for red green for blue.
    # 100mio numbers in our case. A grayscale image has only one layer. Each
    # pixel can either be bright (255), black (0) or something in between.)
    
    # Change the path to a scanner image (Sampledata\Scanned_images in our
    # shared google folder)
    path=r'C:\Users\tobias.grab\switchdrive\Schule\datax\projekt\input\20200916151652_001.jpg'
    im_color=io.imread(path)
    original=rgb2gray(im_color)
    bordersize=0.02;
    original=original[int(bordersize*original.shape[0]):int((1-bordersize)*original.shape[0]),
                      int(bordersize*original.shape[1]):int((1-bordersize)*original.shape[1])]
    print("original shape:", original.shape)
    print("original dtype:", original.dtype)
    
    
    # Rescale the image for computational reasons. Scaling both sides by 
    # factor of five leads to 25 times less numbers to work with
    # (about 1.3 million insead of 33 million)
    scaling_factor=5
    im=rescale(original,1/scaling_factor, multichannel=False)
    print("rescaled size", im.shape)
    y_size=im.shape[0]
    x_size=im.shape[1]
    
    # PREPROCESSING
    # Create a binary image and remove the noise from the image (Some white
    # spots where the plasic part is) using a morphological opening.
    # Simplified a opening replaces the value of each pixel first by the minimum
    # value in its neighborhood (Defined by the kernel). In a second step the
    # value of each pixel gets replaced by the maximum in its neighborhood.
    # That leads to the result, that white spots smaller than the kernel
    # will be black after the opening.
    
    im=im>0.9
    plt.figure()
    plt.imshow(im,vmin=0, vmax=1,cmap="gray")
    kernel = np.ones((10,10))==1
    im=skimage.morphology.binary_opening(im,kernel)
    plt.figure()
    plt.imshow(im, vmin=0, vmax=1,cmap="gray")
    
    # Filter the edges (Looking for the edges of the plastic part)
    # Finding edges of an image can basically be done by calculating the
    # gradient of the image (Using a 2D convolution) since edges are usually
    # strong changes in illumination (so have a high gradient)
    # The canny edge detector is a more sophisticaed way to do it, but the
    # principle is the same
    canny_sigma=1
    plt.figure()
    imedges=feature.canny(im,sigma=canny_sigma)
    plt.imshow(imedges)
    
    #######################################################################
    ## Find the corners of the plastic parts (Intersection of the edge lines) 
    #######################################################################
    # First we have to a representation of the edges, which are in our case
    # the four most prominant lines in the image. Since we want to do some
    # calculations with it, we need to get formulas for those lines.
    # In order to get those formulas, we use a hough transformation
    
    
    # A line usually gets represented by the equation y=a*x+b, however the
    # problem there is that a vertical line can not be represented. A more
    # robust representation is a representation by a angle and a distance (from zero)
    
    # With a hough transformation we transform our image into the hough space.
    # The hough space is a representation of all possible lines, one dimension
    # is the distance, the other the angle. Every point in the hough space
    # is a line in the image. The hough algorithm is basically a voting algorithm.
    # For every point in the hough space, we calculate corresponding line in 
    # our original image the line and count the number of points  that are 
    # on that line. The points with the most votes (the max value) in the hough space
    # correspond to the most prominant line.
    
    # The same principle can be used for circle detection, square detection and
    # so on. You only need to be able to define with hough space with only a few
    # variables (e.g. the radius, and the coordinates of the middle point for
    # a circle ==> the hough space wouldn't be 2 dimensional anymore)
    H,angles,distances = ht.hough_line(imedges)
    # The probelm is that the same line can be representet by a distance and thetha
    # as well as -distance and -theta... so we set half of the hough space to zero
    H[:int(H.shape[0]/2),:int(H.shape[1]/2)]=0
    
    #Find four most dominant points in the hough space, once a dominant point is
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
    #D and theta are the distance and angle representation of the four most
    #prominant lines
    ########################################################################
    ## We got a represenation of the lines now, time to plot everything
    ########################################################################
    
    #Plot of the hough space
    fig,(ax0,ax1) = plt.subplots(ncols=2, nrows=1, figsize=(15,8))
    ax0.imshow(imedges, cmap="gray")
    Himage = ax1.imshow(H,extent=(angles[0],angles[-1],distances[0],distances[-1]),origin="lower",aspect="auto")
    ax1.set(xlabel="angle [rad]", ylabel="d [pixels]", title="H: Hough space accumulator");
    plt.colorbar(Himage)
    ax1.plot(theta, d, "ws", fillstyle="none")
    
    #Plot of the image with the most prominant lines
    p0=np.zeros((2,4))
    p2=np.zeros((2,4))
    for i in range(0,4):
        #In order to draw the line, we need two points on it
        p1 = np.array([d[0,i]*np.cos(theta[0,i]), d[0,i]*np.sin(theta[0,i])])
        linedir = np.array([np.cos(theta[0,i]+np.pi/2), np.sin(theta[0,i]+np.pi/2)])
        p0[:,i] = p1 - linedir * 1000
        p2[:,i] = p1 + linedir * 1000
        # We now draw a line through p0 and p2, without rescaling the axes.
        ax0.plot([p0[0],p2[0]],[p0[1],p2[1]], scalex=False, scaley=False)
    
    
    ########################################################################
    ## We now want find the corners, which are the intersections of the lines
    ########################################################################
    
    
    
    # We first use our two points (which we made for the plot)
    # to calculate the a*x+b representation using a helper function
    lines=[]
    for i in range(0,4):
        lines.append(line(p0[:,i].T, p2[:,i].T))
    #returns A, B and C of A1 * x + B1 * y = C1
    
    
    #Since we only have four lines, we can calculate all possible combination of
    #intersections. If we have parallel lines, there is no intersection
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
    
    
    #######################################################################
    ## We finally use the function transform library from skimage
    ## in order to cut out and warp the image of the plastic part from our
    ## original (high resoultion) image using the calculated corner points
    ##
    ## The skimage.transform.ProjectiveTransform.estimate and the
    ## skimage.transform.warp functions are very confusing, so I am just glad
    ## that it works
    #######################################################################
    
    dst_corners=np.squeeze(np.array([R[0],R[1],R[2],R[3]]))
    dst_sum=np.array([np.sum(dst_corners,axis=1)]).T
    dst_arr=np.concatenate((dst_corners, dst_sum),axis=1)
    sortedArr = dst_arr[np.argsort(dst_arr[:, 2])]*scaling_factor
    
    if sortedArr[1,0]<sortedArr[2,0]:
        src = np.array([[0, 0], [0, 300*2], [400*2, 0],[400*2, 300*2]])
    else:
        src = np.array([[0, 0], [400*2, 0], [0, 300*2],[400*2, 300*2]])
    
    
    
    dst = sortedArr[:,:2]
    
    tform3 = tf.ProjectiveTransform()
    tform3.estimate(src, dst)
    
    
    ######################################################################
    ## We finally have our plastic part image in the variable "warped",
    ## so lets plot it in order to check
    ######################################################################
    warped = tf.warp(original, tform3, output_shape=(300*2,400*2))
    plt.figure()
    plt.imshow(warped,cmap='gray')
    # io.imsave(r'C:\Users\tobias.grab\switchdrive\Schule\datax\projekt\test\Testimg1.jpg',warped) 