# Using program of problem 3...
import os.path

MAX = 2000000

def main():
    FileName = 'listOfPrimes.txt'
    primes = []
    if os.path.isfile(FileName):
        with open(FileName, 'r') as f:
            for line in f:
                primes.append(int(line))
    primes_f = [prime for prime in primes if prime < MAX]

    print(sum(primes_f))

if __name__ == '__main__':
    main()