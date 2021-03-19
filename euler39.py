def find_solutions(p):
	product_lst = []
	counter = 0
	for a in range(1,p):
		for b in range(a,p):
			if a**2+b**2==(p-a-b)**2 and a*b not in product_lst:
				# print(a,b,p-a-b)
				product_lst.append(a*b)
				counter+=1
	return counter
# find_solutions(120)
lst_p = []
lst = []
for p in range(10,1000):
	print(p)
	lst_p.append(p)
	lst.append(find_solutions(p))
print(lst_p[lst.index(max(lst))])
