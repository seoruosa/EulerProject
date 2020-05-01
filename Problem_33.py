def digitOfNumber(num, digit):
    return int(str(num)[digit])

def main():
    num = 1
    den = 1
    for n1 in range(10,99):
        for n2 in range(10, 99):
            try:
                if digitOfNumber(n1,0)==digitOfNumber(n2,1)  and n1!=n2 and n2>n1:
                    if digitOfNumber(n1,1)/digitOfNumber(n2,0) == n1/n2:
                        print(f"1 --> {n1} -- {n2} -- {digitOfNumber(n2,0)}")
                        num *= digitOfNumber(n1,1)
                        den *= digitOfNumber(n2,0)
                elif digitOfNumber(n1,1)==digitOfNumber(n2,0)  and n1!=n2 and n2>n1:
                    if digitOfNumber(n1,0)/digitOfNumber(n2,1) == n1/n2:
                        print(f"2 --> {n1} -- {n2}  -- {digitOfNumber(n2,1)}")
                        num *= digitOfNumber(n1,0)
                        den *= digitOfNumber(n2,1)
                else:
                    pass
            except:
                pass
    print(f"{num}/{den}")

if __name__=='__main__':
    main()