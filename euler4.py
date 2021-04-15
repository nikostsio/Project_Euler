from functions import isPalindromic
def main():
	lst = []
	for i in range(100,1000):
		for j in range(100,1000):
			if isPalindromic(str(i*j)):
				lst.append(i*j)
	print(max(lst))

if __name__ == '__main__':
	main()