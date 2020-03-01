
def decimal_rep(numr, denr):
    word = str(numr//denr)
    rem = numr%denr
    rem_list = []
    recurring = ''

    if rem != 0:
        word += '.'
    while rem!=0 and (rem not in rem_list):
        rem_list.append(rem)
        rem = rem*10
        word += str(rem//denr)
        rem = rem % denr
    if rem in rem_list:
        recurring = word[rem_list.index(rem)+2:]
        non_recurring = word[:rem_list.index(rem)+2]
    else:
        non_recurring = word
    return (word, non_recurring, recurring)


def main():
    max_rec = ''
    max_d = 0
    for d in range(1, 1001):
        word, non_rec, rec = decimal_rep(1,d)
        if len(rec)>len(max_rec):
            max_rec = rec
            max_d = d
    word, non_rec, rec = decimal_rep(1,max_d)
    print(f"{max_d}\n{word}\n{non_rec}\n{rec}")

if __name__ == "__main__":
    main()