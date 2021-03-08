def check(n):
	dig_sum = 0
	for i in str(n):
		dig_sum+=int(i)**5
	if dig_sum == n:
		return True
	return False

def main():

	num = 2
	sum_of = 0
	limit = 500000
	while num<limit:
		if check(num):
			sum_of+=num
			print(num)
		num+=1
	print(f'If all the required numbers are below {limit} your answer is...')
	print(sum_of)
if __name__ == '__main__':
	main()