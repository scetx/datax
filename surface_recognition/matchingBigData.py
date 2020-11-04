from skimage.transform import downscale_local_mean
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
from sklearn.model_selection import train_test_split
import random



def createAutoencoder():
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
    autoencoder= Model(input_img, decoded)
    encoder = Model(input_img, encoded)
    return autoencoder, encoder
    
def checkSimilarity(imgToCheck):
        a=[spatial.distance.cosine(imgToCheck,encoded_imgs[i,:]) for i in range(len(files))]
        if min(a)==0:
            exactMatch=files[np.argmin(a)]
            print("The image is exactely:",files[np.argmin(a)])
            a[np.argmin(a)]=1
            closestMatch=files[np.argmin(a)]
            print("The most similar image in the database is:",files[np.argmin(a)])
        return exactMatch,closestMatch




if __name__ == "__main__":
    
    data_path=r'C:\Users\tobias.grab\IWK_data\artificialVisual'
    files=listdir(data_path)
    nrOfFiles=len(files)
    createDataset=False
    nrOfImages=10000
    trainModel=True
    shape0=120
    shape1=160
    

    if createDataset==True:
        images=[]
        for file in files:
            images.append(cv2.imread(data_path+'\\'+file,0).astype('float32')/255)
        random.seed(1)    
        x_train, x_test = train_test_split(np.reshape(np.array(random.sample(images,nrOfImages)), (nrOfImages, shape0, shape1, 1)), test_size=0.1)
        np.save(r'C:\Users\tobias.grab\switchdrive\Schule\datax\projekt\x_train.npy',x_train)
        np.save(r'C:\Users\tobias.grab\switchdrive\Schule\datax\projekt\x_test.npy',x_test)
        
    else:
        x_train=np.load(r'C:\Users\tobias.grab\switchdrive\Schule\datax\projekt\x_train.npy')
        x_test=np.load(r'C:\Users\tobias.grab\switchdrive\Schule\datax\projekt\x_test.npy')
    

    if trainModel==True:
        autoencoder,encoder = createAutoencoder()
        autoencoder.compile(optimizer='adam', loss="msle")
        es = EarlyStopping(monitor='val_loss', mode='min', verbose=1, patience=5)
        mc = ModelCheckpoint('best_model.h5', monitor='val_accuracy', mode='max', verbose=1, save_best_only=True)
        history= autoencoder.fit(x_train, x_train,
                        epochs=100,
                        batch_size=128,
                        shuffle=True,
                        validation_data=(x_test, x_test),
                        callbacks=[es,mc])
        
        decoded_imgs = autoencoder.predict(x_test[:10,:,:,:])
        # encoded_imgs = encoder.predict(x_test)
        
        plt.plot(history.history['loss'], label='train')
        plt.plot(history.history['val_loss'], label='test')
        plt.legend()
        plt.show()
        

    
    
    
