import statistics as stats
import numpy as np
def part(n):
    if n == 0:
        result = [[]]
	# if n in memo:
	# 	result[n] = memo[n]
    else:
        result = []
        for i in range(1, n + 1):
            for parts in part(n - i):
                result.append([i] + parts)
				# memo = result
    return result

def flattenHeterogeneous(result):
	flattened_array = []
	for element in result:
		if isinstance(element, list):
			flattened_array.extend(flattenHeterogeneous(element))
		else:
			result.append(element)
	return result

def summaryStatistics(result):
	result = np.array(result)
	result = result.flatten()
	maxResult = max(result)
	minResult = min(result)
	rangeOfResult = maxResult - minResult
	averageResult = stats.mean(result)
	medianResult = stats.median(result)
	return "Range: " + str(rangeOfResult) + " Average: " + str(averageResult) + " Median: " + str(medianResult)
  

result = part(5)
print(flattenHeterogeneous(result))
print(summaryStatistics(result))