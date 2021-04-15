from functions import isPrime
def main():
	n = 0
	for i in range(1, int(600851475143**(1/2))+1):
		if isPrime(i) and 600851475143%i == 0:
			print(i)
if __name__ == '__main__':
	main()


