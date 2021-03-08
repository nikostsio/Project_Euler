def main():
	lst = []
	for a in range(2,101):
		for b in range(2,101):
			lst.append(a**b)
	return len(set(lst))
if __name__=='__main__':
	print(main())