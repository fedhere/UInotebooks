# whitening

    1. What are we doing?

Dividing every feature (column  of a dataframe) by its standard deviation. Thus the new variance of the feature (of every column of your dataframe) is 1.


|obs|feat1|feat2|feat3| ... |feat N|
|-----|-----|-----|-----|-----|-----|
|o1 | y11 | y12 | y13 | ... | y1N |
|o2 | y21 | y22 | y23 | ... | y2N |
|o3 | y31 | y32 | y33 | ... | y3N |
|o4 | y41 | y42 | y43 | ... | y4N |
|...||||||
|oM | yM1 | yM2 | yM3 | ... | yMN |


feat1 -> feat1 / std(feat1)

feat2 -> feat2 / std(feat2)

feat3 -> feat3 / std(feat3)

feat4 -> feat4 / std(feat4)

...

feat N -> feat N / std(feat N)



it is advisable to also normalize the features (so that they have all the same importance it is the definition of the *distance* defines the relative feature importance):

feat1 -> (feat1 - mean(feat1)) / std(feat1)

feat2 -> (feat2 - mean(feat2)) / std(feat2)

feat3 -> (feat3 - mean(feat3)) / std(feat3)

feat4 -> (feat4 - mean(feat4)) / std(feat4)

...

featN -> (featN - mean(featN)) / std(featN)




    2. Why are we doing it?

Removing spurious covariance. Normally we assume that the features are independent when we set up to investigate them with any machine learning method (avoid colinearity in the exogenous variables). In fact, there are different kinds of whitening. Standardization simply sets the variance of each feature to 1, and is what I described above. Full whitening (more complex) transforms the covariance matrix of the feature set to the identity matrix. This can be done if the covariance matrix is invertible. This does remove covariance. 

X is a vector with covariance matrix M, which is not singular (invertible)

W is a matrix <=> W^T W = M^-1 <=> W^T W M = I

then 

Y = WX has covariance I



    3. When NOT to do it?

When the covariance of your features needs to be preserved. For example when you cluster time series: if you want to cluster time series based on similar time evolution you can do that by defining a distance time-stamp-by-time-stamp: for example a Eucledian distance 

    D = Sum\_i (Sum\_j,k |y\_j(t\_i) - y\_k(t\_i)|)

In this case whitening would modify the intrinsic shape of the time series, and thus modify the true distance. 
In this case, however, we normalize the feature vectore by observation (by row) so that the mean of each observattion (row of your dataframe) is 0 and the standard deviation is 1:

obs1 -> (obs1 - mean(obs1)) / std(obs1)

obs2 -> (obs2 - mean(obs2)) / std(obs2)

obs3 -> (obs3 - mean(obs3)) / std(obs3)

obs4 -> (obs4 - mean(obs4)) / std(obs4)

...

obsM -> (obsM - mean(obsM)) / std(obsM)
