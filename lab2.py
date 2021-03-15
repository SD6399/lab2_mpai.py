import skimage
from PIL import Image
import numpy as np
from skimage.io import imread, imshow
import cv2
import os
from matplotlib import pyplot as plt
from numpy import array

gmax=255
gmin=0

arr = np.array(skimage.io.imread("D:/dk/university/mpai/lab_2/imgg/07_elaine.tif"))
arr1 = np.array(skimage.io.imread("D:/dk/university/mpai/lab_2/imgg/01_apc.tif"), dtype='uint8')

bb = np.array([])

arr[arr < 127] = 0
arr[arr > 127] = 255

fmax=np.amax(arr1)
fmin=np.amin(arr1)


a=(gmax-gmin)/(fmax-fmin)
b=(gmin*fmax-gmax*fmin)/(fmax-fmin)
print(a,b)

print(arr1)
bb=(arr1*a+b).astype(np.uint8)
print(bb)

plt.subplot(2,2,1)
imshow(arr1)
plt.title("До",size=10)
plt.subplot(2,2,2)
imshow(bb)
plt.title("После",size=10)
plt.show()
# show()
