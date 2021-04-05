from itertools import combinations, chain


def isPrime(n):
	for i in range(2,int(n**(1/2))+1):
		if n%i==0:
			return False
	return True
def sieve(n):
	try:
		is_prime = [0]+[0]+[1]*(n-2)
	except:
		print([1]*n)
		return
	for i in range(2, int(n**(1/2))+1):
		index = i*2
		while index < n:
			is_prime[index] = 0
			index += i
	primes = []
	for i in range(2, n):
		if is_prime[i]:
			primes.append(str(i))
	return primes



primes = [i for i in sieve(1000000) if len(i) - len(set(i))>=3]
print(len(primes))






### I generated the dictionairy i wanted to use with the length of the number and the possible parts that can be replaced

# len_dict = {}
# for i in range(2,7):
# 	num = ''.join([str(j) for j in range(i)])
# 	combs = [i for i in chain.from_iterable([list(combinations(num,i)) for i in range(1,len(num)+1)])]
# 	len_dict[len(num)] = combs

### Then i printed the dictionairy and removed the possible ways to replace that included the last digit because if you were to replace that digit
### with numbers 1 - 9 you'd get 5 non-prime numbers

len_dict = {2: [('0',)],
 3: [('0', '1')],
 4: [('0', '1'), ('0', '2'),('1', '2'),('0', '1', '2')], 
 5: [('0', '1'), ('0', '2'), ('0', '3'), ('1', '2'), ('1', '3'), ('2', '3'), ('0', '1', '2'), ('0', '1', '3'), ('0', '2', '3'),('1', '2', '3'),('0', '1', '2', '3')],
 6: [('0', '1'), ('0', '2'), ('0', '3'), ('0', '4'),('1', '2'), ('1', '3'), ('1', '4'),('2', '3'), ('2', '4'), ('3', '4'), ('0', '1', '2'), ('0', '1', '3'), ('0', '1', '4'),('0', '2', '3'), ('0', '2', '4'),('0', '3', '4'),('1', '2', '3'), ('1', '2', '4'),('1', '3', '4'),('2', '3', '4'),('0', '1', '2', '3'), ('0', '1', '2', '4'),('0', '1', '3', '4'),('0', '2', '3', '4'),('1', '2', '3', '4'),('0', '1', '2', '3', '4')]}



# Funcion to find the value of the prime sequence
def find_num(prime):
	prime_lst = [i for i in prime]
	combs = len_dict[len(prime)]
	biggest = 0
	for i in combs:
		fprime = prime_lst[:]
		num_of_primes = 0
		for j in range(10):
			for k in i:
				fprime[int(k)]=str(j)
			# print(int(''.join(fprime)))
			if ''.join(fprime) in primes:
				num_of_primes+=1
		biggest = max(biggest,num_of_primes)
	return biggest

# print(find_num('56003'))

for i in primes:
	print(i)
	if find_num(i)==8:
		print(f'------------------>{i}<-----------------------')
		break