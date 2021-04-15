from functions import isPrime
def check(n):
	n_str = str(n)
	for i in range(len(n_str)):
		if not isPrime(int(n_str[i:len(n_str)])):
			return False
	for i in range(1,len(n_str)):
		if not isPrime(int(n_str[0:i])):
			return False
	return True
def main():
	n = 11
	s = 0
	counter = 0
	while counter < 11:
		if check(n):
			print(n)
			counter += 1
			s+=n
		n+=2
	print('Your answer is...')
	print(s)

if __name__ == '__main__':
	main()