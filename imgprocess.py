###Xiaoming Liu 51/03/2019
#This scirpt takes png images of SNP windows
#of different sizes and resizes them into
#images of the same size
#Building dependencies
import glob
from skimage.io import imread
from skimage.io import imsave
from skimage.transform import resize

file_names = glob.glob('ImageData/*.png')
file_num = len(file_names)
imgs = [None] * file_num
imgs_rescaled = [None] * file_num

for i in range(file_num):
    img = imread(file_names[i])
    img = resize(img, (64,64), anti_aliasing=True)
    imsave('ImageData/Rescaled/rescaled_window'+str(i)+'.png',img)
    imgs[i] = img

#glob.glob()
print(len(imgs))
print(imgs[0].shape)
print(imgs[0])