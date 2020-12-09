import cv2
import matchingAlgos
from os import listdir
import pandas as pd
import numpy as np


if __name__ == "__main__":
    
    implemented_algos=["sift","surf","brisk","akaze","kaze","autoencoder","invariant autoencoder"]
    # implemented_algos=["sift"]
    # alg="autoencoder"
    top_k=10
    path_testimgs=r"C:\Users\tobias.grab\IWK_data\test_testimgs3"
    test_files=listdir(path_testimgs)
    test_imgs=[cv2.imread(path_testimgs + "\\" + filename,0) for ind,filename in enumerate(test_files)]
    # test_imgs=test_imgs[:2]
    
    
    best_matches_perAlg=[]
    time_per_alg=[]
    avg_score=[]
    
    for alg in implemented_algos:
        best_matches=[]
        for ind, test_img in enumerate(test_imgs):
            name_testimg=test_files[ind]
            names_testimg = [name_testimg for x in range(len(test_files))]
            names_testimg = pd.DataFrame(names_testimg,columns=["name_testimg"])
            
            matches,avg_score=matchingAlgos.getBestMatches(alg,test_img,top_k)
            
            confidence_score=pd.DataFrame(np.array(matches["score"]/max(matches["score"])),columns=["confidence"])
            if alg=="autoencoder":
                confidence_score=pd.DataFrame(np.array(1-matches["score"]/avg_score),columns=["confidence"])
                
            avg_score=pd.DataFrame(np.ones(top_k)*avg_score,columns=["avg_score"])
            
            
            matches=matches.join([names_testimg,confidence_score,avg_score])
            
            
            isMatch=np.array([matches.name[i][0:9]==matches.name_testimg[i][0:9] for i in range(top_k)])
            isMatch=pd.DataFrame(isMatch,columns=["isMatch"])
            matches=matches.join([isMatch])
            
            
            best_matches.append(matches)
        best_matches_perAlg.append(best_matches)
    
    