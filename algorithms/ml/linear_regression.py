def linear_regression(X, Y):
	pass

def derivative(X, Y):
	N = len(X)
	
	if(len(Y) <= N):
		Y = Y[:N]
	else:
		N = len(Y)
		X = X[:N]

	m = 0

	for i in range(1, N):
		m += (Y[i+1] - Y[i])/(X[i+1] - X[i])

	return m/N
