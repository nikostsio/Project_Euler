import sys
# According to wikipedia
def wikiPentagonal(n):
	if (((24*n+1)**(1/2))+1)%6==0:
		return True
	return False
def main():
	j = 0
	while True:
		print(j)
		for k in range(1,j):
			pent_j=j*(3*j-1)//2
			pent_k=k*(3*k-1)//2
			if wikiPentagonal(pent_j+pent_k) and wikiPentagonal(abs(pent_j-pent_k)):
				print(pent_j,'-',pent_k,'=',abs(pent_j-pent_k))
				sys.exit()

		j+=1
if __name__=='__main__':
	main()
