
def main():
	lst = [11,12,13,14,15,16,17,18,19,20]
	num = 2520
	while not all(num%n==0 for n in lst):
		print(num)
		num+=2520
	else:
		print(num)
if __name__ == '__main__':
	main()