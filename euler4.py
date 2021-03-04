def isPalindromic(n):
	reverse = ''
	for i in range(len(n) - 1, -1, -1):
		reverse += n[i]
	if n == reverse:
		return True
	else:
		return False


def main():
	lst = []
	for i in range(100,1000):
		for j in range(100,1000):
			if isPalindromic(str(i*j)):
				lst.append(i*j)
	print(max(lst))

if __name__ == '__main__':
	main()