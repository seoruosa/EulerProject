from Problem_27 import Prime

def rotate(l, n):
    eqRot = n%(len(l))
    return l[-eqRot:] + l[:-eqRot]

def allNumberRotations(num):
    digits = len(str(num))
    return set([int(rotate(str(num), i)) for i in range(0, digits)])

def main():
    p = Prime()

    print(p.primesList()[-1])
    p.find(max_prime=1000000)
    print(p.primesList()[-1])

    circularPrimes = set()
    for prime in p.primesList():
        if prime not in circularPrimes:
            allRotations = allNumberRotations(prime)
            if all([p.isPrime(n) for n in allRotations]):
                for numOfList in allRotations:
                    circularPrimes.add(numOfList)
                    print(numOfList)
    
    print(len(list(circularPrimes)))


if __name__=='__main__':
    main()