from keras import models, layers, regularizers
model = models.Sequential()
model.add(layers.Conv2D(16, (6,6,),(1,1),
                        kernel_regularizer= regularizers.l2(0.0001),
                        activation='relu',
                        padding='same',
                        input_shape = (64,64,1)))