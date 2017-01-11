#!/usr/bin/env python

import cv2
import numpy as np
import os
import time
from matplotlib import pyplot as plt


def process(img):
    p = normalize(img)
    vp = vectorize(p)
    lset = [0] * 4
    lset1 = (0, 3, 6, 9, 18, 21)
    lset2 = (1, 2, 4, 6, 15)
    hshs = np.concatenate((shallow(vp, lset1), shallow(vp, lset2)))
    return hshs


def normalize(img):
    p = np.zeros(12)
    h, w, _ = img.shape
    p[0] = np.mean(img[0: h / 2, 0: w / 2, 0])
    p[1] = np.mean(img[0: h / 2, 0: w / 2, 1])
    p[2] = np.mean(img[0: h / 2, 0: w / 2, 2])
    p[3] = np.mean(img[h / 2: h, 0: w / 2, 0])
    p[4] = np.mean(img[h / 2: h, 0: w / 2, 1])
    p[5] = np.mean(img[h / 2: h, 0: w / 2, 2])
    p[6] = np.mean(img[h / 2: h, w / 2: h / 2, 0])
    p[7] = np.mean(img[h / 2: h, w / 2: h / 2, 1])
    p[8] = np.mean(img[h / 2: h, w / 2: h / 2, 2])
    p[9] = np.mean(img[0: h / 2, w / 2: h / 2, 0])
    p[10] = np.mean(img[0: h / 2, w / 2: h / 2, 1])
    p[11] = np.mean(img[0: h / 2, w / 2: h / 2, 2])
    minp = np.amin(p)
    maxp = np.amax(p)
    for i in range(12):
        p[i] = (p[i] - minp) / (maxp - minp)
        if p[i] <= 0.3:
            p[i] = 0
        elif p[i] <= 0.6:
            p[i] = 1
        else:
            p[i] = 2
    return p


def vectorize(p):
    vp = np.zeros(24)
    for i in range(12):
        vp[2 * i: 2 * (i + 1)] = [1] * int(p[i]) + [0] * (2 - int(p[i]))
    return vp


def shallow(vp, lset):
    res = [0] * len(lset)
    for i in range(len(lset)):
        res[i] = vp[lset[i]]
    return res


def build_dataset():
    dataset = []
    for root, _, filenames in os.walk("static/dataset"):
        for f in filenames:
            filename = os.path.join(root, f)
            img = cv2.imread(filename)
            dataset.append((process(img), filename))
    return dataset


def match(tgt, db):
    orb = cv2.ORB()
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    img1 = cv2.imread(tgt, 0)
    kp1, des1 = orb.detectAndCompute(img1, None)

    img3 = None
    kp3 = None
    result = []

    for d in db:
        img2 = cv2.imread(d, 0)
        kp2, des2 = orb.detectAndCompute(img2, None)
        matches = bf.match(des1, des2)
        result.append((d, matches))

    sorted(result, key=lambda r : r[1])
    if len(result) > 10:
        result = result[-1:-11:-1]
    else:
        result = result[::-1]
    for i in len(result):
        result[i] = result[i][0]
    return result


def search_img(target, db):
    tgt = process(cv2.imread(target))
    res = []
    for d in db:
        dist = np.linalg.norm(d[0] - tgt)
        if dist < 0.01:
            res.append(d[1])
    match_result = match(target, res)


def main():
    start_time = time.clock()
    target = "target.jpg"
    tgt = process(cv2.imread(target))
    db = build_dataset()
    res = []
    for d in db:
        dist = np.linalg.norm(d[0] - tgt)
        if dist < 0.01:
            res.append(d[1])
    match_result = match(target, res)
    end_time = time.clock()
    print "Cost time %s" % (end_time - start_time)
    plt.imshow(match_result), plt.show()


if __name__ == '__main__':
    main()
