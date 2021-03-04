# a = '''75
# 95 64
# 17 47 82
# 18 35 87 10
# 20 04 82 47 65
# 19 01 23 75 03 34
# 88 02 77 73 07 63 67
# 99 65 04 28 06 16 70 92
# 41 41 26 56 83 40 80 70 33
# 41 48 72 33 47 32 37 16 94 29
# 53 71 44 65 25 43 91 52 97 51 14
# 70 11 33 28 77 73 17 78 39 68 17 57
# 91 71 52 38 17 14 91 43 58 50 27 29 48
# 63 66 04 68 89 53 67 30 73 16 69 87 40 31
# 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''

# triangle = []
# for string in a.split('\n'):
# 	lst = [int(i) for i in string.split(' ')]
# 	triangle.append(lst)
# print(triangle) 

triangle = [[75], 
[95, 64], 
[17, 47, 82], 
[18, 35, 87, 10], 
[20, 4, 82, 47, 65], 
[19, 1, 23, 75, 3, 34], 
[88, 2, 77, 73, 7, 63, 67], 
[99, 65, 4, 28, 6, 16, 70, 92], 
[41, 41, 26, 56, 83, 40, 80, 70, 33], 
[41, 48, 72, 33, 47, 32, 37, 16, 94, 29], 
[53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14], 
[70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57], 
[91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48], 
[63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31], 
[4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]

# def find_max():
# 	sum_ = 0
# 	(y,x) = (0,0)
# 	while y<14:
# 		# print(y)
# 		if x == 0:
# 			m = max(triangle[y+1][0:2])
# 		else:
# 			m = max(triangle[y+1][x:x+2])
# 		x = triangle[y+1].index(m)
# 		y+=1
# 		sum_+=m
# 	return sum_
# print(find_max())


sum_of_path = 75
def find_best_path(xa,ya):
	global sum_of_path
	paths = []
	if ya<=10:
		add = 4
		for i in range(2):
			for j in range(2):
				for k in range(2):
					for l in range(2):
						paths.append([i,j,k,l])
	elif ya==11:
		add = 3
		for i in range(2):
			for j in range(2):
				for k in range(2):
					paths.append([i,j,k])
	elif ya == 12:
		add = 2
		for i in range(2):
			for j in range(2):
				paths.append([i,j])
	elif ya == 13:
		add = 1
		paths.append([0])
		paths.append([1])
	else:
		return 
	num_paths = []
	sums = []
	for path in paths:
		(x,y) = (xa,ya)
		temp_sum = 0
		tri = []
		for direction in path:
			temp_sum += triangle[y+1][x+direction]
			tri.append(triangle[y+1][x+direction])
			x = triangle[y+1].index(triangle[y+1][x+direction])
			y+=1
		num_paths.append(tri)
		sums.append(temp_sum)
	sum_of_path+=sum(num_paths[sums.index(max(sums))])
	print(num_paths[sums.index(max(sums))])
	print(sum_of_path)
	if add + ya == 15:
		return
	else:
		find_best_path(xa+sum(paths[sums.index(max(sums))]),ya+add)
find_best_path(0,0)