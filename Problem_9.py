# https://projecteuler.net/problem=9

def main():
    l = [i*i for i in range(1,1000)]
    pythagorean_triplet = []
    for a in l:
        for b in l:
            for c in l:
                if(a+b == c):
                    triplet = {'a':a,'b':b, 'c':c}
                    pythagorean_triplet.append(triplet)
                    print(triplet)

    for triplet in pythagorean_triplet:                    
        if(triplet['a']**0.5+triplet['b']**0.5+triplet['c']**0.5 == 1000):
            print(f"\n\n{triplet}\n\n")
            print((triplet['a']**0.5)*(triplet['b']**0.5)*(triplet['c']**0.5))

if __name__ == "__main__":
    main()

    # a + b + c == 1000 & a*a + b*b == c*c
    # a = 1000 - (b+c)
    # a, b, c > 1
    # b+c < 998 => b<998-c
    # b < 997