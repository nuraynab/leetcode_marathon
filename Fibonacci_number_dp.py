###Recursive solution
def fib(n):
	if n <= 1:
		return n
	else:
		return fib(n-1) + fib(n-2)
print(fib(10))


def fib_m(n):
	table = {}
	return fib_m_helper(n, table)

def fib_m_helper(n, table):
	if n not in table:
		if n <= 1:
			table[n] = n
		else:
			table[n] = fib_m_helper(n-1, table) + fib_m_helper(n-2, table)
	return table[n]

print(fib_m(10))

def fib_t(n):
	fib = {}
	fib[0] = 0
	fib[1] = 1
	for i in range(2, n + 1):
		fib[i] = fib[i-1] + fib[i-2]
	return fib[n]
print(fib_t(10))

def fib_easy(n):
	first = 0
	second = 1
	for i in range(2, n + 1):

		num = first + second 
		first = second 
		second = num 
	return num

print(fib_easy(10))