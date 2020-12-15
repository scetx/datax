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
    data_path=r'C:\Users\tobias.grab\switchdrive\Schule\datax\projekt\output'
    files=listdir(data_path)
    nrOfFiles=len(files)

    # Specify the feature creation algorithm of the opencv library we want to use
    # brisk and akaze seem to work nice for our data. I don't know how they work
    # yet
    ########
    ## TODO: Research the different algorithm and choose a good one
    ########
    alg="akaze"
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
        
    # Read the image we would like to match to one of the images in the database
    # Change the path so it works for you (Images in google Folder 
    # Sampledata/PreprocessedScans_Testdata)
    imgToMatch = cv2.imread(r'C:\Users\tobias.grab\switchdrive\Schule\datax\projekt\test\Testimg2.jpg',0)
    (kps1, descs1) = ftAlg.detectAndCompute(imgToMatch, None)
    # From what I understand, the output of those algorithms are always
    # keypoints (relevant points in the image) as well as a description of
    # each keypoint (using different filters describing the neighborhood)
    # So if we take for example a rotated image of the same object, the
    # describtion should be the same (since it's the same object) and the
    # location of the keypoints change.
    # So by comparing the description of the keypoints of every image of the
    # database with the testimage, we should find the best match
    
    nrOfGoodPerImage=np.zeros([nrOfFiles,1])
    DistPerImage=np.zeros([nrOfFiles,1])
    bauteilnr=0

    #For all images in the database...
    for file in files:
        #Import and calculate the keypoints with the same algorithm as before
        img_from_database = cv2.imread(data_path+'\\'+file,0)    
        (kps2, descs2) = ftAlg.detectAndCompute(img_from_database, None)
    
    
        #Use the bruteforce matcher from the opencv library
        ##########
        ## TODO: Try different matchers
        ##########
        bf = cv2.BFMatcher()
        matches = bf.knnMatch(descs1,descs2,k=2)
        matchesMask = [[0,0] for i in range(len(matches))]
        
        
        # Since some matches are much better than other matches, we have
        # to filter out the good matches. Apparently this can be done using
        # a ratio test described by Lowe in his paper (Not checked yet, so
        # i don't really get how it works)
        for i,(m,n) in enumerate(matches):
            if m.distance < 0.75*n.distance:
                    matchesMask[i]=[1,0]
 

        # In nrOfGoodMatches we get the number of good matches from our test
        # image with the images from our database. The image with the most good
        # matches should be the correct one
        nrOfGoodPerImage[bauteilnr]=np.sum(matchesMask[:])
        bauteilnr=bauteilnr+1
        
        ############
        ## TODO: Use not the number of the good matches, but it's distance.
        ## Hopefully that leads to a better matching
        ############

    #Get the best match and display it
    print("The best match in the database is", files[np.argmax(nrOfGoodPerImage)])
    bestMatch=cv2.imread(data_path+"\\"+files[np.argmax(nrOfGoodPerImage)],0)
    fig,(ax0,ax1)=plt.subplots(ncols=1, nrows=2, figsize=(15,8))
    ax0.imshow(imgToMatch,cmap='gray')
    ax1.imshow(bestMatch,cmap='gray')
    
