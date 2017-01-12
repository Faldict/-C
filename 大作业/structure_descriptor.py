#coding=utf-8
import cv2

class StructureDescriptor:
    __slot__ = ["dimension"]
    def __init__(self, dimension):
        self.dimension = dimension
    def describe(self, image):
        image = cv2.resize(image, self.dimension, interpolation=cv2.INTER_CUBIC)#修改为统一尺寸
        # image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)    #转化为HSV空间
        return image
