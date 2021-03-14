def is_pandigital(n):
	lst = ['1','2','3','4','5','6','7','8','9']
	num = str(n)
	m = 2
	while len(num)<9:
		num+=str(n*m)
		m+=1
	if len(num)!=9:
		return False
	else:
		for i in num:
			if i in lst:
				del lst[lst.index(i)]
			else:
				return False
		if len(lst)==0:
			return True
		return False
def find_pandigital(n):
	num = str(n)
	m = 2
	while len(num)<9:
		num+=str(n*m)
		m+=1
	return num
def main():

	lst = []
	for i in range(2,100000):
		if is_pandigital(i):
			lst.append(find_pandigital(i))
	print(max(lst))
if __name__=='__main__':
	main()