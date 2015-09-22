## How Well Does the Model Fit the Data?

* Once we've established that there is a relationship between X and Y, we might want to know... to what extent does our model fit the data?  A lot?  Just a little bit?  Somewhere in between?
* Poor fit might arise from (a) a linear model not being the correct approximation for the data or (2) there just being a lot of inherent error variability in the data, or both.


#### Residual Standard Error

* Even if we knew β (the true data) perfectly, we still could not perfectly estimate Y from X because of the accumulated error terms *e*.
* The **residual squared error** (RSE) is an estimate of the standard deviation of *e*, or the average amount that the actual response will deviate from the perfect prediction line.
* RSE = sqrt((1/(n-2))RSS) = sqrt((1/(n-2)) * Σ{*i*=1 -> *n*}((*y*[*i*] - *y*^[*i*])^2))
* RSE ends up being a measure of lack of fit.  Very small RSE means the model fits the data very well.  Very large RSE means the model is a poor fit for the data.
* The downside of RSE is that it is measured relative to Y (in units of Y), so it is unclear what constitutes a good RSE and it is hard to compare different models together to assess which one is better.


#### R^2

* The **R^2 statistic** is the poroportion of variance explained by the model.
* R^2 = (TSS - RSS)/TSS = 1 - (TSS/RSS).  RSS is the residual sum of squares.  TSS is the **total sum of squares**, or Σ{*i*=1 -> *n*}((*y*[*i*] - mean(*y*))^2).
* TSS measures the total variance in Y, or the amount of varitability inherent in Y prior to any regression.  RSS measures the amount of variance left unexplained by the regression.
* Hence, TSS - RSS measures the total amount of variability that is explained by the regression, and (TSS - RSS)/TSS makes it proportional to the total variability.
* The R^2 statistic tries to correct the problem with RSE of being measured relative to Y by being a proportion, and thus always between 0 and 1.
* An R^2 close to 1 indicates a model with good fit and an R^2 close to 0 indicates poor fit.
* While R^2 is easier to interpret than RSE, it still can be difficult to know what threshold makes for a sufficiently good R^2, as different problem domains may be better approximated by linear models and/or have less overall error variability.  For example, in psychology, there is a lot of error variability and non-linearity in predicting human behavior, so R^2 of 0.3 can still be considered quite good.  But in physics, where data can be known to be taken from a perfectly linear mechanism, an R^2 of 0.9 can still be considered quite bad.
* R^2 is also similar to the correlation between X and Y, or *r*.  In fact, *r*^2 = R^2 for single regression (i.e., one predictor is used to predict the response variable).
*r* = (Σ{*i*=1 -> *n*}((*x*[*i*] - mean(*x*)((*y*[*i*] - mean(*y*))))))/((sqrt(Σ{*i*=1 -> *n*}((*x*[*i*] - mean(*x*))^2)))(sqrt(Σ{*i*=1 -> *n*}((*y*[*i*] - mean(*y*))^2))))
