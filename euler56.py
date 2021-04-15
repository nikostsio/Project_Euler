def dig_sum(n):
	return sum([int(i) for i in str(n)])
s_lst = []
for a in range(100):
	for b in range(100):
		s_lst.append(dig_sum(a**b))
def main():
	print(max(s_lst))
if __name__=='__main__':
	main()