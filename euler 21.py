def d(n):
	fact_sum = 1
	for i in range(2, n//2+1):
		if n%i==0:
			fact_sum+=i
	return fact_sum
def is_amicable(n):
	if d(d(n)) == n and n != d(n):
		return True
	return False
def main():
	amicable_sum = 0
	for i in range(1,10001):
		if is_amicable(i):
			amicable_sum+=d(i)
	print(amicable_sum)
if __name__ == '__main__':
	main()
