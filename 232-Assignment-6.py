def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

def generate_primes():
    primes_ = []
    i = 2
    while len(primes_)<20:
        if isPrime(i):
            primes_.append(i)
        i += 1
    return primes_

def generate_fakes():
    primes = generate_primes()
    fakes = []
    for i in range(len(primes)-1):
        fakes.append(primes[i] * primes[i+1])

    return fakes