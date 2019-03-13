###Xiaoming Liu 13/03/2019
#This script uses scikit-allel to subet
#vcf files of polymorphism windows
#by populations (samples beloing to
#a population in a file
###
#Building dependencies
import allel
import glob
import numpy as np
import csv

f = open('PopSampleNames/EUR.csv')
csvread = csv.reader(f, delimiter = '\t')
header = next(csvread)
samples = []
for row in csvread:
    samples.append(row[0])
#print(pops)

for file in glob.glob("./*.vcf"):
    item = allel.read_vcf(file)
    for s in item['samples']:
        if s in samples:
            print(s)
    #print(item)
    print(type(item))
