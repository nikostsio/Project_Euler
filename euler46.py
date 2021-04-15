from functions import isPrime, sieve
def goldbach_split(n):
	primes = sieve(n)
	for i in range(int(n**(1/2))+1):
		for j in primes:
			if j+2*i**2==n:
				return True
	return False
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