import math
# It makes sense to only go up to square root of n
def prime_checker(n):
	if n <3:
		return True
	for i in range(2, int(math.sqrt(n))+1):
		if n%i==0:
			return False
	return True
def main():
	num = 2
	sum_ = 0
	while True:
		if num>=2000000:
			break
		if num%300000==0:
			print(num)
		if prime_checker(num):
			sum_+=num
		num+=1
	print(sum_)
if __name__ == '__main__':
	main()