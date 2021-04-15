def isPrime(n):
	if n<=1:
		return False
	for i in range(2,int(n**(1/2))+1):
		if n%i==0:
			return False
	return True

def isPalindromic(n):
	if str(n) == str(n)[::-1]:
		return True
	return False

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

def factorial(n):
	if n==0:
		return 1
	if n == 1:
		return 1
	return n*factorial(n-1)

def to_binary(n):
	rev_bin = ''
	while n>0:
		rev_bin+=str(n%2)
		n//=2
	return rev_bin[::-1]

def isPadnigital(n):
	lst = [str(i) for i in range(1,len(str(n))+1)]
	for dig in str(n):
		if dig in lst:
			del lst[lst.index(dig)]
		else:
			return False
	if len(lst) == 0:
		return True

