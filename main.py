## Importing packages
import math
from re import X
import statistics
import numpy as np
import pandas as pd
import scipy.stats 

## Numeric data
x = [8.0, 1, 2.5, 4, 28.0]
x_with_nan = [8.0, 1, 2.5, math.nan, 4, 28.0] 
x
x_with_nan

## Interchangable functions
math.isnan(np.nan), np.isnan(math.nan) 
math.isnan(x_with_nan[3]), np.isnan(x_with_nan[3])

## Creating an array
y, y_with_nan = np.array(x), np.array(x_with_nan) 
z, z_with_nan = pd.Series(x), pd.Series(x_with_nan) 
y
y_with_nan
z 
z_with_nan

## Calculating Mean
mean_ = sum(x) / len(x) 
mean_

mean_ = statistics.mean(x) 
mean_

mean_ = statistics.fmean(x) 
mean_

mean_ = statistics.mean(x_with_nan)
mean_ 

mean_ = statistics.fmean(x_with_nan)
mean_

mean_ = np.mean(y)
mean_

mean_ = y.mean()
mean_

np.mean(y_with_nan)
y_with_nan.mean() 

np.nanmean(y_with_nan) 

mean_ = z.mean() 
mean_

z_with_nan.mean() 

## Weighted Mean
0.2 * 2 + 0.5 * 4 + 0.3 * 8

x = [8.0, 1, 2.5, 4, 28.0]
w = [0.1, 0.2, 0.3, 0.25, 0.15]
wmean = sum(w[i] * x[i] for i in range(len(x))) / sum(w)
wmean
wmean = sum(x_ * w_ for (x_, w_) in zip(x, w)) / sum(w)
wmean

y, z, w = np.array(x), pd.Series(x), np.array(w) 
wmean = np.average(y, weights=w)
wmean 
wmean = np.average(z, weights=w)
wmean

(w * y).sum() / w.sum() 

## Arrays 
w = np.array([0.1, 0.2, 0.3, 0.0, 0.2, 0.1])
(w * y_with_nan).sum() / w.sum()

np.average(y_with_nan, weights=w) 

np.average(z_with_nan, weights=w)

## Harmonic Mean
hmean = len(x) / sum(1 / item for item in x) 
hmean

hmean = statistics.harmonic_mean(x)
hmean

statistics.harmonic_mean(x_with_nan)
statistics.harmonic_mean([1, 0, 2])
statistics.harmonic_mean([1, 2, -2])  # Raises StatisticsError 

scipy.stats.hmean(y) 
scipy.stats.hmean(z)

## Geometric Mean
gmean = 1 
for item in x:
    gmean *= item

gmean **= 1 / len(x)
gmean

gmean = statistics.geometric_mean(x)
gmean

gmean = statistics.geometric_mean(x_with_nan)
gmean

scipy.stats.gmean(y)
scipy.stats.gmean(z)

## Median

