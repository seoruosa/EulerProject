def collatz_sequence(n):
    seq = [n]
    while seq[-1] != 1:
        if seq[-1]%2 == 0:
            seq.append(seq[-1]//2)
        else:
            seq.append(3*seq[-1]+1)
    return(seq)

def collatz_sequence_len(n):
    el = n
    seq_len = 1
    while el != 1:
        if el%2 == 0:
            el = el//2
        else:
            el = 3*el+1
        seq_len += 1
    return(seq_len)

def main():
    max_len = 0
    seed = 1
    for i in range(1,1000000):
        len_seq = collatz_sequence_len(i)
        if len_seq>max_len:
            max_len = len_seq
            seed = i
    print(f"len:  {max_len} \nseed: {seed}  \n\n\n {collatz_sequence(seed)}")

if __name__ == '__main__':
    main()