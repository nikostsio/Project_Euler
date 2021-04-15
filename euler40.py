def main():
	irr_fraction = ''
	num = 1
	while len(irr_fraction)<1000000:
		irr_fraction+=str(num)
		num+=1

	prod = 1
	for i in range(7):
		prod *= int(irr_fraction[10**i-1])
	print(prod)
if __name__ == '__main__':
	main()