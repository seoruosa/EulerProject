def powerDigitSum(a, b):
    result = a**b
    result = [int(i) for i in list(str(result))]
    return sum(result)

def main():
    for i in range(1001):
        print(f"{i} - {powerDigitSum(2, i)}")

if __name__ == '__main__':
    main()