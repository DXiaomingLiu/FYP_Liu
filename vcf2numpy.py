###Xiaoming Liu 11/03/2019
#This scirpt takes vcfs of individual windows and
#load them into numpy arrays
###
#Building dependencies

#os.chdir("/FYP_Liu")

import allel
import glob
import numpy as np
import matplotlib.pyplot as plt
#Initializing variables


headers = []
vcfs = glob.glob("VcfData/./*.vcf")
vcf_num = len(vcfs)

snps = [None]*vcf_num
pos = [None]*vcf_num


for i in range(vcf_num):
    print(vcfs[i])
    headers.append(allel.read_vcf_headers(vcfs[i]))
    file = allel.read_vcf(vcfs[i])
    gt = allel.GenotypeArray(file['calldata/GT'])
    dim = gt.shape
    print(gt[0,0,0])
    alt = file['variants/ALT']
    ref = file['variants/REF']

    print(dim,alt.shape,ref.shape)
    #print(file['variants/numalt'])

    print(alt)
    allel_to_color ={'A':(255/2,255/2,0),'C':(0,255/2,255/2),'G':(255/2,0,255/2),'T':(255/2,255/2,255/2)}
    INDEL = (255, 255, 255)

    colour_gt = np.zeros((dim[0],dim[1]))
    for y in range(dim[0]): #for each snp
        for x in range(dim[1]): #in each individual
            for allel in range(2): #for each chromosome
                gt_index = gt[y][x][allel]
                if gt_index: #0,1,2... corresponding to ref and alternative alleles in that order
                    nt = alt[y][gt_index-1] #-1 because starting with the first alternative allele (1-1=0 - first alt allele)
                else:
                    nt = ref[y]
                channel = {allel_to_color[nt] if len(nt)==1 else INDEL}
                gt[y][x][allel] = channel



    snps[i] = gt.reshape((dim[0],dim[1]*dim[2],1))
    pos[i] = file['variants/POS']

    snp_im = gt.reshape((dim[0],dim[1]*dim[2]))
    plt.imshow(snp_im)
    plt.savefig('ImageData/Window_'+str(i))

    print('file finished')
    #print(len(headers[0][4]))

snps = np.asarray(snps)
pos = np.asarray(pos)

#print(snps.shape)
#print(snps)
#print(len(np.where(snps > 0)[-1])/(3445*5008))
#print(pos)
#print(pos.shape)

np.save('NumpyData/test_snp.npy',snps)
np.save('NumpyData/test_pos.npy',pos) #maybe use difference at the end?


fig = plt.figure()
ax1 = fig.add_subplot(121)
import matplotlib.cm as cm
dim = snps[0].shape
#ax1.imshow(snps[0].reshape(dim[0],dim[1]),cmap=cm.Greys_r)
#plt.show()