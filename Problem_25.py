
N_DIGITS = 1000

def n_digits(n):
    return(len(str(n)))

def main():
    f1 = 1
    f2 = 1

    fibo = f1 + f2
    n = 2
    actual = 0
    while n_digits(fibo)<N_DIGITS:
        actual = fibo
        fibo = (f2 + f1)
        f1 = f2
        f2 = fibo
        n += 1
        # print(actual)

    print(f"\n\n{fibo}\n{n}")

if __name__ == '__main__':
    main()