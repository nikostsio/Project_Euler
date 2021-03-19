import ast
def triangular(n):
	return (n*(n+1))//2
def main():
	file = open("words.txt", "r")
	contents = file.read()
	word_lst = ast.literal_eval(contents)
	word_lst = sorted(word_lst)
	letter_lst = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	triangular_lst = [triangular(i) for i in range(1,50)]
	counter = 0
	for word in word_lst:
		value = 0
		for letter in word:
			value += letter_lst.index(letter)+1
		if value in triangular_lst:
			counter+=1
			# print(word)
	print(counter)
if __name__=='__main__':
	main()