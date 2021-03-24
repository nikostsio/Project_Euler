# According to wikipedia
def wikiPentagonal(n):
	if (((24*n+1)**(1/2))+1)%6==0:
		return True
	return False
def wikiHexagonal(n):
	if (((8*n+1)**(1/2))+1)%4==0:
		return True
	return False
num = 2
counter = 0
running = True
while running:
	Tn = num*(num+1)/2
	if wikiPentagonal(Tn) and wikiHexagonal(Tn):
		print(Tn)
		counter +=1
	if counter == 2:
		running = False
	num+=1