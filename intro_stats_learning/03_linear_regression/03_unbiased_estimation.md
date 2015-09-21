## Variance and Standard Deviation

* The **variance** of data is a measure of how spread out the data is.  Data with a variance of 0 means that all the data points are identical.
* Variance is defined as the mean of the squared differences between each data point and the mean data point, or (Σ{*i*=1 -> *n*}((X[*i*] - mean(X))^2))/*n*.
* For example, the set [3, 1, 4, 1, 5, 9] has a mean of (3+1+4+1+5+9)/6 = 3.83.  The set thus has a standard deviation of ((3-3.83)^2 + (1-3.83)^2 + (4-3.83)^2 + (1-3.83)^2 + (5-3.83)^2 + (9-3.83)^2)/6 = 7.47.
* The **standard deviation** is the square root of the variance, σ(X) = sqrt(Var(X)).  The standard deviation is used much more frequently because it is expressed in the same units as the original data.  (Variance would be expressed in squared units.)


## Population vs. Sample

* A **population** is the entire data set we're seeking to estimate.  We've been referring to this as the set X.
* A **sample** is a smaller subsection of the population.  We can refer to this with the set x.  There are many possible samples of X.


## Unbiased Estimation

* If Y^ is **unbiased**, then **on average** Y^ = Y when aggregated across all possible observations of the population.
* Since bias (recall from the bias-variance tradeoff) is the tendency of an estimator to systematically overestimate or underestimate the true value, this definition makes sense.
* The population is the group as a whole we're seeking to make predictions for.  However, the actual makeup of the population is (frequently) unknown to us.
* Observations are smaller subsections (snapshots) of the population that we do get to see and make predictions from.
* Saying that **on average** Y^ = Y means that estimating Y^ from some observations will lead to an **overestimate** of Y (Y^ > Y) and in some observations estimating Y^ will lead to an **underestimate** of Y (Y^ < Y), the average of all these underestimates and overestimates will approach 0 the more observations you get (and the closer you get to seeing the entire population).
* This can be seen in how multiple least squares lines (made from multiple observations of the population) converge to the population regression line (made from the entire population).


## Standard Error

* The set of means we get by looking at all the sample means itself has a mean (a mean of sample means) and a standard deviation (the standard deviation of the sample means).
* The standard deviation of the sample means is called the **standard error**.


## Population vs. Sample Variance

* Calculating the variance for an entire set, or the **population variance**, is (Σ{*i*=1 -> *n*}((X[*i*] - mean(X))^2))/*n*.
* But if we want to calculate the variance for a sample, the **sample variance** we should use (Σ{*i*=1 -> *n*}((X[*i*] - mean(X))^2))/(*n*-1) instead.
* This is called **Bessel's Correction**.  The correction is correcting bias in using the sample variance as an estimate of the population variance, though it comes at the cost of insteading the mean squared error.


## Ubiased Estimation of Means

* Just like how on average Y^ = Y if Y^ is unbiased, on average the sample mean of a random variable is equal to the population mean of that variable.  That is, on average, μ^ = μ (assuming μ^ is unbiased).
* But how far off will a single estimate of μ^ be?  The answer is the standard error of μ^, or SE(μ^).
* Earlier we talked about variance.  The variance of μ^ is equal to the square of the standard error of μ^.  Expressed mathematically, Var(μ^) = SE(μ^)^2.
* The variance of μ^ is also equal to the square of the standard deviation of μ^ divided by the number of observations.  Var(μ^) = (σ^2)/n.
