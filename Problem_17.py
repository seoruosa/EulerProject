# works for n<=1000
def countLetters(n, n_letters=True):
    NUMBERNAME = {0:'', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 
                  10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 
                  17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 
                  60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety', 100:'hundred', 1000:'thousand'}
    NUMBERNAMELETTERS = {n:len(NUMBERNAME[n]) for n in NUMBERNAME}
    n_string = str(n)
    if n > 1000:
        return (-1 if n_letters else 'I dont know how to write')
    if n < 20:
        return (NUMBERNAMELETTERS[n] if n_letters else NUMBERNAME[n])
    if n < 100: 
        return (NUMBERNAMELETTERS[int(n_string[0])*10]+ NUMBERNAMELETTERS[int(n_string[1])] if n_letters else f"{NUMBERNAME[int(n_string[0])*10]} {NUMBERNAME[int(n_string[1])]}")
    if n%1000 == 0:
        return (NUMBERNAMELETTERS[int(n_string[0])]+NUMBERNAMELETTERS[1000] if n_letters else f"{NUMBERNAME[int(n_string[0])]} {NUMBERNAME[1000]}")
    if n%100 == 0:
        return (NUMBERNAMELETTERS[int(n_string[0])]+NUMBERNAMELETTERS[100] if n_letters else f"{NUMBERNAME[int(n_string[0])]} {NUMBERNAME[100]}")
    elif len(n_string) > 2:
        return (NUMBERNAMELETTERS[int(n_string[0])]+NUMBERNAMELETTERS[100]+3+countLetters(int(n_string[1:])) if n_letters else f"{NUMBERNAME[int(n_string[0])]} {NUMBERNAME[100]} and {countLetters(int(n_string[1:]), n_letters=False)}")

def countLettersNumbers(start, end):
    totalCount = 0
    for n in range(start, end):
        totalCount += countLetters(n)
        print(f"{n} -- {countLetters(n, False)} -- {countLetters(n, True)}")
    
    return totalCount

if __name__ == '__main__':
    print(countLettersNumbers(1, 1001))
    # for i in range(123):
    #     print(countLetters(i))