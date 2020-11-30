### THIS FILE DESCRIBES HOW WE DESIGNED AND
## TRAINED THE MODEL


#IMPORTS

import matplotlib.pyplot as plt
import numpy as np
import os
import tensorflow as tf
from tensorflow.keras import optimizers, callbacks
from tensorflow.keras import Sequential
from tensorflow.keras import layers
from tensorflow.keras.models import Model
from tensorflow.keras.preprocessing.image import ImageDataGenerator

#LOADING & PREPROCESSING TRAINING & VALDATION DATA

from google.colab import drive
drive.mount('/content/gdrive')
os.chdir("/content/gdrive/MyDrive/Apollo_20")


datagen= ImageDataGenerator(
    brightness_range = (-250, 250),
    rescale=1./255,
    horizontal_flip = True,
    vertical_flip = True,
    rotation_range = 20,
    validation_split=0.2) # data preprocessing & augmentation

BATCH_SIZE = 32
IMG_SIZE = (256, 256)

#Training data
train_generator = datagen.flow_from_directory(
        'MAIN',  # Main_folder
        target_size=IMG_SIZE,
        batch_size=BATCH_SIZE,
        class_mode="categorical",
        subset="training")

#Validation data
val_generator = datagen.flow_from_directory(
        'MAIN',
        target_size=IMG_SIZE,
        batch_size=BATCH_SIZE,
        class_mode="categorical",
        subset="validation")

#MODEL ARCHITECTURE

IMG_SHAPE = IMG_SIZE + (3,)
base_model = tf.keras.applications.MobileNetV2(input_shape=IMG_SHAPE, include_top=False, weights='imagenet')

base_model.trainable = False

x = base_model.output
x = layers.GlobalAveragePooling2D()(x)
x = layers.Dropout(0.3)(x)
pred = layers.Dense(256, activation = "relu")(x)
x = layers.Dropout(0.3)(x)

pred = layers.Dense(3, activation = "softmax")(x)

model_2 = Model(inputs = base_model.input , outputs = pred)

#OPTIMIZER
adam_opt = optimizers.Adam(learning_rate=base_learning_rate, beta_1=0.9, beta_2=0.999, amsgrad = False)

#COMPILING MODEL
model_2.compile(optimizer=adam_opt,
              loss= "categorical_crossentropy",
              metrics=['accuracy'])

#TRAINING MODEL
es = callbacks.EarlyStopping(patience=10, restore_best_weights=True)

lr = callbacks.ReduceLROnPlateau(monitor='val_loss', factor=0.1, patience=3)

history = model_2.fit(train_generator,
                    epochs=100,
                    batch_size=32,
                    validation_data = val_generator,
                    callbacks = [es, lr])

#SAVING MODEL
model_2.save("saved_model.h5")
#This is saved in the current directory










