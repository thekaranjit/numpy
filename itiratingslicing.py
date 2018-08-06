import numpy as np

import cv2


# Creating array to image

print("++++++++++ Getting as array of image for sample +++++")

im_g = cv2.imread("img.png",0)
print(im_g)

print("+++")

im_g2 = im_g[0:2]

print(im_g2)

print("+++")

im_g3 = im_g[0:2,2:4]

print(im_g3)


print("+++")

for i in im_g:
    print(i)

print("+++")

for i in im_g:
    print(i)


print("+++")

img = np.hstack((im_g,im_g))

print(img)

print("+++")

img1 = np.vstack((im_g,im_g))
print(img1)

print("+++")
lst = np.hsplit(img1,5)

print(lst)

print("+++")
lst2 = np.hsplit(img1,5)

print(lst2)