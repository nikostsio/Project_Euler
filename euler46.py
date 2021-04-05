import math
def isPrime(n):
	if n<=1:
		return False
	for i in range(2,int(math.sqrt(n))+1):
		if n%i==0:
			return False
	return True
def goldbach_split(n):
	primes = [i for i in range(n) if isPrime(i)]
	for i in range(int(math.sqrt(n))+1):
		for j in primes:
			if j+2*i**2==n:
				return True
	return False
# print(goldbach_split(33))
def main():

	i = 9
	while True:
		if not isPrime(i):
			if not goldbach_split(i):
				print('-------->',i,'<--------')
				break
			else:
				print(i)
		i+=2
if __name__=='__main__':
	main()