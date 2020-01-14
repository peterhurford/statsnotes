#### Probit vs. Logit vs. Logistic

* *Probit regression*, *logit regression*, and *logistic regression* all aim to predict a binary outcome using a regression that makes an s-shaped curve from 0 to 1 of the form *y = f(α + βx)*. They differ in how they define *f*.

* The logit model uses something called the cumulative distribution function of the logistic distribution.

* The probit model uses something called the cumulative distribution function of the standard normal distribution.

* The logistic model is the inverse of the logit.

* Logit / logistic has easier interpretation than probit. Logistic regression can be interpreted as modelling log odds (i.e those who smoke >25 cigarettes a day are 6 times more likely to die before 65 years of age).

* Probit models can be generalized to account for non-constant error variances in more advanced econometric settings (known as heteroskedastic probit models) and hence are used in some contexts by economists and political scientists. If these more advanced applications are not of relevance, than it does not matter which method you choose to go with.

* Logistic / logit has slightly flatter tails. That is, the probit curve approaches the axes more quickly than the logit curve.


#### Sources

* https://tutorials.methodsconsultants.com/posts/what-is-the-difference-between-logit-and-probit-models/
* https://stats.stackexchange.com/questions/20523/difference-between-logit-and-probit-models
* https://stats.stackexchange.com/questions/120329/what-is-the-difference-between-logistic-and-logit-regression
* https://www.econometrics-with-r.org/11-2-palr.html
