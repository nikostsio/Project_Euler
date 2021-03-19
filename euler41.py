import math
def isPadnigital(n):
	lst = [str(i) for i in range(1,len(str(n))+1)]
	for dig in str(n):
		if dig in lst:
			del lst[lst.index(dig)]
		else:
			return False
	if len(lst) == 0:
		return True
def isPrime(n):
	if n<=1:
		return False
	for i in range(2,int(math.sqrt(n))+1):
		if n%i==0:
			return False
	return True

def same_digits(n):
	for i in str(n):
		if str(n).count(i)>1:
			return True
	return False
def main():
	for i in range(10001,10000000,2):
		if not same_digits(i) and i%10!=0:
			if isPrime(i) and isPadnigital(i):
				print(i)
if __name__=='__main__':
	main()
