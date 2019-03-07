###Xiaoming Liu 07/03/2019
#This scirpt takes a csv of SNPs consisting of IDs, chromosomal locations, windows
#and other information and retrieves all SNPs found within these windows using tabix
#from the 1000 genomes projects.
###
#Building dependencies
import csv
import subprocess

#Reading SNP IDs and windows
f = open('SNP_windows.csv')
#CSV column order:
#ID, chr_num, SNP_start, SNP_end, strand, left extremety, and right extremety
csvread = csv.reader(f)
header = next(csvread)
for row in csvread:
    print(row[-2],row[-1])
    item_range =  str(row[1])+':'+str(row[-2])+'-'+str(row[-1])
    direc = 'http://ftp.1000genomes.ebi.ac.uk/vol1/ftp/release/20130502/ALL.chr'+str(row[1])+\
            '.phase3_shapeit2_mvncall_integrated_v5a.20130502.genotypes.vcf.gz'
    tabix_cmd = ['tabix', '-h', direc, item_range]
    print(tabix_cmd)
    tcmd = ['ls', '-t']
    #p = subprocess.check_output(tabix_cmd)
    p = subprocess.Popen(tabix_cmd, shell = True,
                         stdout = subprocess.PIPE,
                         stderr = subprocess.PIPE)
    stdout, stderr = p.communicate()
    print(stdout.decode(), stderr.decode())
#Running tabix in bash to retrieve 1000G SNPs that fall within windows
#p = subprocess.Popen()