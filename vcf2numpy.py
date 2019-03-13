###Xiaoming Liu 11/03/2019
#This scirpt takes vcfs of individual windows and
#load them into numpy arrays
###
#Building dependencies

#os.chdir("/FYP_Liu")

import allel
import glob
import numpy as np

#Initializing variables


headers = []
vcfs = glob.glob("./*.vcf")
vcf_num = len(vcfs)

snps = [None]*vcf_num
pos = [None]*vcf_num
for i in range(vcf_num):
    file = vcfs[i]
    item = allel.GenotypeArray(allel.read_vcf(file)['calldata/GT'])
    dim = item.shape
    #print(dim)
    pos[i] = allel.read_vcf(file)['variants/POS']
    snps[i] = item.reshape((dim[0],dim[1]*dim[2],1))
    headers.append(allel.read_vcf_headers(file))
    print(len(headers[0][4]))

snps = np.asarray(snps)
pos = np.asarray(pos)

#print(snps.shape)
#print(snps)
#print(len(np.where(snps > 0)[-1])/(3445*5008))
#print(pos)
#print(pos.shape)

np.save('test_snp.npy',snps)
np.save('test_pos.npy',pos) #maybe use difference at the end?

import matplotlib.pyplot as plt
fig = plt.figure()
ax1 = fig.add_subplot(121)
import matplotlib.cm as cm
dim = snps[0].shape
ax1.imshow(snps[0].reshape(dim[0],dim[1]),cmap=cm.Greys_r)
plt.show()