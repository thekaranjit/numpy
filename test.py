import numpy as np

import cv2


# Creating array to image

print("++++++++++ Getting as array of image for sample +++++")

im_g1 = cv2.imread("test1.jpg",1) # 0 use rgb

print(im_g1) # getting array from picture as rgb


print("++++++++++ Making array to image++++")


cv2.imwrite("testgenerated.jpg", im_g1)

