def linear_regression(X, Y):
	pass

def mean(Z):
	return sum(Z)/len(Z)

def std(Z):
	import math
	err = 0
	z_bar = mean(Z)
	N = len(Z)
	for i in range(0, N):
		err += (Z[i] - z_bar)**2
	return math.sqrt(err/(N-1))

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