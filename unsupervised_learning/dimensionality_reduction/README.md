# Dimensionality Reduction

This project covers the fundamentals of dimensionality reduction, with a
focus on Principal Component Analysis (PCA), implemented from scratch
using numpy.

## Requirements

* Ubuntu 16.04 LTS
* Python 3.5
* numpy 1.15
* All files are executable and end with a new line
* Code follows the pycodestyle (version 2.4) style guide
* All modules, classes, and functions must have documentation

## Tasks

### 0. PCA

File: 0-pca.py

Function `def pca(X, var=0.95):` performs PCA on a dataset.

**Parameters:**
* `X` is a numpy.ndarray of shape (n, d) where:
  * n is the number of data points
  * d is the number of dimensions in each point
  * all dimensions have a mean of 0 across all data points
* `var` is the fraction of the variance that the PCA transformation
  should maintain

**Returns:** the weights matrix W that maintains var fraction of
X's original variance. W is a numpy.ndarray of shape (d, nd)
where nd is the new dimensionality of the transformed X.

**Approach:** Uses Singular Value Decomposition (SVD) on the (mean
centered) data matrix X. The singular values s describe how much
variance is captured by each principal component. The cumulative sum
of s (normalized) tells us how many components nd are needed to
retain at least var fraction of the total variance. W is then
built from the first nd right-singular vectors.

**Example usage:**

    ./0-main.py

See 0-main.py for a full example that:
1. Builds a correlated 6-dimensional dataset
2. Mean-centers it
3. Computes W via pca
4. Projects X into the reduced space T = X @ W
5. Reconstructs X from T and checks the reconstruction error is
   effectively 0

## Author

Fatma Xanım - [GitHub](https://github.com/fatmaxanim2006)
