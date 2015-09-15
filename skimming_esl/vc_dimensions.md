## Shattering

* A set of points is **shattered** by a classification model if that model can evenly split 0-points from 1-points with no overlap.
* All sets of three points (that are not colinear) can be shattered by a linear model (i.e., a model that is just a line separating space).
* There are sets of four points that can't be shattered by a line, but all sets of four points can be shattered by a quadratic model (e.g., parabola).

![](../images/shattering.png)

## VC Dimensions

* A model has a **VC dimension** that refers to the maximum number of non-colinar points it can shatter.
* The VC dimension of linear models is 3 (because a line can shatter 3 but not 4 points).
