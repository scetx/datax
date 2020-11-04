from tensorflow import keras
import numpy as np
from scipy import spatial
from os import listdir
import random

def checkSimilarity(imgToCheck):
        a=[spatial.distance.cosine(imgToCheck, encoded_imgs[i,:]) for i in range(len(encoded_imgs))]
        if min(a)==0:
            exactMatch=files[np.argmin(a)]
            print("The image is exactely: x_train NR",np.argmin(a))
            a[np.argmin(a)]=1
            closestMatch=files[np.argmin(a)]
            print("The most similar image in the database is: x_train NR",np.argmin(a))
        return exactMatch,closestMatch

if __name__ == "__main__":
    
    data_path_all=r'C:\Users\tobias.grab\IWK_data\artificialVisual'
    path_to_model=r'C:\Users\tobias.grab\switchdrive\Schule\datax\projekt\kerasModels'
    files=listdir(data_path_all)
    data_path_subset=r'C:\Users\tobias.grab\switchdrive\Schule\datax\projekt'
    importData=False
    
    if importData==True:
        x_train=np.load(data_path_subset +'\\x_train.npy')
        x_test=np.load(data_path_subset +'\\x_test.npy')
        autoencoder = keras.models.load_model(path_to_model+'\\full_autoencoder.h5')
        encoder= keras.models.load_model(path_to_model+'\\encoder.h5')
        encoded_imgs=encoder.predict(x_train)
    
    checkSimilarity(encoded_imgs[0,:])