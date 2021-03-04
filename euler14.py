def collatz(n):
	num = n
	chain=1
	while num>1:
		if num%2 ==0:
			num = num//2
		else:
			num = 3*num+1
		chain+=1
	return chain

def main():
	lst = []
	lst1 = [i for i in range(1,1000000)]
	for i in range(1,1000000):
		print(i)
		lst.append(collatz(i))
	print(lst1[lst.index(max(lst))])

if __name__ == '__main__':
	main()
