def isPrime(n):
	if n<=1:
		return False
	for i in range(2,int(n**(1/2))+1):
		if n%i==0:
			return False
	return True

def turn_left(curr_dir):
	curr_dir = [curr_dir[1], -curr_dir[0]]
	return curr_dir

def spiral_of(n):
	spiral = [[0 for i in range(n)] for i in range(n)]
	pos = [n//2, n//2]
	direction = [0,1]
	spiral[pos[0]][pos[1]] = 1

	num = 2 
	while num<=n**2:
		if spiral[pos[0]+turn_left(direction)[1]][pos[1]+turn_left(direction)[0]]==0:
			direction = turn_left(direction)
		
		pos[0]+=direction[1]
		pos[1]+=direction[0]
		spiral[pos[0]][pos[1]] = num 
		num+=1
	return spiral

def pad(arr):
	return ', '.join(str(i).rjust(3) for i in arr)

def visual(n):
	return '\n'.join(pad(x) for x in spiral_of(n))
# print(visual(5))
def diagonals(n):
	spiral = spiral_of(n)
	return [
		spiral[i][i]
		for i in range(n)
	] + [
		spiral[n-1-i][i]
		for i in range(n)
		if i!=n//2
	]


def euler58():
	i = 7
	while True:
		c = 0
		d = diagonals(i)
		for j in d:
			if isPrime(j):
				c+=1
		per = 100.0*(c/(i*2-1))
		print(f'{i}: {per}')
		if per<10:
			print(f'-->{i}<--')
		print(i)
		i+=2
# euler58()

# Figured out a way to only generate the diagonals
def euler58_():
	lst = [3,5,7]
	c = 3
	for i in range(5,30001,2):
		a = lst[-3]+(len(lst)//3*8+2)
		b = len(lst)//3+1
		lst.extend([a,a+2*b,a+4*b])
		c+=len([
			i
			for i in [a,a+2*b,a+4*b]
			if isPrime(i)
		])
		if (c/(i*2-1))<0.1:
			print(f'-->{i}<--')
			break
		print(i)
euler58_()
