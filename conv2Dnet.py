from keras import models, layers, regularizers
FILTER_NUM = 32
K_SIZE = (6,6)
STRIDE = (1,1)
SHAPE = (64,64,1)
l2_LAMBDA = 0.0001
P_SIZE = (2,2)
model = models.Sequential()
model.add(layers.Conv2D(FILTER_NUM, kernel_size=K_SIZE,strides=STRIDE,
                        kernel_regularizer= regularizers.l2(l2_LAMBDA),
                        activation='relu',
                        padding='same',
                        input_shape = SHAPE))
model.add(layers.MaxPool2D(pool_size=P_SIZE))

model.add(layers.Conv2D(FILTER_NUM,kernel_size=K_SIZE, strides=STRIDE,
                        kernel_regularizer=regularizers.l2(l2_LAMBDA),
                        activation = 'relu',
                        padding = 'same'))
model.add(layers.MaxPool2D(pool_size=P_SIZE))

model.add(layers.Flatten())
model.add(layers.Dense(32,activation='relu'))
model.add(layers.Dense(5,activation = 'softmax'))

model.compile(optimizer='rmsprop',
              loss = 'categorical_crossentropy',
              metrics=['accuracy'])
###Importing data##
import numpy as np
from scipy import misc
#x_raw = np.load('NumpyData/bw_snp.npy')
#y_raw = np.load('NumpyData/labels.npy')
x_train = np.load()
hist = model.fit(x_train,y_train,batch_size=32,epochs=20,validation_split=0.15)

###Visualising training process###
from matplotlib import rcParams
import matplotlib.pyplot as plt
train_loss = hist.history['loss']
val_loss = hist.history['val_loss']
train_acc = hist.history['acc']
val_acc = hist.history['val_acc']

xc = range(20)
x_axis = np.zeros(len(xc))
for x,i in enumerate(xc):
    x_axis[i] = x+1

rcParams['axes.titlepad'] = 20


