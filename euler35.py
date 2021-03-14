import math
def isPrime(n):
	if n == 1:
		return False
	for i in range(2, int(math.sqrt(n))+1):
		if n%i==0:
			return False
	return True
# print(isPrime(971))
def isCircular(n):
	n = str(n)
	for start in range(len(n)):
		if not isPrime(int(n[start:len(n)]+n[0:start])):
			return False
	return True
# print(isCircular(71))
counter = 0
for i in range(1,1000000):
	if isCircular(i):
		counter += 1
		print(i)
print('Your answer is...')
print(counter)
