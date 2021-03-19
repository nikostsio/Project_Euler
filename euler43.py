from itertools import permutations
def isPadnigital(n):
	lst = [str(i) for i in range(0,len(str(n)))]
	for dig in str(n):
		if dig in lst:
			del lst[lst.index(dig)]
		else:
			return False
	if len(lst) == 0:
		return True

def rule(n):
	prime_lst = [2,3,5,7,11,13,17]
	for i in range(1,8):
		if int(n[i:i+3])%prime_lst[i-1] != 0:
			return False
	return True
def main():
	pandigital_nums = permutations('0123456789')
	s=0
	for num in pandigital_nums:
		if rule(''.join(num)):
			print()
			s+=int(''.join(num))
	print(s)
if __name__=='__main__':
	main()