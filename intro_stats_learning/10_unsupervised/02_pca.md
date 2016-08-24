## Principal Components Analysis

If you have a *n* by *p* grid of observations, plotting them on a two-dimensional grid would involve many possible scatterplots -- *p*(*p*-1)/2 to be exact. Instead, it would be nice if we could find a low-dimensional representation of the data that captures as much of the information as possible, allowing us to see the observations in a lower-dimensional space. **Principal component analysis** (PCA) is a process where we do this dimensionality reduction and optimization.

The first principal component *Z*[1] is the normalized linear combination of the features with the largest variance. That is, *Z*[1] = φ[1,1]*X*[1] + φ[2,1]*X*[2] + ... + φ[*p*,1]*X*[*p*] where ## Principal Components Analysis[*j*=1 to *p*](φ[*j*,1]^2) = 1. φ is the set of **loadings** of the first principal component and the principal component loading vector φ[,1] = (φ[1,1] φ[2,1] ... φ[*p*,1])^T. Normalized in this context means that each variable is transformed to have a mean of zero and a standard deviation of one.

The loadings are constrained to have a sum of squares equal to one to avoid arbitrarally large variance. This means that calculating *Z*[1] is about maximizing the variance subject to the sum of squares constraint.

The second principal component *Z*[2] is the normalized linear combination of features that maximizes variance while being uncorrelated with *Z*[1], making the two components orthogonal (perpendicular) in space.

Principal components can be plotted against each other for a lower dimensional view of the data.

The principal components are the hyperplane that is closest to the *n* observations (using average squared Euclidean distance).


## Percentage of Variance Explained

Total variance in a data set (assuming variables are centered to a mean of zero) is ## Principal Components Analysis[*j*=1 to *p*](Var(*X*[*j*])) = ## Principal Components Analysis[*j*=1 to *p*]((1/*n*)(Σ{*i*=1 -> *n*}(*x*[*i*,*j*]^2)).

The variance explained by the *m*th principal component is (1/*n*)(## Principal Components Analysis[*i*=1 to *n*](*z*[*i*,*m*]^2)) = (1/*n*)(## Principal Components Analysis[*i*=1 to *n*](Σ{*j*=1 -> *p*}(φ[*j*,*m*]*x*[*i*,*j*]))).

The percentage of variance explained (PVE) of the *m*th principal component is the variance explained by the *m*th principal component divided by the total variance of the data set, which is (1/*n*)(## Principal Components Analysis[*i*=1 to *n*](## Principal Components Analysis[*j*=1 to *p*](φ[*j*,*m*]*x*[*i*,*j*]))) / Σ{*j*=1 -> *p*}((1/*n*)(Σ{*i*=1 -> *n*}(*x*[*i*,*j*]^2)).

Plotting the cumulative PVE is called a **scre plot**.


## Use of PCA

Besides being able to better visualize data, PCA can be used as variables in a linear regression or other learning technique. PCA often leads to less noisy results since the signal in a data set is often concentrated in the first few principal components.
