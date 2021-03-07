import math
def prime_checker(n):
	if n<=0:
		return False
	for i in range(2,int(math.sqrt(n))+1):
		if n%i==0:
			return False
	return True
def find_ns(a, b):
	n = 0
	while prime_checker(n**2+a*n+b):
			n+=1
	return n
def main():
	n_lst = []
	ab_lst = []
	for a in range(-1000,1000):
		for b in range(-1001,1001):
			n_lst.append(find_ns(a,b))
			ab_lst.append((a,b))
	print(ab_lst[n_lst.index(max(n_lst))])
	print(ab_lst[n_lst.index(max(n_lst))][0]*ab_lst[n_lst.index(max(n_lst))][1])
if __name__=='__main__':
	main()
