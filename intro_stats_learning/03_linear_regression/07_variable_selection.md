## Variable Selection

* Once we know we have a predictive model, we want to know if all the variables are predictive too.
* We might be tempted to select only those variables where the p-value is < 0.05, but this might be due to false discoveries.

## Selection Techniques

#### Exhausive Search (Looking at Every Model)

* One thing we can do is generate every possible model using every possible cominbatino of variables and then use the model with the best R^2, selecting only those variables.
* For example, if we have two variables A and B, we might make a model with no variables, a model with just A, a model with just B, and a model with both A and B, and pick the model with the best R^2.
* This works well except that with 30 variables, we need to consider 2^30 = 1073741824 models!
* Instead, we can use a few different selection techniques that use heuristics to greatly reduce the search space, even if they don't always pick the *best* combination.

#### Forward Selection

* Begin with the **null model** (the model with no predictors).  Then fit a single linear regression to each variable, constructing *p* models in total.  Take the variable with the lowest RSS.  Add that variable to our model.  Then construct *p* two-variable linear models with the chosen variable and each of the remaining variables, one-by-one.  Add the next variable that had the lowest RSS.  Keep continuing until some **stopping rule**, or criterion for stopping, is satisfied.

#### Backward Selection

* Begin with a model with all the variables.  Remove the variable with the highest p-value and refit.  Keep removing the highest p-value variable until some stopping rule is satisfied (for example, all variables meet a certain p-value threhshold).

#### Mixed Selection

* Begin with the null model and add variables as in forward selection.  However, if, at any step, any of the variables in the model exceed a certain p-value threhsold, remove them from the model and refit.  Stop when all variables in the model meet a certain p-value threshold and any variable not added to the model would not meet that p-value threshold if added.
