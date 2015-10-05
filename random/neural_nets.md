## Neural Nets

* A **neural network** is a network of nodes that are each weak learning algorithms.  Together, these algorithms are combined together to create predictions and classifications.
* A neural network is often compared to a brain.  That may have been the intent in the 1960s, and it is true on some level, but it's easier to think of it as a mathematical function.
* At core, a neural net is simply a function that takes a vector of values, transforms the values by multiplying them by other values, and combines all the values together into one output.


## Weights

* The neural net takes in a vector of **features**, or characteristics of the problem.  For example, weather features may be temperature, humidity, cloud cover, etc.
* The neural net is started through a vector of **weights**, or values that are multiplied by the features.
* These weights start out random, but are trained through iterations of the neural net.


## Dot Product

* A **dot product** is an aggregate value derived from two different vectors.  In this example, we intend to take the sum of the product of the features and the weights.

```Haskell
let features = [1, 2, 3, 4]
let weights = [1.5, 0.5, -1.5, -2.5]
let dot weights features = foldl (+) 0 $ zipWith (*) weights features

dot weights features
> -12
```


## Transform Function

After we have the dot product of the features and the weights, we pass the product into a transform function.

#### Bias

```Haskell
let bias = 1
```

#### Predicting Binary Output

```Haskell
let binary_transform x bias = if x + bias > 0 then 1 else 0

binary_transform (weights `dot` features) bias
> 0
```

#### Predicting Continuous Output

```Haskell
let con_transform x = 1 / (1 + exp (-x))

con_transform (weights `dot` (1:features))
> 2.0342697805520653e-4
```


Perceptron ::: xfer (ws . 1:xs)
layer      ::: [perceptron]          R^n -> R^m (n+1) * m parameters
nerual net ::: composition of layers
100x100 image ... (R^10000 -> R^200), (R^200 -> R^15), (R^15 -> R)
parameters ::: (10001 * 200) + (201 * 15) + 16 = 2003231 parameters

map g (M * v)  (vectorizing transfer function)
