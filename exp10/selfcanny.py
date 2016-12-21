#!/usr/bin/env python
#
# THe code is my implemention for canny edge detection.
#
__author__ = 'Faldict'
__date__ = '2016-11-30'

import cv2
import numpy as np
from matplotlib import pyplot as plt
from math import pi, atan


def selfCanny(img, minVal, maxVal):
    # Noise Reduction
    gray_img = cv2.GaussianBlur(img, (5, 5), 0)
    # Finding Intensity Gradient of the Image
    s_x = cv2.convertScaleAbs(cv2.Sobel(gray_img, cv2.CV_16S, 1, 0))
    s_y = cv2.convertScaleAbs(cv2.Sobel(gray_img, cv2.CV_16S, 0, 1))
    grd = cv2.addWeighted(s_x, 0.5, s_y, 0.5, 0)
    # Non-maximum Suppression
    m, n = gray_img.shape
    thin_img = np.zeros((m, n))
    for i in range(m):
        for j in range(n):
            theta = atan(s_y[i][j] / (s_x[i][j] + 0.001))
            if theta >= 3 * pi / 8 and j > 0 and j < n - 1:
                grd[i][j] = grd[i][j] if (grd[i][j-1] < grd[i][j] and grd[i][j+1] < grd[i][j]) else 0
            elif theta >= pi / 8 and i > 0 and i < m - 1 and (j > 0) and (j < n - 1):
                grd[i][j] = grd[i][j] if (grd[i+1][j+1] < grd[i][j] and grd[i-1][j-1] < grd[i][j]) else 0
            elif theta >= - pi / 8 and i > 0 and i < m - 1:
                grd[i][j] = grd[i][j] if (grd[i-1][j] < grd[i][j] and grd[i+1][j] < grd[i][j]) else 0
            elif theta >= - 3 * pi / 8 and i > 0 and i < m - 1 and j > 0 and j < n - 1:
                grd[i][j] = grd[i][j] if (grd[i-1][j+1] < grd[i][j] and grd[i+1][j-1] < grd[i][j]) else 0
            elif j > 0 and j < n - 1:
                grd[i][j] = grd[i][j] if (grd[i][j-1] < grd[i][j] and grd[i][j+1] < grd[i][j]) else 0
            else:
                grd[i][j] = 0
    # Hysteresis Thresholding
    for i in range(m):
        for j in range(n):
            if grd[i][j] > maxVal:
                thin_img[i][j] = 255
            elif grd[i][j] < minVal:
                thin_img[i][j] = 0
            elif (i > 0) and (i < m-1) and (j > 0) and (j < n-1):
                thin_img[i][j] = 255 if ((grd[i-1][j-1] > maxVal) or (grd[i-1][j] > maxVal) or (grd[i-1][j+1] > maxVal) or (grd[i][j-1] > maxVal) or (grd[i][j+1] > maxVal) or (grd[i+1][j-1] > maxVal) or (grd[i+1][j] > maxVal) or (grd[i+1][j+1] > maxVal)) else 0
    return thin_img


    # my canny edge detection function
img = cv2.imread("dataset/3.jpg", 0)
self_canny = selfCanny(img, 10, 30)
plt.imshow(self_canny, cmap='gray')
plt.show()
