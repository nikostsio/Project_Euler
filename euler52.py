#  Generate the lsit of numbers
from itertools import permutations

numbers = []
p = 5
num = 10**p
while True:
	if num*6<10**(p+1):
		numbers.append(num)
	else:
		p+=1
		num = 10**p
	if p == 6:
		break
	num+=1
def check(n, m):
	p = [int(''.join(i)) for i in list(permutations(str(n)))]
	for i in range(2,m+1):
		if n*i not in p:
			return False
	return True
def main():

	# print(check(142857,6))
	for i in numbers:
		print(i)
		if check(i,6):
			print(f'--->{i}<----')
			break
if __name__=='__main__':
	main()