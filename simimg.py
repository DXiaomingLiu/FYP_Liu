from ImaGene import ImaFile
import numpy as np

#run -i ImaGene.py
myfile = ImaFile(simulations_folder='simulations_3_Binary_0_20000_10',
                 nr_samples=128, model_name='Marth-3epoch-CEU')
mygene = myfile.read_simulations(parameter_name='selection_coeff_hetero', max_nrepl=2000)

mygene.summary()

for sel in mygene.classes:
    print(sel)
    mygene.plot(np.where(mygene.targets == sel)[0][0])
mygene.summary()
print(mygene.data.shape)