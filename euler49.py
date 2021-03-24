import math
import sys
from itertools import permutations
def isPrime(n):
	if n<=1:
		return False
	for i in range(2,int(math.sqrt(n))+1):
		if n%i==0:
			return False
	return True
def check(x,y):
	perms = permutations(str(x))
	better_perms = []
	for perm in perms:
		better_perms.append(''.join(perm))
	for i in range(3):
		if not isPrime(x+(i*y)):
			return False
		if str(x+(i*y)) not in better_perms:
			return False
	# if all(isPrime(x+(i*y)) and str(x+(i*y)) in better_perms for i in range(3)):
	return True
def answer(a,b):
	c = str(a)
	for i in range(2):
		c+=str(a+b)
		a+=b
	return c
print(answer(2969,3330))

def main():
	for a in range(1488,10000):
		print(a)
		for b in range(1,(10000-a)//2):
			if check(a,b):
				print(f'------>{a,b}<------')
				print(answer(a,b))
				sys.exit()

if __name__=='__main__':
	main()