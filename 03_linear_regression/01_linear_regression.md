## Linear Regression

* Predicts a quantitative response.
* Useful jumping off point for predictive methods, as many methods are extensions of linear regression.

## Key Questions for Analysis

* Is there a relationship between X and Y?
* How strong is the relationship between X and Y?
* Which x in X contribute to Y?
* How accurately can we determine which x in X contribute to Y?
* How accurately can we predict future Y given future combinations of x in X?
* Is the relationship between X and Y linear?
* Do the x in X affect Y alone, or do particular combinations of x in X produce synergy together (called an **interaction effect**)?

## Simple Linear Regression

* Y ~= β[0] + β[1]*X
* `~=` means "is approximately modeled as".
* β[0] and β[1] are **model coefficients** or **parameters**.
* Training data lets us estimate β^[0] and β^[1], and we can start predicing that *y*^ = β^[0] + β^[1] * *x*
* *y*^ is a prediction of Y on the basis of X = *x*.
* The `^` symbol indicates the estimated value of an unknown parameter.
