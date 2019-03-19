from ImaGene import *
import numpy as np
from keras.models import load_model

myfile = ImaFile(simulations_folder='Sim1',
                 nr_samples=128, model_name='Marth-3epoch-CEU')
mygene = myfile.read_simulations(parameter_name='selection_coeff_hetero', max_nrepl=2000)

#rnd_idx = get_index_random(mygene)
#mygene.subset(rnd_idx)

mygene.resize((128,128))
mygene.targets = to_binary(mygene.targets)

mygene.save(file='mygene')
model = load_model('Models/conv2Ddense.h5')

pos = mygene.positions



def pos_to_density(positions_list,parts=128):
    length = len(positions_list)
    pos_density_array = np.zeros((length,parts))
    for i in range(length):
        pos_density = np.zeros(parts)
        for position in positions_list[i:]:
            pos_density[(position*parts).astype(int)-1]+=1
        pos_density_array[i] = pos_weights
    return pos_density_array

mynet = ImaNet(name='[C32+P]x3+D64')

pos_density = pos_to_density(mygene.positions,128)
np.save('Sim1/pos_density.npy',pos_weights)
mygene.save(file='Sim1/mygene')

'''
for i in range(0,5):

    score = model.fit([mygene.data,pos_density], mygene.targets, batch_size=32, epochs=1, verbose=1, validation_split=0.10)
    mynet.update_scores(score)

    test_loss, test_acc = model.evaluate([mygene.data,pos_density], mygene.targets)
    print(test_loss,test_acc)

mynet.plot_train()
'''