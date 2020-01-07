import collections
def longest_sub(arr):
	substr = collections.defaultdict(int)
	for i in range(len(arr)):
		substr[arr[i]] = 1

	for i in range(1, len(arr)):
		for j in range(i):
			if arr[i] > arr[j] and substr[arr[i]] < substr[arr[j]] + 1:
				substr[arr[i]] = substr[arr[j]] + 1
	max = 0
	for sub_len in substr.values():
		if sub_len > max:
			max = sub_len
	return max

arr = [10, 22, 9, 33, 21, 50, 41, 60]
print(longest_sub(arr))
