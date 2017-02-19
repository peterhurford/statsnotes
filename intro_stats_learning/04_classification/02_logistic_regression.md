#### Why Not Linear Regression?

* Predicting multiple outcomes (e.g., "Red", "Blue", and "Green") with a regression requires using numeric labels (e.g., 1 = "Red", 2 = "Blue", and 3 = "Green"). But doing this creates an implied ordinality (saying "Green" > "Blue" > "Red") which is not the case, and which will bias the results.

* It would be possible to predict binary outcomes (e.g., 1 = "Red" vs. 0 = "Not Red"). Howver, using a linear regression would still produce predictions outside of [0, 1], which would not be interpretable.


#### Logistic Regression

* **Logistic regression** solves the [0, 1] bounding issue for predicting binary outcomes.

* Rather than using the definition of linear regression, or `p(X) = β[0] + β[1]*X`, logistic regression uses `p(X) = (*e*^(β[0] + β[1]*X))/(1 + *e*^(β[0] + β[1]*X))`. This is a **logistic function** that will always fall between 0 and 1.

* β is estimated using the **maximum likelihood method**, which seeks to find β such that, for each individual, `p(X)` is as close as possible to 0 when the individual is the 0-represented class and `p(X)` is as close as possible to 1 when the individual is in the 1-represented class.

* This is formalized using the following **likelihood function**: `*l*(β) = Π{*i* : *y*[*i*] = 1}p(x[*i*]) * Π{*i* : *y*[*i*] = 0}(1 − p(x[*i*]))`. β is chosen to maximize this function.


#### Hypothesis Testing

* Linear regression says that for every one-unit increase in X, you will get a β-unit increase in Y. Logistic regression instead suggests that for every one-unit increase in X, you will get a β-unit increase in the **log-odds** (also called logit) of Y.  Log-odds are `log(p(X) / (1 - p(X)))` and are the log of the odds ratio, which is `p(X) / (1 - p(X))`.

* The **z-statistic** of the logistic regression is analagous to the *t*-statistic of the linear regression. The *z*-statistic of β[1] is equal to `β[1] / SE(β[1])`.

* The null hypothesis is that `p(X) = (*e*^(β[0])) / (1 + *e*^(β[0]))`, or that there is no relationship because β[1] = 0. 


#### Multiple Logistic Regression

* Just as linear regression can be scaled to multiple variables by extending `p(X) = β[0] + β[1]*X` to `p(X) = β[0] + β[1]*X + β[2]*X + ... + β[*p*]*X`, logistic regression can be scaled to multiple variables by extending `p(X) = (*e*^(β[0] + β[1]*X)) / (1 + *e*^(β[0] + β[1]*X))` to `p(X) = (*e*^(β[0] + β[1]*X + β[2]*X + ... + β[*p*]*X)) / (1 + *e*^(β[0] + β[1]*X + β[2]*X + ... + β[*p*]*X))`.
