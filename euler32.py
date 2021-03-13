def check(a,b):
	lst = ['1','2','3','4','5','6','7','8','9']
	for i in str(a)+str(b)+str(a*b):
		if i in lst:
			del lst[lst.index(i)]
		else:
			return False
	if len(lst)==0:
		return True
	return False
# print(check(39,186))
def main():

	my_sum = 0
	used = []
	for a in range(1,1000):
		for b in range(10**(4-len(str(a))),10**(4-len(str(a))+1)):
			print(a)
			if check(a,b) and a*b not in used:
				used.append(a*b)
				my_sum+=a*b
	print('Your answer is..')
	print(my_sum)
if __name__ == '__main__':
	main()