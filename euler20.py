def factorial(n):
	if n == 1:
		return 1
	return n*factorial(n-1)
def find_sum(n):
	n = str(n)
	sum_ = 0
	for num in n:
		sum_ += int(num)
	return sum_
def main():
	print(find_sum(factorial(100)))
if __name__ == '__main__':
	main()