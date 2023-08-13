import numpy as np
import argparse
import matplotlib.pyplot as plt
import cv2
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import os

def getFusionScore(imagepath):
    print("imagepath :",imagepath)
    
    
    model = Sequential()
    model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(128,128,1)))
    model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))
     
    model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))
     
    model.add(Flatten())
    model.add(Dense(1024, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(12, activation='softmax'))
    model.load_weights('CNN_Weight_model_Fusion.h5')
    
    img = cv2.imread(imagepath)
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    img_AZ = np.expand_dims(np.expand_dims(cv2.resize(gray_image, (128, 128)), -1), 0)
    prediction = model.predict(img_AZ)
    maxindex = int(np.argmax(prediction))
    return maxindex
   
if __name__ == '__main__':
    getFusionScore()                  

