def edit_distance(s1, s2):
	m = len(s1) + 1
	n = len(s2) + 1
	edit  = [[0] * n for i in range(m)]
	for i in range(m):
		for j in range(n):
			if i == 0:
				edit[i][j] = j
			elif j == 0:
				edit[i][j] = i
			elif s1[i-1] == s2[j-1]:
				edit[i][j] = edit[i-1][j-1]
			else:
				edit[i][j] = 1 + min(edit[i-1][j], edit[i][j-1], edit[i-1][j-1])
	return edit[m-1][n-1]

s1 = "CART"
s2 = "MARCH"
print(edit_distance(s1, s2))
