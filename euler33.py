def check(a,b):
	if a%10==0 and b%10==0:
		return False
	start = a/b
	start_a, start_b = a,b
	for ind, i in enumerate(str(a)):
		if i in str(b):
			a = str(a)[1 -ind]
			b = str(b)[1 - str(b).index(i)]
			break	
	if (start_a, start_b) == (a,b):
		return False
	if b!='0' and int(a)/int(b) == start:
		return True
	return False
def main():

	lst = []
	numer = 1
	denom = 1
	for a in range(10,100):
		for b in range(a+1,100):
			if check(a,b):
				numer*=a
				denom*=b
	print(numer,'/', denom)
	#I was kinda lucky because i saw that the fraction could be easily simplified just by dividing both the enumerator and denominator with 387296
	# Therefore the value of the denominator is equal to: 100
if __name__=='__main__':
	main()