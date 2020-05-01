"""
The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.
Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
(Please note that the palindromic number, in either base, may not include leading zeros.)
"""

def baseTransformation(number, b1=10, b2=2):
    """Transform a integer number of base b1 to base b2, returns a string"""
    remain = int(number)
    transformed = ''
    while remain >= b2:
        transformed += str(remain%b2)
        remain = remain//2
    if remain!=0:
        transformed += str(remain%b2)
    return transformed[::-1]

def isPalindromic(text):
    return text==str(text)[::-1]

def main():
    bothBasePalindromList = list()
    for n in range(1000000):
        if isPalindromic(str(n)):
            if isPalindromic(baseTransformation(n)):
                bothBasePalindromList.append(n)
                print(n)
    print(sum(bothBasePalindromList))

if __name__ == '__main__':
    main()