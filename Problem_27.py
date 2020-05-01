
import os.path

class Prime():
    def __init__(self, filename='listOfPrimes_test.txt'):
        self.filename = filename
        self.primes = []

        if os.path.isfile(filename):
            with open(filename, 'r') as f:
                for line in f:
                    self.primes.append(int(line))
        else:
            with open(filename, 'w') as f:
                f.write('2\n3\n')
                self.primes.append(2)
                self.primes.append(3)
    
    def find(self, max_prime=0, num_of_primes=0):
        with open(self.filename, 'a') as f:
            MAXPRIME = self.primes[-1]
            n = MAXPRIME
            while n <= max_prime or len(self.primes)<num_of_primes:
                for prime in self.primes:
                    if n%prime == 0:
                        break
                else:
                    if n > MAXPRIME:
                        self.primes.append(n)
                        f.write(str(n) + '\n')
                n += 2
    
    def printPrimesList(self, max_prime=0, num_of_primes=0):
        i = 0
        try:
            while (self.primes[i] <= max_prime or i<num_of_primes) and i < len(self.primes):
                print(self.primes[i], end=', ')
                i += 1
        except IndexError:
            pass
        print('')
    
    def isPrime(self, n):
        if n>(self.primes[-1])**2-1:
        # if n>(self.primes[-1]):
            self.find(max_prime=(int(n**0.5)+1))
        if n == 1:
            return False
        for prime in self.primes:
            if n == prime:
                return True
            elif n % prime == 0:
                return False
        return True
    
    def primesList(self):
        return self.primes



class Quadratic:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def __str__(self):
        return f"n^2 {'+' if self.a>0 else '-'} {self.a if self.a>0 else -1*self.a}*n {'+' if self.b>0 else '-'} {self.b if self.b>0 else -1*self.b}"

    def apply(self, n):
        return (n*n + self.a * n + self.b)

A = 1000
B = 1000

def main():

    prime = Prime()
    max_n = []
    max_n_quadratic = []
    for a in range(-A+1, A):
        for b in range(-B, B+1):
            n = 0
            quad = Quadratic(a, b)
            # print(quad, end='')
            while prime.isPrime(abs(quad.apply(n))):
                n += 1
            # print(f"    -   {n}")
            # if n>0:
            #     print(f"{quad}    -   {n}")
            try:
                if n>max_n[-1]:
                    max_n_quadratic.append(Quadratic(a, b))
                    max_n.append(n)
            except IndexError:
                max_n_quadratic.append(Quadratic(a, b))
                max_n.append(n)

    print(f"max_n: {max_n[-1]}\nQuadratic: {max_n_quadratic[-1]}")

    for i in range(max_n[-1]):
        print(max_n_quadratic[-1].apply(i))

if __name__ == '__main__':
    main()