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

![](../images/residual-plots.png)

On the left, there is no relationship between the resudial and the variable, which means the linear relationship looks correct.  However, on the right graph, there is a strong linear relationship between the residuals and the variable, which suggests the assumption of a linear relationship between the variable and the DV is not correct.
