import math
def factor_quantity(n):
	quantity = 0
	for i in range(1,math.ceil(math.sqrt(n))+1):
		if n%i == 0:
			quantity += 2
		if i*i == n:
			quantity -= 1
	return quantity
def main():
	number = 1
	for i in range(2,1000000):
		number+=i
		if factor_quantity(number)>500:
			print(number)
			break
if __name__ == '__main__':
	main()

