## How do we determine which estimate of *f* is the best?

* In order to determine how good our estimate is, we need to measure **quality of fit** (QoF), or quantify the extent to which the predicted response value for a given observation is close to the true response value for that observation, across all observations.

#### Mean Squared Error

* For regressions, a common used measure is **mean squared error** (MSE), or the sum of the squares of the differences between the actual value and the predicted value, or (1/*n*) * (Σ{*i*=1 -> *n*}((*y*[*i*] - *f^*(*x*[*i*]))^2)).

* MSE is small if the predicted responses are very close to the true responses and large if, for at least some of the observations, the predicted and true responses differ substantially.


## Training QoF vs. Validation QoF

* Recall that **training data** is the set of data we use to estimate *f*.  **Validation data** (also called a **hold-out set**) is a separate data set that we specifically hold out and do not use for estimating *f*.

* Why?  We don't care how accurately we can determine the train data.  Rather, we care how accurately our model can generalize to data it has not seen before, to make predictions.  Holding out validation data allows us to simulate seeing new data the model is not trained on.  We can then use validation data to assess our model accuracy.

* **Training QoF** is the QoF metric assessed on the training data -- after *f* is estimated (meaning the model is trained), we then look back at the data used to estimate *f* and assess the QoF.  However, because we want to test generalization to data we have not seen before, what we would actually prefer to do is assess **Validation QoF**, or perform the QoF metric with validation data.  In nearly every case, Validation QoF will be worse than Training QoF.

* Using Validation QoF also helps gaurd against overfitting.  If the Training QoF is very good, it could be because we've captured a bunch of randomness that is present only in the training dataset and which doesn't generalize.  This overfitting won't help with the validation set, and Validation QoF will be much worse.


## Test Data vs. Validation Data

* How can we get the best Validation QoF?  As we can see, merely trying to optimize Training QoF will not lead to an optimized Validation QoF.

* We may try to repeatedly train (also called "fit") models and assess their Validation QoF, but then this risks overfitting Validation QoF too, which reduces the quality of Validation QoF as a metric of model accuracy.

* Instead, the solution is to create two hold-out sets -- a test set and a validation set.  We then continue to fit and refit models and test against the test set, assessing Test QoF.  Once we have optimized Test QoF, we then -- only once -- look to our second hold-out set, the validation set, and assess Validation QoF, and use Validation QoF as our final metric.

* Test QoF works as a good intermediary metric because it will be less susceptible to overfitting and other problems of non-generalization, since it is not a part of the training data.


## Bias-Variance Tradeoff

* The expected validation MSE can always be decomposed to the sum of three fundamental quantities: variance of *f^*(*x*[0]), the squared **bias** of *f^*(*x*[0]), and the variance of the error terms *e*.  That is, E(*y*[0] - *f^*(*x*[0]))^2 = Var(*f^*(*x*[0])) + (Bias(*f^*(*x*[0])))^2 + Var(*e*), where E(*y*[0] - *f^*(*x*[0]))^2 is the **expected validation MSE** and refers to the average validation MSE we would obtain if we repeatedly estimated *f* using a large number of training sets and tested each at *x*[0].

* This means that in order to minimize expected validation MSE, we should select a statistical learning method that simlataneously achieves low variance and low bias.

* **Variance** refers to the amount by which *f^* would change if we estimated it using a different train set.  In general, more flexible statistical methods have higher variance, since they track observations much more closely and are thus more sensitive to small changes in observations between training sets.

* **Bias** refers to the error introduced by using a simplified model to approximate a more complicated relationship.  For example, linear models introduce bias to the degree that the relationship they are modeling is not truly linear.  Generally more flexible methods have lower bias because they are able to more closely model the true relationship.

* This means that as we increase the flexibility of the model, variance will increase and bias will decrease, having differential impacts on the expected validation MSE.  This relationship between bias and variance is referred to as the **bias-variance tradeoff**.  The challenge lies in finding a method for which both the variance and the squared bias are low.  This also explains how exteremely flexible methods may fail to outperform less flexible methods -- they introduce more variance than they reduce squared bias.
