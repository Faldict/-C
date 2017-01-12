#coding=utf-8
import numpy
import csv
import re

class Searcher:
    __slot__ = ["colorIndexPath", "structureIndexPath"]
    def __init__(self, colorIndexPath, structureIndexPath):
        self.colorIndexPath, self.structureIndexPath = colorIndexPath, structureIndexPath
    def solveColorDistance(self, features, queryFeatures, eps = 1e-5):#求二范数（距离）
        distance = 0.5 * numpy.sum([((a - b) ** 2) / (a + b + eps) for a, b in zip(features, queryFeatures)])
        return distance
    def solveStructureDistance(self, structures, queryStructures, eps = 1e-5):#求二范数（距离）
        distance = 0
        normalizeRatio = 5e3
        for index in xrange(len(queryStructures)):
            for subIndex in xrange(len(queryStructures[index])):
                a = structures[index][subIndex]
                b = queryStructures[index][subIndex]
                distance += (a - b) ** 2 / (a + b + eps)
        return distance / normalizeRatio
    def searchByColor(self, queryFeatures):
        searchResults = {}
        with open(self.colorIndexPath) as indexFile:
            reader = csv.reader(indexFile)#读取索引表
            for line in reader:
                features = []
                for feature in line[1:]:
                    feature = feature.replace("[", "").replace("]", "")#用 代替[ ]
                    feature = re.split("\s+", feature)#以任意多空白字符划分
                    rmlist = []
                    for index, strValue in enumerate(feature):
                        if strValue == "":
                            rmlist.append(index)
                    for _ in xrange(len(rmlist)):#清除空白参数
                        currentIndex = rmlist[-1]
                        rmlist.pop()
                        del feature[currentIndex]
                    feature = [float(eachValue) for eachValue in feature]
                    features.append(feature)
                distance = self.solveColorDistance(features, queryFeatures)
                searchResults[line[0]] = distance#图片名字为键，距离为值的字典
            indexFile.close()
        return searchResults
    def transformRawQuery(self, rawQueryStructures):#图像转化为特征向量形式
        queryStructures = []
        for substructure in rawQueryStructures:
            structure = []
            for line in substructure:
                for tripleColor in line:
                    structure.append(float(tripleColor))
            queryStructures.append(structure)
        return queryStructures
    def searchByStructure(self, rawQueryStructures):
        searchResults = {}
        queryStructures = self.transformRawQuery(rawQueryStructures)
        with open(self.structureIndexPath) as indexFile:
            reader = csv.reader(indexFile)
            for line in reader:
                structures = []
                for structure in line[1:]:
                    structure = structure.replace("[", "").replace("]", "")
                    structure = re.split("\s+", structure)
                    if structure[0] == "":
                        structure = structure[1:]
                    structure = [float(eachValue) for eachValue in structure]
                    structures.append(structure)
                distance = self.solveStructureDistance(structures, queryStructures)
                searchResults[line[0]] = distance
            indexFile.close()
        return searchResults
    def search(self, queryFeatures, rawQueryStructures, limit = 10):#综合两种匹配返回前limit个结果
        featureResults = self.searchByColor(queryFeatures)
        structureResults = self.searchByStructure(rawQueryStructures)
        results = {}
        for key, value in featureResults.iteritems():
            results[key] = value + structureResults[key]
        results = sorted(results.iteritems(), key = lambda item: item[1], reverse = False)#以综合分值排序
        return results[ : limit]
