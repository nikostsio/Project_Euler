from functions import isPrime
def main():

	num = 2
	index = 1
	while True:
		if isPrime(num):
			print(index, '-->',num)
			index+=1
		if index==10002:
			break
		num+=1
if __name__ == '__main__':
	main()