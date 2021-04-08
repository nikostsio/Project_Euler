def factorial(n):
	if n<=1: 
		return 1
	return n*factorial(n-1)
def num_of_combs(a,b):
	return factorial(a)/(factorial(b)*factorial(a-b))
def main():

	c = 0
	for a in range(100,0,-1):
		# print(a)
		for b in range(0,a):
			if num_of_combs(a,b)>10**6:
				c+=1
	print(c)
if __name__=='__main__':
	main()
# print(num_of_combs(5,3))