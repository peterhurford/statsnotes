Weights, Bias Parameter
let ws = [1.5, 0.5, -1.5, -2.5]
let dot ws xs = foldl (+) 0 $ zipWith (*) ws xs
Dot product

let xfer x = 1 / (1 + exp (-x))

Transform Function

let perc xs = xfer (dot wts (1:xs))

Perceptron ::: xfer (ws . 1:xs)
layer      ::: [perceptron]          R^n -> R^m (n+1) * m parameters
nerual net ::: composition of layers
100x100 image ... (R^10000 -> R^200), (R^200 -> R^15), (R^15 -> R)
parameters ::: (10001 * 200) + (201 * 15) + 16 = 2003231 parameters

map g (M * v)  (vectorizing transfer function)
