# I'm gonna calculate the square root of 2
# Pretty exciting!!
def main():

	lst = [(3,2), (7, 5)]
	counter = 0
	for i in range(1000):
		# I noticed a pattern in the first few fractions the problem gave, so I tried them and they seem to work!
		denom = lst[-1][1]+lst[-1][0]
		numer = lst[-1][1]+denom
		if len(str(numer))>len(str(denom)):
			counter+=1
		lst.append((numer,denom))
	print(counter)
	print(lst[-1][0]/lst[-1][1])
if __name__=='__main__':
	main()