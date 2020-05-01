POWER = 5
def main():
    figures = 1
    for i in [10**n-1 for n in range(1,100)]:
        # print(f"{len(str(i))} -- {len(str(sum([i**POWER for i in [int(a) for a in str(i)]])))}")
        figures = len(str(i))
        if len(str(i)) == len(str(sum([i**POWER for i in [int(a) for a in str(i)]]))):
            break
    # print(10**(figures-1))
    result = 0
    for i in range(1, 10**figures):
        if i == sum([i**POWER for i in [int(a) for a in str(i)]]) and i!=1:
            result += i
            print(i)
        # if i%1000==0:
        #     print([i**POWER for i in [int(a) for a in str(i)]])
    print(result)

if __name__ == "__main__":
    main()