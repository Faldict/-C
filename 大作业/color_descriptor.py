#coding=utf-8
import cv2
import numpy

class ColorDescriptor:
    __slot__ = ["bins"]
    def __init__(self, bins):
        self.bins = bins
    def getHistogram(self, image, mask, isCenter):
        imageHistogram = cv2.calcHist([image], [0, 1, 2], mask, self.bins, [0, 180, 0, 256, 0, 256])#绘制直方图
        imageHistogram = cv2.normalize(imageHistogram, imageHistogram).flatten()#归一一维化
        if isCenter:#中心增加权重
            weight = 5.0
            for index in xrange(len(imageHistogram)):
                imageHistogram[index] *= weight
        return imageHistogram
    def describe(self, image):
        image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        features = []#特征数组
        height, width = image.shape[0], image.shape[1]
        centerX, centerY = int(width * 0.5), int(height * 0.5)#中心点
        segments = [(0, centerX, 0, centerY), (0, centerX, centerY, height), (centerX, width, 0, centerY), (centerX, width, centerY, height)]#四周掩模
        axesX, axesY = int(width * 0.75) / 2, int (height * 0.75) / 2#中心掩模

        ellipseMask = numpy.zeros([height, width], dtype="uint8")
        cv2.ellipse(ellipseMask, (centerX, centerY), (axesX, axesY), 0, 0, 360, 255, -1)#椭圆中心掩模
        for startX, endX, startY, endY in segments:
            cornerMask = numpy.zeros([height, width], dtype="uint8")
            cv2.rectangle(cornerMask, (startX, startY), (endX, endY), 255, -1)#矩形四周掩模
            cornerMask = cv2.subtract(cornerMask, ellipseMask)
            imageHistogram = self.getHistogram(image, cornerMask, False)
            features.append(imageHistogram)
       
        imageHistogram = self.getHistogram(image, ellipseMask, True)
        features.append(imageHistogram)
        # return
        return features
