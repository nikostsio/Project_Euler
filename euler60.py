from functions import sieve, isPrime
primes = sieve(1000)[1:]
def sum_of_digits(n):
	return sum([int(i) for i in str(n)])


for idx, i in enumerate(primes):
	# if idx == 1:
	# 	break
	s = set()
	for j in primes:
		if isPrime(int(str(j)+str(i))) and isPrime(int(str(i)+str(j))):
			s.add(j)
	print(s)
	# s = set([j for j in primes if isPrime(int(str(j)+str(i))) and isPrime(int(str(i)+str(j)))])

	# s = set(lst)
	# print(lst)
	# for j in s:
	# 	if len(set([k for k in primes if isPrime(int(str(k)+str(j))) and isPrime(int(str(j)+str(k)))]))>len(lst):
	# 		lst = [j]+[k for k in primes if isPrime(int(str(k)+str(j))) and isPrime(int(str(j)+str(k)))]
