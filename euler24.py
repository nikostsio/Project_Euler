def main():
	num = 1
	for a in range(10):
		for b in [x for x in range(10) if x!=a]:
			for c in [x for x in range(10) if x!=a and x!=b]:
				for d in [x for x in range(10) if x!=a and x!=b and x!=c]:
					for e in [x for x in range(10) if x!=a and x!=b and x!=c and x!=d]:
						for f in [x for x in range(10) if x!=a and x!=b and x!=c and x!=d and x!=e]:
							for g in [x for x in range(10) if x!=a and x!=b and x!=c and x!=d and x!=e and x!=f]:
								for h in [x for x in range(10) if x!=a and x!=b and x!=c and x!=d and x!=e and x!=f and x!=g]:
									for i in [x for x in range(10) if x!=a and x!=b and x!=c and x!=d and x!=e and x!=f and x!=g and x!=h]:
										for j in [x for x in range(10) if x!=a and x!=b and x!=c and x!=d and x!=e and x!=f and x!=g and x!=h and x!=i]:
											print(num)
											if num == 1000000:
												print(str(a)+str(b)+str(c)+str(d)+str(e)+str(f)+str(g)+str(h)+str(i)+str(j))
												return
											num+=1
if __name__ == '__main__':
	 main()