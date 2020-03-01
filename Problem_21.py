from Problem_12 import divisors

def proper_divisors(n):
    return (divisors(n))[:-1]

LIMIT = 10000

def main():
    i=1
    itens_list = {}
    while i<=LIMIT:
        itens_list[i] = proper_divisors(i)
        i+=1
    
    amicable = set()

    for j in itens_list:
        try:
            if j == sum(itens_list[sum(itens_list[j])]) and j != sum(itens_list[j]):
                amicable.add(j)
                amicable.add(sum(itens_list[j]))
        except:
            pass
    print(amicable)

    for i in amicable:
        print(f"{i} {proper_divisors(i)}")
    
    print(f"\n\n {sum(amicable)}")



if __name__ == '__main__':
    main()