#coding=utf-8
import color_descriptor
import structure_descriptor
import searcher
import cv2
import os 

def find_name(queryImage):
    idealBins = (8, 12, 3)
    idealDimension = (16, 16)

    colorDescriptor = color_descriptor.ColorDescriptor(idealBins)#掩模处理后的直方图
    structureDescriptor = structure_descriptor.StructureDescriptor(idealDimension)#HSV色彩空间的矩阵
    #queryImage = cv2.imread("query.jpg")
    colorIndexPath =os.path.abspath("colorindex")
    structureIndexPath =os.path.abspath("structureindex")

    queryFeatures = colorDescriptor.describe(queryImage)#掩模处理后的直方图
    queryStructures = structureDescriptor.describe(queryImage)#HSV色彩空间的矩阵

    imageSearcher = searcher.Searcher(colorIndexPath, structureIndexPath)
    searchResults = imageSearcher.search(queryFeatures, queryStructures)
    result=[]#图片名称所在的列表
    for imageName, score in searchResults:
        result.append(imageName)
    return result
