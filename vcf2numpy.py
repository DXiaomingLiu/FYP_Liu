###Xiaoming Liu 07/03/2019
#This scirpt takes vcfs of individual windows and
#load them into numpy arrays
###
#Building dependencies
import allel
import glob
#os.chdir("/FYP_Liu")
vcfs = []
for file in glob.glob("./*.vcf"):
    vcfs.append(allel.read_vcf(file))

#print(vcfs[0]['samples'])
#print(type(vcfs[0]))

gf = allel.GenotypeArray(vcfs[0]['calldata/GT'])
print(gf)

def plot_ld(gn, title):
    m = allel.rogers_huff_r(gn) ** 2
    ax = allel.plot_pairwise_ld(m)
    ax.set_title(title)

gn = gf.to_n_alt()

print(gn)
p = plot_ld(gn[:1000], 'Figure 1. Pairwise LD.')
print(p)
