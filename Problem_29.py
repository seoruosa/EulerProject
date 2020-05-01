def main():
    powerSet = set()
    for a in range(2, 101):
        for b in range(2,101):
            powerSet.add(a**b)
    print(len(powerSet))


if __name__=='__main__':
    main()