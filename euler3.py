import math
def prime_checker(n):
	for i in range(2,int(math.sqrt(n)+1)):
		if n%i==0:
			return False
	return True
def main():

	n = 0
	for i in range(1, int(math.sqrt(600851475143))+1):
		if prime_checker(i) and 600851475143%i == 0:
			print(i)
if __name__ == '__main__':
	main()


