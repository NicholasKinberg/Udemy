def partitions(n):
	if n == 0:
		result = [[]]
	# if n in memo:
	# 	result[n] = memo[n]
	else:
		result = []
		for i in range(1, n + 1):
			for partition in partitions(n - i):
				result.append([i] + partition)
				# memo = result
	return result

print(partitions(5))