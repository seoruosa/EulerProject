
def sum_of_digits(n):
    result = [int(i) for i in list(str(n))]
    return sum(result)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)
    

def main():
    print(sum_of_digits(factorial(100)))

if __name__ == '__main__':
    main()