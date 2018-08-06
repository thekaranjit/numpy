import numpy as np

import cv2

# Creating image to array


print("++++++++++ Getting as Black and White+++++")

im_g = cv2.imread("img.png",0) # 0 use black and white

print(im_g) # getting array from picture

print("++++++++++ Getting as RGB +++++")

im_g2 = cv2.imread("img.png",1) # 0 use rgb

print(im_g2) # getting array from picture as rgb

