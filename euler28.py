def turn_right(curr_dir):
	curr_dir = [-curr_dir[1], curr_dir[0]]
	return curr_dir
def spiral_of(n):
	spiral = [[0 for i in range(n)] for i in range(n)]
	pos = [n//2, n//2]
	direction = [0,-1]
	spiral[pos[0]][pos[1]] = 1
	num = 2
	while num<=n**2:
		if spiral[pos[0]+turn_right(direction)[1]][pos[1]+turn_right(direction)[0]]==0:
			direction = turn_right(direction)
		pos[0]+=direction[1]
		pos[1]+=direction[0]
		spiral[pos[0]][pos[1]] = num
		num+=1
	return spiral

def visual(spiral):
	for i in spiral:
		row = ''
		for num in i:
			row+=str(num)
			row+=' '*(8 - len(str(num)))
		print(row)
# visual(spiral_of(13))
def sum_of_diags_in(spiral):
	diag_sum = -1
	for i in range(len(spiral)):
		diag_sum+= spiral[i][i]
	for j in range(len(spiral)):
		diag_sum+=spiral[j][len(spiral)-1-j]
	return diag_sum
def main():
	print(sum_of_diags_in(spiral_of(1001)))
if __name__=='__main__':
	main()