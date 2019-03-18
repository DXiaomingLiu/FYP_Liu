from ImaGene import ImaFile
import numpy as np

#run -i ImaGene.py
myfile = ImaFile(simulations_folder='Test_Simulations_3_B',
                 nr_samples=5, model_name='Marth-3epoch-CEU')
mygene = myfile.read_simulations(parameter_name='selection_coeff_hetero', max_nrepl=2000)

mygene.summary()

for sel in mygene.classes:
    print(sel)
    mygene.plot(np.where(mygene.targets == sel)[0][0])
mygene.summary()