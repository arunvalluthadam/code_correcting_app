def sum_of_multiples(num):
	max = 999
	result = 0
	for i in range(1,max):
		if num*i < max:
			result += num*i
	print result