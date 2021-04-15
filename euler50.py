from functions import sieve
def main():
	lim = 1000000
	primes = sieve(lim)
	length = 0
	largest = 0
	last_prime = len(primes)
	# print(len(primes))
	for i in range(len(primes)):
		for j in range(i+length, last_prime):
			s = sum(primes[i:j])
			if s < lim:
				if s in primes:
					length = j-i
					# print(length)
					largest = s
			else:
				break

	print(largest)
	print(length)
if __name__=='__main__':
	main()