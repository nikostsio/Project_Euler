
num_dict = {'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'T':10,'J':11,'Q':12,'K':13,'A':14}
def find(n, dict_):
	for i in dict_:
		if dict_[i]==n:
			return True, i
	return False, 0
def time_num(n_lst, s_lst):
	the_dict = {}
	shape_dict = {}
	for i in n_lst:
		if i in the_dict:
			the_dict[i] += 1
		else:
			the_dict[i] = 1
	for i in s_lst:
		if i in shape_dict:
			shape_dict[i] += 1
		else:
			shape_dict[i] = 1

	f = (max(shape_dict.values()))
	biggest = 0
	counter = 0
	for i in the_dict:
		if the_dict[i]==2 and len(the_dict)!=2:
			biggest = max(biggest, i)
			counter +=1
	if counter == 0:
		value = 100*0
	if counter == 1:
		value = 100*1+biggest
	if counter == 2:
		value = 100*2
	if find(3, the_dict)[0]:
		value = 100*3+find(3, the_dict)[1]
	if sorted(n_lst) == [min(n_lst)+i for i in range(5)]:
		value = 100*4
	if len(shape_dict)==1:
		value = 100*5
	if len(the_dict)==2 and find(3, the_dict)[0]:
		value = 100*6+find(3, the_dict)[1]
	if find(4, the_dict)[0]:
		value = 100*7+find(4, the_dict)[1]
	if sorted(n_lst) == [min(n_lst)+i for i in range(5)] and len(shape_dict) == 1:
		value = 100*8
	if sorted(n_lst) == [10+i for i in range(5)] and len(shape_dict) == 1:
		value = 100*9	
	return value
def high_cards(lst1, lst2):
	for i in range(len(lst1)-1, -1, -1):
		if lst1[i]==lst2[i]:
			continue
		elif lst1[i]>lst2[i]:
			return 1
		else:
			return 2
def main():
	# Getting the poker hands
	file = open("poker.txt", "r")
	hand_lst = []
	for line in file:
		stripped_line = line.strip()
		hand_lst.append(stripped_line)
	file.close()
	pair_lst = []
	for i in hand_lst:
		pair_lst.append((i[:14],i[15:]))

	winner1 = 0
	for i in pair_lst:
		nums1 = [num_dict[j[0]] for j in i[0].split(' ')]

		shapes1 = [j[1] for j in i[0].split(' ')]
		nums2 = [num_dict[j[0]] for j in i[1].split(' ')]
		shapes2 = [j[1] for j in i[1].split(' ')]
		if time_num(nums1, shapes1)==time_num(nums2, shapes2):
			if high_cards(sorted(nums1), sorted(nums2)) == 1:
				winner1+=1
		elif time_num(nums1, shapes1)>time_num(nums2, shapes2):
			winner1+=1
	print(winner1)
if __name__=='__main__':
	main()




### This is the function I first coded, which names the value of the hand

# def time_num(n_lst, s_lst):
# 	the_dict = {}
# 	shape_dict = {}
# 	for i in n_lst:
# 		if i in the_dict:
# 			the_dict[i] += 1
# 		else:
# 			the_dict[i] = 1
# 	for i in s_lst:
# 		if i in shape_dict:
# 			shape_dict[i] += 1
# 		else:
# 			shape_dict[i] = 1

# 	f = (max(shape_dict.values()))
# 	biggest = 0
# 	counter = 0
# 	for i in the_dict:
# 		if the_dict[i]==2 and len(the_dict)!=2:
# 			biggest = max(biggest, i)
# 			counter +=1
# 	value = ''
# 	if counter == 0:
# 		value = (f'High card {max(the_dict)}')
# 	if counter == 1:
# 		value = (f'One pair {biggest}')
# 	if counter == 2:
# 		value = (f'Two pair {sorted([i for i in the_dict if the_dict[i]==2])}')
# 	if find(3, the_dict)[0]:
# 		value = (f'Three of {find(3, the_dict)[1]}')
# 	if sorted(n_lst) == [min(n_lst)+i for i in range(5)]:
# 		value = (f'Straight {min(n_lst)}-{max(n_lst)}')
# 	if len(shape_dict)==1:
# 		value = (f'Flush with {shape_dict[0]}')
# 	if len(the_dict)==2 and find(3, the_dict)[0]:
# 		value = (f'Full House with {find(3, the_dict)[1]}')
# 	if find(4, the_dict)[0]:
# 		value = (f'Four of -{find(4, the_dict)[1]}')
# 	if sorted(n_lst) == [min(n_lst)+i for i in range(5)] and len(shape_dict) == 1:
# 		value = (f'Straight Flush {min(n_lst)}-{max(n_lst)} with {shape_dict[0]}')
# 	if sorted(n_lst) == [10+i for i in range(5)] and len(shape_dict) == 1:
# 		value = (f'Royal Flush with {shape_dict[0]}')	
# 	return value