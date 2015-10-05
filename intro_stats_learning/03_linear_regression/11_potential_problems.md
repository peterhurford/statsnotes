## Potential Problems in Fitting a Linear Model

Six key problems:

* Non-linearity of response-predictor relationships
* Correlation of error terms
* Non-constant variance of error terms
* Outliers
* High-leverage points
* Colinearity


## Dealing with Non-Linearity

* The linear model assumes there is a straight-line relationship between the predictors and the response.  If this is false, the predictive power of the model is greatly reduced.  This is called **non-linearity**.
* To detect non-linearity, we look at **residual plots**, or plotting the residuals against the predicted values of Y^[*i*].  A problem with non-linearity will manifest itself as a relationship between the residuals and Y^[*i*], which will be shown in the residual plot.
* The best way to correct this problem is to either (a) switch to a different method of prediction other than the linear model or (b) add additional variables that act as transformations of various predictors, such as log(X), sqrt(X), or X^2.

![](../images/residual-plots.png)

On the left, there is no relationship between the resudial and the variable, which means the linear relationship looks correct.  However, on the right graph, there is a strong linear relationship between the residuals and the variable, which suggests the assumption of a linear relationship between the variable and the DV is not correct.


## Dealing with Correlated Error Terms

* Remember that Y = β[0] + β[1]X[1] + β[2]X[2] really means Y = β[0] + β[1]X[1] + β[2]X[2] + *e*, where *e* is a set of error terms.  *e*[*i*] is the error term for an individual observation, coming from Y[*i*] = β[0,*i*] + β[1,*i*]X[1,*i*] + β[2,*i*]X[2,*i*] + *e*[*i*].
* If *e*[*i*] for various *i* are correlated within *e*, then many of the assumptions of linear models are broken, leading to wrong calculations of statistical significance and wrong confidence intervals.
* For example, consider what would happen if we accidentally duplicated our data, so data and error terms are identical in pairs.  This would lead us to calculate statistical significance and confidence intervals with a sample size of 2*n*, when we should have calculated with just *n*.
* Correlated error terms can exist when sampling from correlated populations (e.g., multiple members of the same family are sampled) or in **time-series data**, where samples at certain points in time are frequently correlated with the same sample taken just before.
* A way to detect correlations of residuals in time-series data is to plot the residuals against time and look for patterns.

![](../images/errors-over-time.png)


## Dealing with Non-constant Variance of Error Terms
