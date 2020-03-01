import math
def main():
    print('')    

def triangle_numbers(n):
    return sum([i for i in range(1, n+1)])

def divisors(n):
    LIMIT = int(n**0.5)+1
    l = set()
    for i in range(1,LIMIT):
        if n%i==0:
            l.add(i)
            l.add(n//i)
    l = list(l)
    l.sort()
    return l

def main():
    n = 1
    n_divisors = 0
    while n_divisors<=500:
        triangle = triangle_numbers(n)
        n_divisors = len(divisors(triangle))
        print(f"{n} {triangle} {n_divisors}")
        n += 1

if __name__ == '__main__':
    main()