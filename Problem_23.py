from Problem_21 import proper_divisors
from Problem_12 import divisors

LIMIT = 28123

def abundant_list(n):
    return [i for i in range(1, n+1) if sum(proper_divisors(i))>i]

# array is ordered
def sum_on_list(n, array):
    low, high = (0, len(array)-1)

    while low <= high:
        if n == array[low] + array[high]:
            return (array[low], array[high])

        if array[low] + array[high] < n:
            low += 1
        else:
            high -= 1
    return None


def main():

    abundants = abundant_list(LIMIT)
    # abundants = [12]

    # for i in abundants:
    #     print(f"{i} {proper_divisors(i)} {divisors(i)} -> {sum(proper_divisors(i))}")

    # print(abundants)

    # print([i for i in abundants if i%2!=0])

    # print(sum_on_list(5, [1,3,5,8]))
    non_abundant_sum = [i for i in range(1, LIMIT+1) if sum_on_list(i, abundants) == None]

    print(non_abundant_sum)
    print(f"\n\n{sum(non_abundant_sum)}")

if __name__== '__main__':
    main()