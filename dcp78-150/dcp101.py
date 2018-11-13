
"""
Return the prime partitions of an even number
using Goldbach's conjecture as a basis
"""

class PrimeGen(object):
    """Generate prime numbers
        Using memoization/dynamic programming store
        data for generating new and holding previously
        generated prime numbers
    """
    def __init__(self):
        self.bound = 1
        self.prime_set = [1, 2]
    def generate(self, upperBound: int):
        if upperBound <= self.bound:
            return
        if upperBound % 2 == 0:
            upperBound -= 1
        # sieve = [True] * ((upperBound - self.bound)/2) #Only have to check odds
        # for i in xrange(self.bound+2, upperBound, 2):

        for i in range(self.bound+2, upperBound+1, 2): #Check only odd numbers
            pflag = True
            for prime in self.prime_set[1:]: #exclude 1 as a prime here
                if i % prime == 0:
                    pflag = False
                    break
            if pflag:
                self.prime_set.append(i)
        #Keep the bound odd
        self.bound = upperBound + (1 if upperBound % 2 == 0 else 0)
    def primes(self, upperBound): #returns list of primes up until bound
        if upperBound > self.bound:
            self.generate(upperBound)
        return [p for p in self.prime_set if p <= upperBound]

class SievePrime(object):
    def __init__(self):
        self.bound = 1
        self.base_list = [1, 2]
        self.prime_list = []
    def gen(self, upperBound):
        sieve = [True] * (upperBound - self.bound - 2 + 1)
        for p in self.prime_list:
            #eliminate things from sieve using already calculated primes
            #first multiple of p after self.bounds+2 (inclusive)
            first_multiple = ((self.bound+2)//p)
            if first_multiple % 2 == 0:
                first_multiple += 1
            else:
                first_multiple += 2
            first_multiple *= p
            print("f mult: ", first_multiple)
            sieve[first_multiple-(self.bound+2)::2*p]=[False]*((upperBound-first_multiple)//(2*p) + 1)
        # print(sieve)
        for x in range(self.bound+2, int(upperBound**0.5)+1, 2):
            i = x - (self.bound+2)
            if sieve[i]:
                sieve[i+2*x::2*x] = [False]*((upperBound-self.bound-2)//(2*x))
        # print(sieve)
        for i in range(0, upperBound-self.bound-1, 2):
            if sieve[i]:
                self.prime_list.append(i+self.bound+2)
        # print(self.prime_list)
        self.bound = upperBound - (1 if upperBound % 2 == 0 else 0)
        return (self.base_list + self.prime_list)

def generate(upperBound: int):
    bound = 1
    prime_set = []
    if upperBound <= bound:
        return
    if upperBound % 2 == 0:
        upperBound -= 1
    # sieve = [True] * ((upperBound - bound)/2) #Only have to check odds
    # for i in xrange(bound+2, upperBound, 2):

    for i in range(bound+2, upperBound+1, 2): #Check only odd numbers
        pflag = True
        for prime in prime_set: #exclude 1 as a prime here
            if i % prime == 0:
                pflag = False
                break
        if pflag:
            prime_set.append(i)
    #Keep the bound odd
    bound = upperBound + (1 if upperBound % 2 == 0 else 0)
    return [1, 2] + [p for p in prime_set if p <= upperBound]
        
def rwh_primes(n):
    #https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*(((n-i*i-1)//(2*i))+1)
    return [1, 2] + [i for i in range(3,n,2) if sieve[i]]

def gen(upperBound):
    bound = 1
    prime_list = []
    base_list = [1, 2]
    sieve = [True] * (upperBound - bound - 2 + 1)
    for p in prime_list:
        #eliminate things from sieve using already calculated primes
        #first multiple of p after bounds+2 (inclusive)
        first_multiple = ((bound+2)//p)
        if first_multiple % 2 == 0:
            first_multiple += 1
        else:
            first_multiple += 2
        first_multiple *= p
        # print("f mult: ", first_multiple)
        sieve[first_multiple-(bound+2)::2*p]=[False]*((upperBound-first_multiple)//(2*p) + 1)
    # print(sieve)
    for x in range(bound+2, int(upperBound**0.5)+1, 2):
        i = x - (bound+2)
        # print(f'{bound}, {upperBound}, {i}, {x}, {((upperBound-(x*2-bound-2))//(2*x))}')
        if sieve[i]:
            # s = ((upperBound-bound-2)//(2*x))
            sieve[i+(x-1)*x::2*x] = [False]*((upperBound-(x*x))//(2*x) + 1)
    # print(sieve)
    for i in range(0, upperBound-bound-1, 2):
        if sieve[i]:
            prime_list.append(i+bound+2)
    # print(prime_list)
    bound = upperBound - (1 if upperBound % 2 == 0 else 0)
    return (base_list + prime_list)

def goldbach_terms(num):
    if num % 2 != 0:
        return [0,0]
    primes = gen(num)
    left = primes[0]
    right = primes[len(primes)-1]
    done = False
    for left in primes:
        for right in reversed(primes):
            if(left+right < num):
                break
            if(left+right == num):
                done = True
                break
        if done:
            break
    return (left, right)

if __name__ == "__main__":
    primes = PrimeGen()
    p_list = generate(1000)
    sprimes = SievePrime()
    sp_list = sprimes.gen(100)
    print(sp_list)
    sp_list = gen(1000)
    p_list.sort()
    print(p_list)
    print(sp_list)
    rwh_list = rwh_primes(1000)
    print("lists identical: ", (p_list==sp_list==rwh_list))

    print(goldbach_terms(10))