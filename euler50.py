def sieve(n):
	is_prime = [0]+[0]+[1]*(n-2)
	for i in range(2, int(n**(1/2))+1):
		index = i*2
		while index < n:
			is_prime[index] = 0
			index += i
	primes = []
	for i in range(2, n):
		if is_prime[i]:
			primes.append(i)
	return primes

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