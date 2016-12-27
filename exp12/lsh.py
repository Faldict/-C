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
    for root, _, filenames in os.walk("Dataset"):
        for f in filenames:
            filename = os.path.join(root, f)
            img = cv2.imread(filename)
            dataset.append((process(img), filename))
    return dataset


def drawMatches(img1, kp1, img2, kp2, matches):
    """
    I copy an implementation of cv2.drawMatches as OpenCV 2.4.9
    does not have this function available but it's supported in
    OpenCV 3.0.0

    This function takes in two images with their associated 
    keypoints, as well as a list of DMatch data structure (matches) 
    that contains which keypoints matched in which images.

    An image will be produced where a montage is shown with
    the first image followed by the second image beside it.

    Keypoints are delineated with circles, while lines are connected
    between matching keypoints.

    img1,img2 - Grayscale images
    kp1,kp2 - Detected list of keypoints through any of the OpenCV keypoint 
              detection algorithms
    matches - A list of matches of corresponding keypoints through any
              OpenCV keypoint matching algorithm
    """

    # Create a new output image that concatenates the two images together
    # (a.k.a) a montage
    rows1 = img1.shape[0]
    cols1 = img1.shape[1]
    rows2 = img2.shape[0]
    cols2 = img2.shape[1]

    out = np.zeros((max([rows1,rows2]),cols1+cols2,3), dtype='uint8')

    # Place the first image to the left
    out[:rows1,:cols1] = np.dstack([img1, img1, img1])

    # Place the next image to the right of it
    out[:rows2,cols1:] = np.dstack([img2, img2, img2])

    # For each pair of points we have between both images
    # draw circles, then connect a line between them
    for mat in matches:

        # Get the matching keypoints for each of the images
        img1_idx = mat.queryIdx
        img2_idx = mat.trainIdx

        # x - columns
        # y - rows
        (x1,y1) = kp1[img1_idx].pt
        (x2,y2) = kp2[img2_idx].pt

        # Draw a small circle at both co-ordinates
        # radius 4
        # colour blue
        # thickness = 1
        cv2.circle(out, (int(x1),int(y1)), 4, (255, 0, 0), 1)   
        cv2.circle(out, (int(x2)+cols1,int(y2)), 4, (255, 0, 0), 1)

        # Draw a line in between the two points
        # thickness = 1
        # colour blue
        cv2.line(out, (int(x1),int(y1)), (int(x2)+cols1,int(y2)), (255, 0, 0), 1)

    # Also return the image if you'd like a copy
    return out


def match(tgt, db):
    orb = cv2.ORB()
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    img1 = cv2.imread(tgt, 0)
    kp1, des1 = orb.detectAndCompute(img1, None)

    img3 = None
    kp3 = None
    best = 0

    for d in db:
        img2 = cv2.imread(d, 0)
        kp2, des2 = orb.detectAndCompute(img2, None)
        matches = bf.match(des1, des2)
        if len(matches) > best:
            img3 = img2
            kp3 = kp2
            best = len(matches)
    img = drawMatches(img1, kp1, img3, kp3, matches[:10])
    return img


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
