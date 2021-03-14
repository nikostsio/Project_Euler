def euclid(num,d, start, end):
	decimals = ''
	index=1
	while len(decimals)<=end-start:
		num*=10
		# print(num, d)
		if index>=start and index<=end:
			decimals += str(num//d)
		num = num%d
		if num == 0:
			break
		index+=1
	return decimals
def find_pattern(div):
	dec = euclid(1,div, 1,2000)
	for ind in range(100):
		# print(ind)
		start = ind
		rec = ''
		while ind<len(dec)-ind+start:
			if ind>start+1:
				if dec[ind] == dec[start]:
					# print(ind,start)
					try:
						if all(dec[i] == dec[ind+i-start] for i in range(start,ind-start)):
							if len(rec) == 2 and rec[0]==rec[1]:
								return 1
							return len(rec)
					except:
						return start, ind
			rec+=dec[ind]
			ind+=1
	return 0
def main():
	div_lst = []
	len_lst = []
	for i in range(1,1000):
		print(i)
		div_lst.append(i)
		len_lst.append(find_pattern(i))
	print('Your answer is...')
	print(div_lst[len_lst.index(max(len_lst))])
if __name__ == '__main__':
	main()