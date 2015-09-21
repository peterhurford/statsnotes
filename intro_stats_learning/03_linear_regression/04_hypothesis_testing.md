## Hypothesis Testing

* **Hypothesis tests** test certain hypotheses about the coefficients (β).
* Hypothesis tests involve picking between >1 hypotheses that, together, are **mutually exclusive** (only one of them can be true) and are **collectively exhaustive** (at least one of them must be true).
* The most common hypothesis test tests the **null hypothesis** that there is no relationship between X and Y (that is, β[1] = 0) against the **alternative hypothesis** that there is a relationship between X and Y (β[1] != 0).


## Evaluating the Null Hypothesis

* We're willing to reject the null hypothesis β[1] = 0) if our prediction, β^[1], is sufficiently far enough from 0 to be sufficiently confident it is not 0.
* We could see if 0 falls outside our confidence interval.  If it does, perhaps we are confident that β[1] isn't 0.
* Another way is to use the standard error calculate the **t-statistic**, which measures the number of standard deviations our measured β[1] is from 0.  We do this by calculating *t* = (β[1] - 0)/(SE(β[1])).
* If there is no relationship between X and Y, then *t* will be drawn from a **t-distribution** with *n*-2 **degrees of freedom**.  Since the t-distribution is quite similar to a **normal distribution**, we can calculate the probability of observing a t-statistic as large as abs(*t*) or later, assuming β^[1] = 0.  This probability is called the **p-value**.
* A small p-value indicates that there was a really low probability of observing *t* by chance.  However, there is a comparatively much higher probability of observing *t* if *t* was drawn from a distribution where β^[1] != 0.  Hence, a sufficiently small p-value leads us to infer that β^[1] != 0 and therefore there is a relationship between X and Y.
* Thus, a sufficiently small p-value leads us to reject the null hypothesis.
* Typically, "sufficiently small" p-values are below 0.05, which corresponds to *t* being greater han 2.


## TODO:
* What are degrees of freedom?
* What is a normal distribution?
* What is a t-distribution?
