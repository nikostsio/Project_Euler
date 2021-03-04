def prime_checker(n):
	prime = 0
	for i in range(2, n):
		if n%i==0:
			prime = -1
			break
	if prime == -1:
		return False
	else:
		return True
def main():

	num = 2
	index = 1
	while True:
		if prime_checker(num):
			print(index, '-->',num)
			index+=1
		if index==10002:
			break
		num+=1
if __name__ == '__main__':
	main()