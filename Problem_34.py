from math import factorial 

# Find a lower/upper limit where a intersection occurs between two increasing functions
def findIntersectionNatural(f, g, inf=1, sup=1000):
    n=inf
    while n<=sup:
        f_greater_g = f(n)>g(n)
        n += 1
        # print(f"{f(n)} -- {g(n)} -- {f_greater_g}")
        if f_greater_g!=(f(n)>g(n)):
            break
    if f(n)==g(n):
        return (n, n)
    else:
        return (n-1, n)

def main():

    n_dig = max(findIntersectionNatural(lambda n: factorial(9)*n, lambda n: 10**n))
    max_range = max(factorial(9)*n_dig, 10**n_dig)

    curious_numbers = []
    for n in range(10,max_range):
        if sum([factorial(int(i)) for i in str(n)]) == n:
            print(f"{[factorial(int(i)) for i in str(n)]} -- {sum([factorial(int(i)) for i in str(n)])} -- {n}")
            curious_numbers.append(n)

    print(f"Sum of curious numbers: {sum(curious_numbers)}")
if __name__=='__main__':
    main()