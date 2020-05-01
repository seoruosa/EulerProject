import itertools

def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

class Permutation:
    def __init__(self, listOfElements):
        self.listOfElements = listOfElements
    
    def listAllPermutations(self):
        return list(itertools.permutations(self.listOfElements))
    
    def countPermutations(self):
        return factorial(len(self.listOfElements))

def main():
    p = Permutation([1,2,3,4,5,6,7,8,9])
    print(p.countPermutations())
    print(len(p.listAllPermutations()))

    listIntToString = lambda x: [str(i) for i in x]
    listToInt = lambda x: int(''.join(listIntToString(x)))

    #([(a,b) for (a,b) in list(itertools.combinations(a[:-1],2)) if a>=1 and b<=8 and abs(a-b)>1]):

    allUnusual = set()
    for a in p.listAllPermutations():
        for (k1,k2) in [(1,5), (2,5)]:
            m1 = listToInt(a[:k1])
            m2 = listToInt(a[k1:k2])
            p = listToInt(a[k2:])
            if m1*m2==p:
                print(f"{m1} * {m2} = {p}")
                allUnusual.add(p)
    

    print(sum(allUnusual))


# (1,5), (2,5)
if __name__=='__main__':
    main()