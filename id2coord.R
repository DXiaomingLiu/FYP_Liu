###Xiaoming Liu 07/03/2019
###This script takes a list of SNP rs numbers and retrieve thier chromosomal locations
###+ specificying a window around the SNP and other information using biomaRt. Output is in csv

###Establishing dependencies
library(biomaRt)

###
ensembl <- useMart('ENSEMBL_MART_SNP',host="grch37.ensembl.org", 
                   path="/biomart/martservice" ,dataset = 'hsapiens_snp')

#To be changed to read csv of future SNP IDs of interest
#IDs <- c('rs2112347','rs4771122','rs11672660','rs10830963','rs2943645') #Test IDs

###To be uncommented
df_SNP <- read.csv('VariantData/SNPs.csv',header = TRUE)
IDs <- df_SNP$SNP_ID

SNPs <- getBM(attributes = c('refsnp_id','chr_name',
                            'chrom_start',
                            'chrom_end',
                            'chrom_strand'),
             filters = 'snp_filter',values = IDs,
             mart = ensembl, uniqueRows = TRUE)
size = 50000 #50kb window size
SNPs$label <- df_SNP$LABEL
SNPs$left <- SNPs$chrom_start - size
SNPs$right <- SNPs$chrom_end + size

print(SNPs)
write.csv(SNPs, file = "SNP_windows.csv",row.names=FALSE)
#Output SNPs in csv

