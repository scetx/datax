##
## Import libraries, use opencv (cv2) version 3.4.2.16 so you don't run into
## licencing issues
##
import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
from os import listdir
import cv2
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    #########################################################################
    ## The script works for rotated test images very well, still has some
    ## problem with our test images, since the glitter in the plastic part
    ## reflects the light very different when scanned from another angle...
    ## Hence some points that used to be black (in the database image) are
    ## now white in the test image.
    ## This problem should be solved when using a scanner that measures the 
    ## pervasive light instead of the reflected
    #########################################################################
    ## Code is basically a modification of https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_feature2d/py_matcher/py_matcher.html
    ## and https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_feature2d/py_surf_intro/py_surf_intro.html
    
    
    # Get the names of all the images in the specified path (database images)
    # Change the path so it works for you (Images in google Folder 
    # Sampledata/PreprocessedScans_SampleData)
    
    

    # Specify the feature creation algorithm of the opencv library we want to use
    # brisk and akaze seem to work nice for our data. I don't know how they work
    # yet
    ########
    ## TODO: Research the different algorithm and choose a good one
    ########
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
    
    data_path=r'C:\Users\tobias.grab\switchdrive\Schule\datax\projekt\database'
    files=listdir(data_path)  
    nrOfFiles=len(files)
    imgToMatch = cv2.imread(r'C:\Users\tobias.grab\switchdrive\Schule\datax\projekt\database_test\Nr384_2.jpg',0)
    (kps1, descs1) = ftAlg.detectAndCompute(imgToMatch, None)
    
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
    print("The best match in the database is", files[np.argmax(nrOfGoodPerImage)])
    bestMatch=cv2.imread(data_path+"\\"+files[np.argmax(nrOfGoodPerImage)],0)
    fig,(ax0,ax1)=plt.subplots(ncols=1, nrows=2, figsize=(15,8))
    ax0.imshow(imgToMatch,cmap='gray')
    ax1.imshow(bestMatch,cmap='gray')
    
