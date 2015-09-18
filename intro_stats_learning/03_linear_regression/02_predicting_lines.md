## Estimating β^

* β^[0] = mean(*y*) - β^[1] * mean(*x*)
* β^[1] = (Σ{*i*=1 -> *n*}((*x*[*i*] - mean(*x*))(*y*[*i*] - mean(*y*))))/(Σ{*i*=1 -> *n*}((*x*[*i*] - mean(*x*))^2)
* mean(*x*) refers to the **sample mean** of *x*, or (1/n)Σ{*i*=1 -> *n*}(*x*[*i*]).


## Interpreting β^

* Given that Y ~= β[0]^ + β[1]^*X, we estimate that for every increase of 1 in X, we predict there will be a corresponding β[1]^ increase in Y.  Also, when X = 0, we predict Y will be β[0]^.


## Assessing the Accuracy of β^

* The line given by Y = β[0] + β[1]*X + *e* is the **population regression line**, or the line that most closely resembles the relationship (given perfect data).
* The line given by Y^ = β[0]^ + β[1]^*X is the **least squares line**, or the line that best predicts the relationship using least squares analysis on the data we have.

![](../images/population-regression-line.png)


## Unbiased Estimation

* If Y^ is **unbiased**, then **on average** Y^ = Y when aggregated across all possible observations of the population.
* The population is the group as a whole we're seeking to make predictions for.  However, the actual makeup of the population is (frequently) unknown to us.
* Observations are smaller subsections (snapshots) of the population that we do get to see and make predictions from.
* Saying that **on average** Y^ = Y means that estimating Y^ from some observations will lead to an **overestimate** of Y (Y^ > Y) and in some observations estimating Y^ will lead to an **underestimate** of Y (Y^ < Y), the average of all these underestimates and overestimates will approach 0 the more observations you get (and the closer you get to seeing the entire population).
* This can be seen in how multiple least squares lines (made from multiple observations of the population) converge to the population regression line (made from the entire population).
