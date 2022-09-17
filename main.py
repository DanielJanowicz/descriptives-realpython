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

n = len(x)
if n % 2:
    median_ = sorted(x)[round(0.5*(n-1))]
else:
    x_ord, index = sorted(x), round(0.5 * n)
    median_ = 0.5 * (x_ord[index-1] + x_ord[index])

median_

median_ = statistics.median(x)
median_
median_ = statistics.median(x[:-1])
median_

statistics.median_low(x[:-1])
statistics.median_high(x[:-1])

statistics.median(x_with_nan)
statistics.median_low(x_with_nan)
statistics.median_high(x_with_nan)

median_ = np.median(y)
median_
median_ = np.median(y[:-1])
median_

np.nanmedian(y_with_nan)
np.nanmedian(y_with_nan[:-1])

z.median()
z_with_nan.median()

## Mode
u = [2, 3, 2, 8, 12]
mode_ = max((u.count(item), item) for item in set(u))[1]
mode_

mode_ = statistics.mode(u)
mode_
mode_ = statistics.multimode(u)
mode_

v = [12, 15, 12, 15, 21, 15, 12]
statistics.mode(v)  # Raises StatisticsError
statistics.multimode(v)

statistics.mode([2, math.nan, 2])
statistics.multimode([2, math.nan, 2])
statistics.mode([2, math.nan, 0, math.nan, 5])
statistics.multimode([2, math.nan, 0, math.nan, 5])

u, v = np.array(u), np.array(v)
mode_ = scipy.stats.mode(u)
mode_
mode_ = scipy.stats.mode(v)
mode_

mode_.mode
mode_.count

u, v, w = pd.Series(u), pd.Series(v), pd.Series([2, 2, math.nan])
u.mode()
v.mode()
w.mode()

## Variance
n = len(x)
mean_ = sum(x) / n
var_ = sum((item - mean_)**2 for item in x) / (n - 1)
var_

var_ = statistics.variance(x)
var_

statistics.variance(x_with_nan) # Raises StatisticsError

var_ = np.var(y, ddof=1)
var_
var_ = y.var(ddof=1)
var_

np.var(y_with_nan, ddof=1)
y_with_nan.var(ddof=1)

np.nanvar(y_with_nan, ddof=1)

z.var(ddof=1)
z_with_nan.var(ddof=1)

## Standard Deviation
