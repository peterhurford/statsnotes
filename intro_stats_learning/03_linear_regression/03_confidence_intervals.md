## Estimating β^

* β^[0] = mean(*y*) - β^[1] * mean(*x*)
* β^[1] = (Σ{*i*=1 -> *n*}((*x*[*i*] - mean(*x*))(*y*[*i*] - mean(*y*))))/(Σ{*i*=1 -> *n*}((*x*[*i*] - mean(*x*))^2))
* mean(*x*) refers to the **sample mean** of *x*.


## Assessing the Accuracy of β^

* The line given by Y = β[0] + β[1]*X + *e* is the **population regression line**, or the line that most closely resembles the relationship (given perfect data).
* The line given by Y^ = β[0]^ + β[1]^*X is the **least squares line**, or the line that best predicts the relationship using least squares analysis on the data we have.

![](../images/population-regression-line.png)


## Standard Error of β^

* SE(β^[0]) = Var(*e*) * ((1/n) + ((mean(*x*)^2)/(Σ{*i*=1 -> *n*}((*x*[*i*]-mean(*x*))^2))))
* SE(β^[1]) = Var(*e*)/(Σ{*i*=1 -> *n*}((*x*[*i*]-mean(*x*))^2))
* I don't know enough math to figure out why these formulae are the way they are.
* It's cool to see that SE(β^[1]) goes down as the points are more numerous or more spread out.  This makes sense, since we have more leverage to estimate a slope when either or both of these things are the case.
* In general, we don't know Var(*e*), but we can estimate it from the data by using the **residual square error**, which is the square root of the sum of squared residuals divided by *n* - 2, or sqrt(RSS/(n-2)).
* To be strict, we should be talking about SE^(β^[0]) instead of SE(β^[0]) when using RSS as Var(*e*), because we're making a prediction.


## Confidence Intervals

* A **confidence interval** tells you the chance that the true value of A will be inside an interval ranging from A^[1] to A^[2].
* The standard error of β^ can be used to construct confidence intervals.
* There is a approximately a 95% chance that β[1] (the true value) will be contained in the interval [β^[1] - 2*SE(β^[1]), β^[1] + 2*SE(β^[1])].  In other words, this interval is the 95% confidence interval of β^[1].
* The same is also true for β[0].  [β^[0] - 2*SE(β^[0]), β^[0] + 2*SE(β^[0])] is the 95% confidence interval for β[0] and, in other words, β[0] is within plus or minus two standard errors of β^[0] approximately 95% of the time.
* The estimate is only approximate because of limitations of the equaltion itself, because the estimate should vary slightly from 2 based on the number of observations and because it assumes the errors are [Gaussian](https://en.wikipedia.org/wiki/Gaussian_function) (bell-curve shaped).  
