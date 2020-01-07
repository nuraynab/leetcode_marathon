##time O(n*k), space O(n*k)
def binomial_coeff(n, k):
	table = [[0] * (k + 1) for i in range(n + 1)]
	for i in range(n + 1): 
		for j in range(k + 1):
			if j == 0 or j == i:
				table[i][j] = 1
			else:
				table[i][j] = table[i-1][j] + table[i-1][j-1]
	return table[n][k]
print(binomial_coeff(4, 2))


##time O(n*k), space O(k)
def binomial_coeff2(n, k):
	C = [0] * (k + 1)
	C[0] = 1
	for i in range(1, (n + 1)):
		for j in range(min(i, k), 0, -1):
			C[j] = C[j] + C[j-1]
	return C[k]
print(binomial_coeff2(4, 2))