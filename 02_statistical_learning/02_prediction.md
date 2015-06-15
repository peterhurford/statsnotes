## Statistical Learning

* Goal is to make accurate predictions about cause and effect.


## Prediction

* Predict Y from X.

* Y^ = *f^*(X), where *f^* represents our estimate of *f* and Y^ represents our prediction of Y.


#### Prediction Accuracy

* The accuracy of our prediction depends on how similar Y^ is to Y.

* Inaccuracy is caused by reproducible error and irreducible error.

* **Reducible error** represents the error that results from *f^* being an imperfect representation of *f*.  We can reduce reducible error by making *f^* more like *f*.

* **Irreducible error** represents the error that results from *e*.  Since *e* cannot be predicted from X, this error is irreducible and nothing can be done.

* Because of irreducible error, even a perfect model (*f^* = *f*) will not result in perfect prediction (Y^ = Y).


#### Notation for Error

* Error can be defined as E(Y - Y^)^2 = E(*f*(X) + *e* - f^(X))^2 = (*f*(X) - *f^*(X))^2 + Var(*e*).

* E is error. Var is the variance function.

* (*f*(X) - *f^*(X))^2 is reducible error, Var(*e*) is irreducible error.


#### Where does irreducible error come from?

* Why would *e* be bigger than 0?

* This could be because while X includes many variables, there is another important variable useful in predicting Y that is not in X.

* *e* also could include unmeasurable variation, such that no possible variable could capture it.
