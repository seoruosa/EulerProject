from Problem_20 import factorial

def permutations(itens_list, repetition=False):
    number_itens = len(list(set(itens_list))) if not(repetition) else len(itens_list)
    return factorial(number_itens)

DIGITS = [i for i in range(10)]

def element_of_lexico_permutation(position, digits):
    number = []
    # order digits
    order_digits = digits[:]
    order_digits.sort()

    n_permutations = 0
    while len(number)<len(digits):
        i = 0
        while n_permutations+permutations(order_digits[:-1])<=position:
            n_permutations += permutations(order_digits[:-1])
            i += 1
        number.append(order_digits.pop(i))
    return number

def main():
    print(int(''.join([str(i) for i in element_of_lexico_permutation(1000000-1, DIGITS)])))

if __name__ == "__main__":
    main()

"""
0 1 2 3 4

4 elemento:
    0 - 4! p = 24
"""