from itertools import permutations
file = open('cipher.txt')
f = [i for i in file]
lst = f[0].split(',')
file.close()
# def encrypt(source, key):
# 	res = ''
# 	for i in range(len(source)):
# 		res+=chr((ord(source[i]) ^ ord(key[i%len(key)])))
# 	return res
def problem59():
	combs = list(permutations('abcdefghijklmnopqrstuvwxyz', 3))
	counter = 0
	for j in combs:
		if counter%500==0:
			print('Working on it...')
		txt = ''
		for i in range(len(lst)):
			a = chr(int(lst[i])^ord(j[i%3]))
			txt+=chr(int(lst[i])^ord(j[i%3]))
		if 'and ' in txt and 'the ' in txt:
			print('Done!')
			print(f'\nDecrypted text was:\n{txt}')
			print(f"Password was: '{''.join(j)}'")
			print(f'The sum of the original ascii codes is: {sum([ord(i) for i in txt])}')
			break
		counter +=1
def main():
	problem59()
if __name__ == '__main__':
	main()