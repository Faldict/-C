#!/usr/bin/env python

import cv2
import numpy as np 
from matplotlib import pyplot as plt

img1_0 = cv2.imread('img1.png', 0)
img1_1 = cv2.imread('img1.png')
img2_0 = cv2.imread('img2.png', 0)
img2_1 = cv2.imread('img2.png')

plt.hist(img1_0.ravel(), 256, [0, 256]); plt.show()
plt.hist(img1_1.ravel(), 256, [0, 256]); plt.show()
plt.hist(img2_0.ravel(), 256, [0, 256]); plt.show()
plt.hist(img2_1.ravel(), 256, [0, 256]); plt.show()
