def linear_regression(X, Y):
	alpha_ = alpha(X, Y)
	beta_ = beta(X, Y)
	Y_pred = []
	for i in range(0, len(Y)):
		Y_pred.append(alpha_ + beta_*X[i])
	return Y_pred

def beta(X, Y):
	return cov(X, Y)/(variance(X))
def alpha(X, Y):
	return mean(Y) - beta(X, Y)*mean(X)

def mean(Z):
	return sum(Z)/len(Z)

def std(Z):
	import math
	return math.sqrt(variance(Z))

def variance(Z):
	err = 0
	z_bar = mean(Z)
	N = len(Z)
	for i in range(0, N):
		err += (Z[i] - z_bar)**2
	return err/(N-1)

def cov(X, Y):
	X_bar = mean(X)
	Y_bar = mean(Y)
	cov = 0

	N = min([len(X), len(Y)])
	for i in range(0, N):
		cov += (X[i] - X_bar)*(Y[i] - Y_bar)
	return cov/(N-1)

def corr(X, Y):
	return cov(X, Y)/(std(X)*std(Y))

def r_2(X, Y):
	return corr(X, Y)**2