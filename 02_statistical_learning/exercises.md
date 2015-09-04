**1. For each of parts (a) through (d), indicate whether we would generally expect the performance of a flexible statistical learning method to be better or worse than an inflexible method. Justify your answer.**

**(a) The sample size n is extremely large, and the number of predictors p is small.**  A flexible method would preform better because it can extract extra information from the large n.  The large n also greatly reduces the risk of overfitting, which is the biggest problem with highly flexible methods.

**(b) The number of predictors p is extremely large, and the number of observations n is small.** The risk of overfitting is very high and any patterns picked up by flexible methods are more likely to be mere noise.  Therefore an inflexible method should be preferred.

**(c) The relationship between the predictors and response is highly non-linear.** Inflexible methods have a lot of trouble picking up non-linear relationships, so we should prefer a flexible method.

**(d) The variance of the error terms, i.e. σ2 = Var(ε), is extremely high.** The high variance of error terms means that the sample will have a lot of noise in the relationship.  Therefore we should prefer an inflexible method that is less likely to overfit to this noise.

-

**2. Explain whether each scenario is a classification or regression problem, and indicate whether we are most interested in inference or prediction. Finally, provide n and p.**

**(a) We collect a set of data on the top 500 firms in the US. For each firm we record profit, number of employees, industry and the CEO salary. We are interested in understanding which factors affect CEO salary.**  This is a regression problem, because CEO salary is a continuous variable.  We are interested in inference, because we want to know how factors impact CEO salary.  n = 500 (500 firms provide our data points) and p = 3 (profit, number of employees, and industry).

**(b) We are considering launching a new product and wish to know whether it will be a success or a failure. We collect data on 20 similar products that were previously launched. For each product we have recorded whether it was a success or failure, price charged for the product, marketing budget, competition price, and ten other variables.**  This is a classification problem, as we are trying to classify success vs. failure.  This is also a prediction problem because we want to predict success vs. failure with less concern for understanding the underlying relationships.  n = 20 (20 similar products previously launched) and p = 13 (price, marketing budget, competition price, and ten other variables).

**(c) We are interesting in predicting the % change in the US dollar in relation to the weekly changes in the world stock markets. Hence we collect weekly data for all of 2012. For each week we record the % change in the dollar, the % change in the US market, the % change in the British market, and the % change in the German market.**  This is a regression problem because % change in the US dollar is a quantitative dependent variable.  This is also ap rediction problem because "we are interested in predicting the % change".  n = 52 (weekly data over 2012) and p = 3 (% change in US, % change in British, % change in German).

-

**5. What are the advantages and disadvantages of a very flexible (versus a less flexible) approach for regression or classification? Under what circumstances might a more flexible approach be preferred to a less flexible approach? When might a less flexible approach be preferred?**

Because of the bias-variance tradeoff, neither approach is better than the other.  A very flexible approach is great when the relationship is highly non-linear, you have a lot of data points to find a pattern from, and/or the irreducible error is low.  A very inflexible approach is great when the relationship is highly linear, you don't have many data points, and/or the irreducible error is high.

-

**6. Describe the differences between a parametric and a non-parametric statistical learning approach. What are the advantages of a parametric approach to regression or classification (as opposed to a non- parametric approach)? What are its disadvantages?**

A non-parametric approach is better at fitting highly nonlinear patterns, because less assumptions are made about the structure of the data.  However, this can be dangerous in situations where the risk of overfitting is high (see exercise #5).  Furthermore, this comes at the cost of not being able to easily interpret the data, since you don't have the interpretation structure of the parameters.

-

**7. The table below provides a training data set containing six observations, three predictors, and one qualitative response variable.**

| Obs | X1 | X2 | X3 | Y |
| --- | -- | -- | -- | - |
| Content Cell  | Content Cell  | Content Cell  | Content Cell  | Content Cell |
| 1   | 0  | 3  | 0  | Red |

| Obs | X1 | X2 | X3 | Y     |
| --- | -- | -- | -- | ----- |
| 1   | 0  | 3  | 0  | Red   |
| 2   | 2  | 0  | 0  | Red   |
| 3   | 0  | 1  | 3  | Red   |
| 4   | 0  | 1  | 2  | Green |
| 5   | −1 | 0  | 1  | Green |
| 6   | 1  | 1  | 1  | Red   |

**Suppose we wish to use this data set to make a prediction for Y when X1 = X2 = X3 = 0 using K-nearest neighbors.**

**(a) Compute the Euclidean distance between each observation and the test point, X1 = X2 = X3 = 0.**

Obs 1 has Euclidean Distance sqrt[(0 - 0)^2 + (3 - 0)^2 + (0 - 0)^2] = 3.

Obs 2 has Euclidean Distance sqrt[(2 - 0)^2 + (0 - 0)^2 + (0 - 0)^2] = 2.

Obs 3 has Euclidean Distance sqrt[(0 - 0)^2 + (1 - 0)^2 + (3 - 0)^2] = sqrt[0 + 1 + 9] = sqrt[10] = ~3.16.

Obs 4 has Euclidean Distance sqrt[(0 - 0)^2 + (1 - 0)^2 + (2 - 0)^2] = sqrt[1 + 4] = sqrt[5] = ~2.24.

Obs 5 has Euclidean Distance sqrt[(-1 - 0)^2 + (0 - 0)^2 + (1 - 0)^2] = sqrt[1 + 1] = sqrt[2] = ~1.41.

Obs 6 has Euclidean Distance sqrt[(1 - 0)^2 + (1 - 0)^2 + (1 - 0)^2] = sqrt[1 + 1 + 1] = sqrt[3] = ~1.73.

**(b) What is our prediction with K = 1? Why?**

The nearest neighbor to test point (0, 0, 0) is Obs 5 (-1, 0, 1) with euclidean distance ~1.41.  Since Obs 5 was Green, we predict (K = 1) that the test point will also be Green.

**(c) What is our prediction with K = 3? Why?**

The nearest three neighbors to test point (0, 0, 0) are Obs 5, Obs 6 (with distance ~1.73), and Obs 2 (with distance 2).  Since Obs 5 was Green, Obs 6 was Red, and Obs 2 was Red, we predict (K = 3) the test point will be the majority -- Red.

**(d) If the Bayes decision boundary in this problem is highly nonlinear, then would we expect the best value for K to be large or small? Why?**

A highly nonlinear Bayes boundary would suggest that there is less advantage to generalizing further due to high variance, so the best value for K would be small.
