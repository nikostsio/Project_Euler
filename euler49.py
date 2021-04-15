from itertools import permutations
from functions import isPrime
def check(x,y):
	perms = [''.join(i) for i in permutations(str(x))]
	for i in range(3):
		if not isPrime(x+(i*y)):
			return False
		if str(x+(i*y)) not in perms:
			return False
	return True
def answer(a,b):
	c = str(a)
	for i in range(2):
		c+=str(a+b)
		a+=b
	return c
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