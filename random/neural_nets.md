## Neural Nets

* A **neural network** is a network of nodes that are each weak learning algorithms.  Together, these algorithms are combined together to create predictions and classifications.
* A neural network is often compared to a brain.  That may have been the intent in the 1960s, and it is true on some level, but it's easier to think of it as a mathematical function.  In my opinion, thinking about neural nets using the brain analogy is more confusing than helpful.
* At core, a neural net is simply a function that takes a vector of values, transforms the values by multiplying them by other values, and combines all the values together into one output.
* Predictions are then found for a dependent variable (variable to be predicted) by passing in multiple independent variables, which are then aggregated with weights using a dot product and a transform function.
* Note: I have pretty limited knowledge of neural nets, so much of this could be wrong.


## Weights

* The neural net takes in a vector of **features**, or characteristics of the problem.  For example, weather features may be temperature, humidity, cloud cover, etc.
* The neural net is started through a vector of **weights**, or values that are multiplied by the features.
* These weights start out random, but are trained through iterations of the neural net.


## Dot Product

* A **dot product** is an aggregate value derived from two different vectors, such as by taking the sum of the product of the features and the weights.  Here is an example in Haskell:

```Haskell
let features = [1, 2, 3, 4]
let weights = [1.5, 0.5, -1.5, -2.5]
-- Multiply each feature by each weight and then sum the entire set together.
let dot weights features = foldl (+) 0 $ zipWith (*) weights features

dot weights features
> -12
```


## Transform Function

After we have the dot product of the features and the weights, we pass the product into a transform function.

#### Bias

The bias is an important parameter in neural networks, as it allows you to control the overall output of the neural network by moving the entire set of predictions up or down.  It focuses analagous to the intercept in a linear model.

```Haskell
let bias = 1
```

#### Predicting Binary Output

For predicting binary output with a given set of features, a given set of weights, and the bias, a binary transform function is used, where the result is 1 if the dot product of the weights and the features plus the bias is greater than 0, and 0 otherwise.

```Haskell
let binary_transform x bias = if x + bias > 0 then 1 else 0

binary_transform (weights `dot` features) bias
> 0
```

#### Predicting Continuous Output

We also can predict a continuous output by using a different transform function relying on a logistic transformation.  Here, we incorporate the bias by prepending it to the feature list.

```Haskell
let continuous_transform x = 1 / (1 + exp (-x))

continuous_transform (weights `dot` (bias:features))
> 2.0342697805520653e-4
```


## The Neural Network

* The **neural network** is a composition of **layers**, each of which are a composition of **perceptrons**.  "Perceptron" is a fancy word for those transformation functions we talked about earlier.
* Each layer takes a large amount of inputs and reduces it to a smaller number of inputs through these transformation functions, until we ultimately have a single prediction.
* For example, an 100x100 pixel image will yield 10000 variables (the value of each pixel), which could be reduced to 200 variables through one layer, reduced to 15 by a second layer, and reduced to one by a third layer.
* There needs to be a weight for each input plus the bias at each step.  This means that in our example, there are ((10000 + 1) * 200) + ((200 + 1) * 15) + ((15 + 1) * 1) = 2,003,231 weights.


## Learning

* But how do we get the correct value of the weights?  This is the key question of **learning**.

#### Backpropagation

* One technique for learning (among several) is **backpropagation**.
* For this, we start all the weights at 1 (or, with **random backpropagation**, at small random values).
* We then take an example of where we know what the output from the inputs should be (called **training data**) and we predict the output from the inputs using the current weights.
* We then compare the predicted output to what the output *should have been* and we get an **error rate**.
* We then use this error rate to inform the finalmost layer, figuring out what the error rate of each weight was.  These error rates then are used to inform the second-finalmost layer, etc., propogating backwards through the neural net.
* We then adjust all the weights by their errors and repeat the process.
* After millions of rounds of doing this, we finally get reasonable predictions.

#### Overfitting

* One problem with this backpropogation technique is **overfitting**, where the weights end up too closely aligned (or **fitted**) to random fluctuations in the training data and don't sufficiently generalize to future data in the real world.
* One solution to overfitting is **early stopping**.  The idea is that overfitting risk is the highest when the neural net is *trained too much*, so we stop the training early according to some criterion to keep the net sufficiently general.


## Recurrent Neural Nets vs. Feedforward Neural Nets

* What I described are called **feedforward neural nets**.  There is also something called a **recurrent neural network**, which produces arbitrary amounts of output given inputs.  I don't (yet) understand how these work.
