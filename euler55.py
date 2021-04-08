def isPalindromic(n):
	if str(n) == str(n)[::-1]:
		return True
	return False
def isLychrel(n):
	for i in range(50):
		n+=int(str(n)[::-1])
		if isPalindromic(n):
			return False
	return True
def main():
	l_count = 0
	for i in range(10001):
		if isLychrel(i):
			# print(i)
			l_count+=1
	print(l_count)
if __name__=='__main__':
	main()