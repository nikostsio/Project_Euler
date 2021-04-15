from functions import isPrime, isPadnigital

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
