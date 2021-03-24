import time
def prim(n,primes):
    for i in primes:
        if n%i == 0:
            return False
def factors(n,primes):
    factors = []
    for i in primes:
        if n%i == 0:
            n /= i
            factors.append(i)
    return factors
def main(): 
    primes = [2]
    for i in range(2,10000):
        if prim(i,primes) == None:
            primes.append(i)
    for j in range(0,1000000):
        if  j%1000 == 0:
            print(j)
        if all(len(factors(j+i,primes))==4 for i in range(4)):
            print(f'----------->{j}<-------------')
            break
if __name__ == '__main__':
    main()