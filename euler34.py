from functions import factorial
def check(n):
	fact_sum = 0
	for dig in str(n):
		fact_sum += factorial(int(dig))
	if fact_sum == n:
		return True
	return False

def main():

	my_sum = 0
	for i in range(3,100000):
		if check(i):
			my_sum+=i
	print(my_sum)
if __name__=='__main__':
	main()