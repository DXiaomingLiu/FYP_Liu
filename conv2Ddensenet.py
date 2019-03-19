from keras import layers, Input, regularizers, Model
lambda_l2 = 0.0001

ht_input = Input(shape = (128,128,1), dtype ='float32', name = 'ht')

x = layers.Conv2D(filters = 256,kernel_size = (3,3), activation = 'relu',
                  kernel_regularizer= regularizers.l2(lambda_l2),
                  input_shape=(128, 128, 1))(ht_input)
x = layers.AveragePooling2D(pool_size=(2,2))(x)

for i in range(0,4):
    x = layers.Conv2D(filters = 256,kernel_size = (2,2), activation = 'relu', kernel_regularizer= regularizers.l2(lambda_l2))(x)
    x = layers.AveragePooling2D(pool_size=(2,2))(x)

x = layers.Flatten()(x)

pos_input = Input(shape = (128,), dtype = 'float32', name = 'pos')

y = layers.Dense(64, activation = 'relu', kernel_regularizer = regularizers.l2(lambda_l2)) (pos_input)
for i in range(0,4):
    y = layers.Dense(64, activation='relu', kernel_regularizer=regularizers.l2(lambda_l2))(y)

output = layers.concatenate([x,y],axis=-1)
output = layers.Dense(64,activation='relu',kernel_regularizer=regularizers.l2(lambda_l2))(output)
sel = layers.Dense(1,activation = 'sigmoid')(output)


model = Model(inputs=(ht_input,pos_input), outputs = sel)

model.compile(optimizer='rmsprop',
              loss='binary_crossentropy',
              metrics=['accuracy'])

print(model.summary())

from keras.utils import plot_model
plot_model(model, to_file='Models/conv2Ddense_flow.png')

model.save('Models/conv2Ddense.h5')