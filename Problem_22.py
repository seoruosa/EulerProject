FILEPATH = 'p022_names.txt'

def alphabeticalPosition(letter):
    return (ord(letter.lower()) - ord('a') + 1)

def nameScore(name):
    return sum([alphabeticalPosition(letter) for letter in name])

def main():
    with open(FILEPATH, 'r') as f:
        l = [i[1:-1] for i in f.read().split(',')]
    l_sorted = l[:]
    l_sorted.sort()

    total = 0
    for i, name in enumerate(l_sorted):
        total += nameScore(name)*(i+1)
    print(total)


if __name__ == '__main__':
    main()