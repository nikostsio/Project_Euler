from functions import isPrime
def isCircularPrime(n):
	n = str(n)
	for start in range(len(n)):
		if not isPrime(int(n[start:len(n)]+n[0:start])):
			return False
	return True
# print(isCircularPrime(71))
def main():	
	counter = 0
	for i in range(1,1000000):
		if isCircularPrime(i):
			counter += 1
			print(i)
	print('Your answer is...')
	print(counter)

if __name__=='__main__':
	main()