# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 17:02:47 2020

@author: tobias.grab
"""

from skimage.transform import downscale_local_mean
import keras
from keras.layers import Input, Dense, Conv2D, MaxPooling2D, UpSampling2D, BatchNormalization, Flatten, Reshape
from keras.models import Model
from keras import backend as K
from keras.callbacks import EarlyStopping
from keras.callbacks import ModelCheckpoint
import tensorflow as tf
from skimage import exposure
import matplotlib.pyplot as plt
import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
from os import listdir
import cv2
import numpy as np
from scipy import spatial

if __name__ == "__main__":
    
    data_path=r'C:\Users\tobias.grab\switchdrive\Schule\datax\projekt\database'
    files=listdir(data_path)
    nrOfFiles=len(files)
    shrinkFactor=10
    createDataset=1
    trainModel=0
    shape0=int(1200/shrinkFactor)
    shape1=int(1600/shrinkFactor)
    
    #A good val loss here is about 0.01
    input_img = Input(shape=(shape0, shape1, 1))
    x = Conv2D(16, (3, 3), activation='relu', padding='same')(input_img)
    x = MaxPooling2D((2, 2), padding='same')(x)
    x = Conv2D(8, (3, 3), activation='relu', padding='same')(x)
    x = MaxPooling2D((2, 2), padding='same')(x)
    x = Conv2D(8, (3, 3), activation='relu', padding='same')(x)
    x = MaxPooling2D((2, 2), padding='same')(x)
    encoded1 = Conv2D(1,(3,3),activation='relu', padding='same')(x)
    encoded = Flatten()(encoded1)

    # x= Reshape((15,20,1))(encoded)
    x = Conv2D(8, (3, 3), activation='relu', padding='same')(encoded1)
    x = UpSampling2D((2, 2))(x)
    x = Conv2D(8, (3, 3), activation='relu', padding='same')(x)
    x = UpSampling2D((2, 2))(x)
    x = Conv2D(16, (3, 3), activation='relu', padding='same')(x)
    x = UpSampling2D((2, 2))(x)
    decoded = Conv2D(1, (3, 3),activation='relu', padding='same')(x)
    
    autoencoder = Model(input_img, decoded)
    autoencoder.compile(optimizer='adam', loss="msle")
    
    if createDataset==True:
        images=[]
        for file in files:
            images.append(downscale_local_mean(cv2.imread(data_path+'\\'+file,0),(shrinkFactor,shrinkFactor)))
            
        images = [exposure.equalize_hist(i) for i in images]
        images=[i.astype('float32') for i in images]
        
        x_all= np.array(images[:])
        x_train = np.array(images[:350])
        x_test = np.array(images[350:])
        x_all = np.reshape(x_all, (len(x_all), shape0, shape1, 1))
        x_train = np.reshape(x_train, (len(x_train), shape0, shape1, 1))
        x_test = np.reshape(x_test, (len(x_test), shape0, shape1, 1))
    
    
    
    if trainModel==1:
        es = EarlyStopping(monitor='val_loss', mode='min', verbose=1, patience=50)
        mc = ModelCheckpoint('best_model.h5', monitor='val_accuracy', mode='max', verbose=1, save_best_only=True)
        history= autoencoder.fit(x_train, x_train,
                        epochs=1000,
                        batch_size=64,
                        shuffle=True,
                        validation_data=(x_test, x_test),
                        callbacks=[es,mc])
        
        decoded_imgs = autoencoder.predict(x_test)
        encoder = Model(input_img, encoded)
        encoded_imgs = encoder.predict(x_all)
        
        plt.plot(history.history['loss'], label='train')
        plt.plot(history.history['val_loss'], label='test')
        plt.legend()
        plt.show()
    else:
        path_to_model=r'C:\Users\tobias.grab\switchdrive\Schule\datax\projekt\kerasModels'
        autoencoder = keras.models.load_model(path_to_model+'\\full_autoencoder.h5')
        encoder= keras.models.load_model(path_to_model+'\\encoder.h5')
        decoded_imgs = autoencoder.predict(x_test)
        encoded_imgs=encoder.predict(x_all)
        
    n = 5
    plt.figure(figsize=(20, 4))
    for i in range(n):
        # display original
        ax = plt.subplot(2, n, i+1)
        plt.imshow(x_test[i].reshape(shape0, shape1))
        plt.gray()

    
        # display reconstruction
        ax = plt.subplot(2, n, i + n +1)
        plt.imshow(decoded_imgs[i].reshape(shape0, shape1))
        plt.gray()

    plt.show()
    
    
    def checkSimilarity(imgToCheck):
        a=[spatial.distance.cosine(imgToCheck,encoded_imgs[i,:]) for i in range(len(files))]
        if min(a)==0:
            exactMatch=files[np.argmin(a)]
            print("The image is exactely:",files[np.argmin(a)])
            a[np.argmin(a)]=1
            closestMatch=files[np.argmin(a)]
            print("The most similar image in the database is:",files[np.argmin(a)])
        return exactMatch,closestMatch
    
    [exact,close]=checkSimilarity(encoded_imgs[316,:])
    
    # plt.figure(figsize=(20, 8))
    # for i in range(1, n + 1):
    #     ax = plt.subplot(1, n, i)
    #     plt.imshow(encoded_imgs[i].reshape((4, 4 * 8)).T)
    #     plt.gray()
    #     ax.get_xaxis().set_visible(False)
    #     ax.get_yaxis().set_visible(False)
    # plt.show()
    
    spatial.distance.cosine(encoded_imgs[316,:],encoded_imgs[20,:])
    
