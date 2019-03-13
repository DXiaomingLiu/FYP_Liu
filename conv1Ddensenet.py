###Xiaoming Liu 12/03/2019
#Using the Keras functional API,
#this scirpt sets up a multi-input model of
#a 1D Convnet branch taking snp genotype as its input
#and a deep neural network branch intaking snp postions
#This model tries to implement the one specified in
#Schrider and colleagues' paper (page 234, 2018)
###
#Building dependencies
from keras import layers, regularizers, Input
import matplotlib.pyplot as plt
import numpy as np

lambda_l2 = 0.0001

pop = 2500
ht_input = Input(shape = (pop*2,), dtype ='float32', name = 'ht')

x = layers.Conv1D(filters = 256,kernel_size = 2, activation = 'relu', kernel_regularizer= regularizers.l2(lambda_l2),input_shape=(30, 1))\
    (ht_input)
x = layers.AveragePooling1D(pool_size=2)(x)

for i in range(0,4):
    x = layers.Conv1D(filters = 256,kernel_size = 2, activation = 'relu', kernel_regularizer= regularizers.l2(lambda_l2))(x)
    x = layers.AveragePooling1D(pool_size=2)(x)
x = layers.Flatten()(x)
x = layers.Dense(units=256, activation='relu')(x)
pos_input = Input(shape = (3500,5008), dtype = 'float32', name = 'pos')
y = layers.Dense(64, activation = 'relu', kernel_regularizer = regularizers.l2(lambda_l2)) (pos_input)
for i in range(0,4):
    y = layers.Dense(64, activation='relu', kernel_regularizer=regularizers.l2(lambda_l2))(y)
branch_conv_dim = x.shape
y = layers.Dense(256, activation='relu')(y)
y = layers.Reshape(branch_conv_dim)(y)
output = layers.concatenate([x,y],axis=-1)

#branch_dense_dim = y.shape
#print(branch_conv_dim,branch_dense_dim)

