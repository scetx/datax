# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 17:02:47 2020

@author: tobias.grab
"""
from skimage.transform import rotate
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
import tensorflow_addons as tfa

if __name__ == "__main__":
    
    data_path=r'C:\Users\tobias.grab\switchdrive\Schule\datax\projekt\database'
    # data_path=r"C:\Users\tobias.grab\IWK_data\test"
    
    files=listdir(data_path)
    nrOfFiles=len(files)
    shrinkFactor=10
    createDataset=True
    trainModel=True
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
    
    LOSS=tf.keras.losses.cosine_similarity
    autoencoder = Model(input_img, decoded)
    autoencoder.compile(optimizer='adam', loss="mse")
    
    if createDataset==True:
        images=[]
        for file in files:
            images.append(downscale_local_mean(cv2.imread(data_path+'\\'+file,0),(shrinkFactor,shrinkFactor)))
            # images.append(cv2.imread(data_path+'\\'+file,0))
            
        images = [exposure.equalize_hist(i) for i in images]
        images=[i.astype('float32') for i in images]
        
        x_all= np.array(images[:])
        y_all= np.concatenate((x_all,x_all),axis=0)
        x_all= np.concatenate((x_all,x_all[:,::-1,::-1]),axis=0)
        x_train = np.array(images[:350])
        y_train=np.concatenate((x_train,x_train),axis=0)
        x_train= np.concatenate((x_train,x_train[:,::-1,::-1]),axis=0)
        x_test = np.array(images[350:])
        y_test=np.concatenate((x_test,x_test),axis=0)
        x_test= np.concatenate((x_test,x_test[:,::-1,::-1]),axis=0)
        
        x_all = np.reshape(x_all, (len(x_all), shape0, shape1, 1))
        x_train = np.reshape(x_train, (len(x_train), shape0, shape1, 1))
        x_test = np.reshape(x_test, (len(x_test), shape0, shape1, 1))
        y_all = np.reshape(y_all, (len(y_all), shape0, shape1, 1))
        y_train = np.reshape(y_train, (len(y_train), shape0, shape1, 1))
        y_test = np.reshape(y_test, (len(y_test), shape0, shape1, 1))
    
    
    
    if trainModel==1:
        es = EarlyStopping(monitor='val_loss', mode='min', verbose=1, patience=10)
        mc = ModelCheckpoint('invariant_autoencoder.h5', monitor='val_accuracy', mode='max', verbose=1, save_best_only=True)
        history= autoencoder.fit(x_train, y_train,
                        epochs=500,
                        batch_size=128,
                        shuffle=True,
                        validation_data=(x_test, y_test),
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
    
    spatial.distance.cosine(encoded_imgs[316,:],encoded_imgs[20,:])
    
