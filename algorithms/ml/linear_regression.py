def linear_regression(X, Y):
	pass

def mean(Z):
	return sum(Z)/len(Z)

def std(Z):
	import math
	err = 0
	z_bar = mean(Z)
	N = len(Z)
	for i in range(1, N):
		err += (Z[i] - z_bar)**2
	return math.sqrt(err/(N-1))

def cov(X, Y):
	X_hat = X-mean(X)
	Y_hat = Y-mean(Y)
	N = min([len(X_hat), len(Y_hat)])
	cov = 0
	for i in range(1, N):
		cov += X_hat[i]*Y_hat[i]
	return cov/(N-1)

def corr(X, Y):
	return cov(X, Y)/(std(X)*std(Y))

def r_2(X, Y):
	return corr(X, Y)**2