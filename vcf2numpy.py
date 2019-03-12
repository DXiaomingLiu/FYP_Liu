###Xiaoming Liu 11/03/2019
#This scirpt takes vcfs of individual windows and
#load them into numpy arrays
###
#Building dependencies
import allel
import glob
import numpy as np
#os.chdir("/FYP_Liu")
snps = []
pos = []
headers = []
for file in glob.glob("./*.vcf"):
    item = allel.GenotypeArray(allel.read_vcf(file)['calldata/GT'])
    dim = item.shape
    print(dim)
    pos.append(allel.read_vcf(file)['variants/POS'])
    snps.append(item.reshape(dim[0],dim[1]*dim[2],1))
    headers.append(allel.read_vcf_headers(file))

    print(len(headers[0][4]))

#print(vcfs[0]['samples'])
#print(type(vcfs[0]))
#print(headers[0][4])
#print(type(headers[0]))

#gfs = np.zeros(len(vcfs),len(vcfs[0]))
#gf = allel.GenotypeArray(vcfs[0]['calldata/GT'])
#print(gf)
#for i in range(len(vcfs)):
#    vcfs[i] = allel.GenotypeArray(vcfs[0]['calldata/GT']).to_n_alt()


def plot_ld(gn, title):
    m = allel.rogers_huff_r(gn) ** 2
    ax = allel.plot_pairwise_ld(m)
    ax.set_title(title)

#gn = gf.to_n_alt()

#print(gn)
#print(gn.shape)
#print(type(gn))
#p = plot_ld(gn[:1000], 'Figure 1. Pairwise LD.')
#print(p)
snps = np.asarray(snps)
pos = np.asarray(pos)
print(snps.shape)
print(snps)
print(len(np.where(snps > 0)[-1])/(3445*5008))
print(pos)
print(pos.shape)
np.save('test_snp.npy',snps)
np.save('test_pos.npy',pos)