from ImaGene import *
import numpy as np
from keras.models import load_model

mygene = load_imagene(file='Sim1/mygene')
pos_weights = np.load('Sim1/pos_weights.npy')

model = load_model('Models/conv2Ddense.h5')
mynet = ImaNet(name='[C32+P]x3+D64')

for i in range(0,5):

    score = model.fit([mygene.data,pos_weights], mygene.targets, batch_size=32, epochs=1, verbose=1, validation_split=0.10)
    mynet.update_scores(score)

    test_loss, test_acc = model.evaluate([mygene.data,pos_weights], mygene.targets)
    print(test_loss,test_acc)

mynet.plot_train()