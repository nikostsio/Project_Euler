def to_binary(n):
	rev_bin = ''
	while n>0:
		rev_bin+=str(n%2)
		n//=2
	return rev_bin[::-1]
def check(n):
	if str(n) == str(n)[::-1] and to_binary(n) == to_binary(n)[::-1]:
		return True
	return False
def main():
	s = 0
	for i in range(1,1000000):
		if check(i):
			print(i)
			s+=i
	print('Your answer is...')
	print(s)
if __name__=='__main__':
	main()