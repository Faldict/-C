#!/usr/bin/env python
#
# THe code is my implemention for canny edge detection.
#
__author__ = 'Faldict'
__date__ = '2016-11-30'

import cv2
import numpy as np
from matplotlib import pyplot as plt


def selfCanny(img, minVal, maxVal):
    # Noise Reduction
    gray_img = cv2.GaussianBlur(img, (5, 5), 0)
    # Finding Intensity Gradient of the Image
    s_x = cv2.convertScaleAbs(cv2.Sobel(gray_img, cv2.CV_16S, 1, 0))
    s_y = cv2.convertScaleAbs(cv2.Sobel(gray_img, cv2.CV_16S, 0, 1))
    grd = np.add(np.square(s_x), np.square(s_y))
    # Non-maximum Suppression
    m, n = gray_img.shape
    print m, n
    thin_img = np.zeros((m, n))
    for i in range(m):
        for j in range(n):
            theta = s_y[i][j] / s_x[i][j]
            if abs(theta) == 1 & i > 0 & i < m - 1:
                thin_img[i][j] = gray_img[i][j] * (gray_img[i-1][j] < gray_img[i][j] & gray_img[i+1][j] < gray_img[i][j])
            elif theta == 0 & j > 0 & j < n - 1:
                thin_img[i][j] = gray_img[i][j] * (gray_img[i][j-1] < gray_img[i][j] & gray_img[i][j+1] < gray_img[i][j])
            elif theta > 0:
                thin_img[i][j] = gray_img[i][j] * (gray_img[i+1][j+1] < gray_img[i][j] & gray_img[i-1][j-1] < gray_img[i][j])
            elif theta < 0:
                thin_img[i][j] = gray_img[i][j] * (gray_img[i-1][j+1] < gray_img[i][j] & gray_img[i+1][j-1] < gray_img[i][j])
            else:
                thin_img[i][j] = gray_img[i][j]
    # Hysteresis Thresholding
    for num in thin_img.flat:
        if num > maxVal:
            num = 1
        elif num < minVal:
            num = 0
    return thin_img

    # my canny edge detection function
img = cv2.imread("3.jpg", 0)
self_canny = selfCanny(img, 50, 200)
plt.imshow(self_canny, cmap='gray')
plt.show()