## Nonlinear Linear Models (Polynomial Regression)

* Another way we can extend these linear models is to not make them linear anymore
* This is what gives linear models a fair degree of ability to still flexibly fit a lot of data, while remaining quite interpretable.
* For example, if we have Y = β[0] + β[1]X[1] + β[2]X[2] and it turns out the correct relationship between X[2] and Y is not linear but rather quadratic, we can change the equation to Y = β[0] + β[1]X[1] + β[2]X[2] + β[3]X[2]^2 to capture this effect.
* This relationship is still linear, we're just using a variable X[3] = X[2]^2.
