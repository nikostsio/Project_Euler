from functions import sieve
def factors(n,primes):
    factors = []
    for i in primes:
        if n%i == 0:
            n /= i
            factors.append(i)
    return factors
def main(): 
    primes = sieve(20000)
    for j in range(0,1000000):
        if  j%1000 == 0:
            print(j)
        if all(len(factors(j+i,primes))==4 for i in range(4)):
            print(f'----------->{j}<-------------')
            break
if __name__ == '__main__':
    main()