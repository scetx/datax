# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 17:02:47 2020

@author: tobias.grab
"""

from skimage.transform import downscale_local_mean
from keras.layers import Input, Dense, Conv2D, MaxPooling2D, UpSampling2D
from keras.models import Model
from keras import backend as K
from skimage import exposure
import matplotlib.pyplot as plt
import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
from os import listdir
import cv2
import numpy as np

if __name__ == "__main__":
    
    data_path=r'C:\Users\tobias.grab\switchdrive\Schule\datax\projekt\database'
    files=listdir(data_path)
    nrOfFiles=len(files)
    shrinkFactor=5
    createDataset=1
    trainModel=1
    
    input_img = Input(shape=(240, 320, 1))
    
    x = Conv2D(16, (5, 5), activation='relu', padding='same')(input_img)
    x = MaxPooling2D((2, 2), padding='same')(x)
    x = Conv2D(8, (5, 5), activation='relu', padding='same')(x)
    x = MaxPooling2D((2, 2), padding='same')(x)
    x = Conv2D(8, (3, 3), activation='relu', padding='same')(x)
    x = MaxPooling2D((2, 2), padding='same')(x)
    x = Conv2D(8, (3, 3), activation='relu', padding='same')(x)
    encoded = MaxPooling2D((2, 2), padding='same')(x)
    
    #At this point, we have a low dimensional representation
    
    x = Conv2D(8, (3, 3), activation='relu', padding='same')(encoded)
    x = UpSampling2D((2, 2))(x)
    x = Conv2D(8, (3, 3), activation='relu', padding='same')(x)
    x = UpSampling2D((2, 2))(x)
    x = Conv2D(8, (5, 5), activation='relu', padding='same')(x)
    x = UpSampling2D((2, 2))(x)
    x = Conv2D(16, (5, 5), activation='relu', padding='same')(x)
    x = UpSampling2D((2, 2))(x)
    decoded = Conv2D(1, (3, 3), activation='sigmoid', padding='same')(x)
    
    autoencoder = Model(input_img, decoded)
    autoencoder.compile(optimizer='adadelta', loss='binary_crossentropy')
    
    if createDataset==True:
        images=[]
        for file in files:
            images.append(downscale_local_mean(cv2.imread(data_path+'\\'+file,0),(shrinkFactor,shrinkFactor)))
            
        images = [exposure.equalize_hist(i) for i in images]
        images=[i.astype('float32') for i in images]
        
        x_train = np.array(images[:350])
        x_test = np.array(images[350:])
        x_train = np.reshape(x_train, (len(x_train), 240, 320, 1))
        x_test = np.reshape(x_test, (len(x_test), 240, 320, 1))
    
    if trainModel==1:
        autoencoder.fit(x_train, x_train,
                        epochs=50,
                        batch_size=32,
                        shuffle=True,
                        validation_data=(x_test, x_test),
                        callbacks=[])
        
        decoded_imgs = autoencoder.predict(x_test)
        encoder = Model(input_img, encoded)
        encoded_imgs = encoder.predict(x_test)
        
    n = 5
    plt.figure(figsize=(20, 4))
    for i in range(n):
        # display original
        ax = plt.subplot(2, n, i+1)
        plt.imshow(x_test[i].reshape(240, 320))
        plt.gray()

    
        # display reconstruction
        ax = plt.subplot(2, n, i + n +1)
        plt.imshow(decoded_imgs[i].reshape(240, 320))
        plt.gray()

    plt.show()
    
    # plt.figure(figsize=(20, 8))
    # for i in range(1, n + 1):
    #     ax = plt.subplot(1, n, i)
    #     plt.imshow(encoded_imgs[i].reshape((4, 4 * 8)).T)
    #     plt.gray()
    #     ax.get_xaxis().set_visible(False)
    #     ax.get_yaxis().set_visible(False)
    # plt.show()

