<script type="text/x-mathjax-config">
  MathJax.Hub.Config({
    extensions: ["tex2jax.js"],
    jax: ["input/TeX", "output/HTML-CSS"],
    tex2jax: {
      inlineMath: [ ['$','$'], ["\\(","\\)"] ],
      displayMath: [ ['$$','$$'], ["\\[","\\]"] ],
      processEscapes: true
    },
    "HTML-CSS": { availableFonts: ["TeX"] }
  });
</script>
<script type="text/javascript"
   src="https://cdn.mathjax.org/mathjax/latest/MathJax.js">
</script>
# 实验报告：LSH

###### Class: F1503023
###### Author: 王嘉璐

## 为什么使用LSH

>用Nearest neighbor (NN) 或k-nearest neighbor (KNN)在数据库中检索和输入数据距离最近的1个或k个数据，一般情况下算法复杂度为O(n)（例如暴力搜索），优化情况下可达到O(log n)（例如二叉树搜索），其中n为数据库中的数据量。当数据库很大（即N 很大时），搜索速度很慢。

Hashing的基本思想是按照某种规则（Hash函数）把数据库中的数据分类，对于输入数据，先按照该规则找到相对应的类别，然后在其中进行搜索。由于某类别中的数据量相比全体数据少得多，因此搜索速度大大加快。

## LSH算法及实现

### 图像的表示

数据可以表示成一个d维的整数向量。其中，$ p_i $ 是整数，满足 \\( 0 \leq p _{i} \leq C \\) 这里C是整数的上限。

> 在本实验中，每幅图像用一个12维的颜色直方图表示：把图像分成四份，分别对每一份求三通道颜色直方图，构成一个12维向量p。

在得到12维向量`p`，以后还要对`p`进行正则化处理，使每一个分量都处于`0-1`之间：

$$ p_i = \frac{p _i - p _{min}}{p _{max} - p _{min}} $$

之后对`p`量子化：

```
p_i = 
	| 0 <= p_i <= 0.3     0
	| 0.3 <= p_i <= 0.6   1
	| 0.6 <= p_i <= 1     2
```

这样，每一张图片都有一个对应的向量 $ p_i $

### LSH预处理

对得到的d维向量哈希用 d*C 维Hamming码表示：

> vp = unary(p1)unary(p2)...unary(pd)  
> unary(p) = [1] * p + [0] * (C - p)


选取{0, 1, 2, ... d}的若干个子集，将vp投影到这些子集上便得到了图片的Hash值。代码实现如下：

``` python
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

```

在本实验中d=12, C=2。

### 图片检索

首先对数据集里的图片LSH预处理后得到一个字典，之后对目标图片预处理后在字典中找到hash值相同的图片，构成一个待匹配的子数据集。最后用ORB算子对目标图片和子数据集里的图片匹配。

```
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
    img = cv2.drawMatches(img1, kp1, img3, kp3, matches[:10])
    return img
```

> python-opencv3 开始有 cv2.drawMathces() 函数。我使用的版本暂无，所以我拷贝了一个该函数的实现。

## 实验结果

我用上周的SIFT算法求数据集中与目标图片匹配的图片，耗时大约7秒左右。用本周LSH处理后再用ORB匹配，耗时大约只有0.2s左右。可见LSH可以大大提高图片检索的速度。  

有意思的是，虽然两种方法得到的检索结果相同，但是使用SIFT特征点匹配的准确度更高，而ORB的很多特征点匹配并不是那么的准确。可见，ORB算子提高了速度但是却牺牲了准确率。
