my_dict = {1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',
			10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen'}
dekades = {2:'twenty',3:'thirty',4:'forty',5:'fifty',6:'sixty',7:'seventy',8:'eighty',9:'ninety'}
def one_two_digit(n):
	if n<0:
		print("We only do positives...it isn't that hard but im bored")
		return None
	text = ''
	if n>0 and n<20:
		text += my_dict[n]
	if n>=20 and n<100:
		text += dekades[n//10]
		if n%10!=0:
			text +='-'
			text += my_dict[int(str(n)[1])]
	return text

def text_num(n):
	if len(str(n)) <= 2:
		return one_two_digit(n)
	text = ''
	if n>=100:
		text += my_dict[n//100]
		text += ' hundred '
		if n%100!=0:
			text+='and '
			if str(n)[1] == '0':
				text+=one_two_digit(int(str(n)[2]))
			else:
				text+=one_two_digit(int(str(n)[1:3]))
	if n == 1000:
		text = 'one thousand'
	return text


def letters(text):
	return len(text) - text.count(' ') - text.count('-')

def main():
	sum_ = 0
	for i in range(1,1001):
		sum_+=letters(text_num(i))
	print(sum_)


if __name__ == '__main__':
	main()