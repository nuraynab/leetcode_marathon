def longest_common_sub(s1, s2):
	n = len(s1) + 1
	m = len(s2) + 1
	L = [[0] * m for i in range(n)]
	for i in range(n):
		for j in range(m):
			if i == 0 or j == 0:
				L[i][j] = 0
			elif s1[i - 1] == s2[j - 1]:
				L[i][j] = L[i-1][j-1] + 1
			else:
				L[i][j] = max(L[i-1][j], L[i][j-1])
	return L[n-1][m-1]

s1 = "AGGTAB"
s2 = "GXTXAYB"
print(longest_common_sub(s1, s2))