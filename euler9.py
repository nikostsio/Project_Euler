def main():
	for a in range(120,1000):
		for b in range(a+1,1000):
			for c in range(b+1,1000):
				if (a**2)+(b**2) == (c**2):
					print(a,b,c)
					if a+b+c == 1000:
						print(a,b,c, '<-------------...Product is:', a*b*c)
						return
if __name__ == '__main__':
	main()

