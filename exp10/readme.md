# Experiment Report 8: Canny Edge Detector

###### Author: 王嘉璐
##### Class: F1503023

## Theory

The *Canny Edge detector* was developed by John F. Canny in 1986. Also known to many as the optmal detector, Canny algorithm. Three main criteria:

- **Low error rate**: Meaning a good detection of only existent edges.
- **Good localization**: The distance between edge pixels detected and real edge pixels have to be minimized.
- **Minimal response**: Only one detector response per edge.

## Algorithm

### 1. Filter out any noise. 

The Gaussian filter is used for this purpose. An example of a Gaussian kernel of `size=5` that might be used is shown below:  

<img src="http://docs.opencv.org/2.4/_images/math/8e268d7b17755d3bc1b321449d1d6de7f807d789.png" alt="K = \dfrac{1}{159}\begin{bmatrix}
          2 &amp; 4 &amp; 5 &amp; 4 &amp; 2 \\
          4 &amp; 9 &amp; 12 &amp; 9 &amp; 4 \\
          5 &amp; 12 &amp; 15 &amp; 12 &amp; 5 \\
          4 &amp; 9 &amp; 12 &amp; 9 &amp; 4 \\
          2 &amp; 4 &amp; 5 &amp; 4 &amp; 2
                  \end{bmatrix}">
 
### 2. Find the intensity gradient of the image.

For this, we follow a procedure analogous to Sobel:

a. Apply a pair of convolution masks in x and y directions:  
	
<img src="http://docs.opencv.org/2.4/_images/math/daf149b9164966d5bdedb03720101683dd851e07.png" alt="G_{x} = \begin{bmatrix}
-1 &amp; 0 &amp; +1  \\
-2 &amp; 0 &amp; +2  \\
-1 &amp; 0 &amp; +1
\end{bmatrix}
G_{y} = \begin{bmatrix}
-1 &amp; -2 &amp; -1  \\
0 &amp; 0 &amp; 0  \\
+1 &amp; +2 &amp; +1
\end{bmatrix}"> 

b. Find the gradient strength and direction with:

<img src="http://docs.opencv.org/2.4/_images/math/4c2af1833fd9f9af4ec5506ff8a83e217ebbe6db.png" alt="\begin{array}{l}
G = \sqrt{ G_{x}^{2} + G_{y}^{2} } \\
\theta = \arctan(\dfrac{ G_{y} }{ G_{x} })
\end{array}">

The direction is rounded to one of four possible angles (namely 0, 45, 90, or 135)

### 3. *Non-maximum suppression* is applied.

This removes pixels that are not considered to be part of an edge. Hence, only thin lines (candidate edges) will remain.

### 4. *Hysteresis*: The final step.

Canny does use two thresholds (upper and lower):

- a. If a pixel gradient is higher than the upper threshold, the pixel is accepted as an edge
- b. If a pixel gradient value is below the lower threshold, then it is rejected.
- c. If the pixel gradient is between the two thresholds, then it will be accepted only if it is connected to a pixel that is above the upper threshold.

Canny recommended a upper lower ratio between 2:1 and 3:1.

## Code

### Gaussian Filter

```
    # Noise Reduction
    gray_img = cv2.GaussianBlur(img, (5, 5), 0)
```

### Sobel Operator

```
    # Finding Intensity Gradient of the Image
    s_x = cv2.convertScaleAbs(cv2.Sobel(gray_img, cv2.CV_16S, 1, 0))
    s_y = cv2.convertScaleAbs(cv2.Sobel(gray_img, cv2.CV_16S, 0, 1))
    grd = cv2.addWeighted(s_x, 0.5, s_y, 0.5, 0)
```

### Non-maximum Suppression

```
    m, n = gray_img.shape
    print m, n
    thin_img = np.zeros((m, n))
    for i in range(m):
        for j in range(n):
            theta = s_y[i][j] / s_x[i][j]
            if (abs(theta) > tan(3 * pi / 8)) and i > 0 and i < m - 1:
                thin_img[i][j] = gray_img[i][j] * (grd[i-1][j] < grd[i][j] and grd[i+1][j] < grd[i][j])
            elif (abs(theta) < tan(pi / 8)) and (j > 0) and (j < n - 1):
                thin_img[i][j] = gray_img[i][j] * (grd[i][j-1] < grd[i][j] and grd[i][j+1] < grd[i][j])
            elif theta > 0:
                thin_img[i][j] = gray_img[i][j] * (grd[i+1][j+1] < grd[i][j] and grd[i-1][j-1] < grd[i][j])
            elif theta < 0:
                thin_img[i][j] = gray_img[i][j] * (grd[i-1][j+1] < grd[i][j] and grd[i+1][j-1] < grd[i][j])
            else:
                thin_img[i][j] = gray_img[i][j]
```

### Hysteresis Thresholding

```
    for i in range(m):
        for j in range(n):
            if grd[i][j] > maxVal:
                thin_img[i][j] = 255
            elif grd[i][j] < minVal:
                thin_img[i][j] = 0
            elif (i > 0) and (i < m-1) and (j > 0) and (j < n-1):
                thin_img[i][j] = 255 if ((grd[i-1][j-1] > maxVal) or (grd[i-1][j] > maxVal) or (grd[i-1][j+1] > maxVal) or (grd[i][j-1] > maxVal) or (grd[i][j+1] > maxVal) or (grd[i+1][j-1] > maxVal) or (grd[i+1][j] > maxVal) or (grd[i+1][j+1] > maxVal)) else 0
```

## Review

- It's better for minVal : maxVal = 1 : 3
- I think the whole process is just like a convolutional neural network.