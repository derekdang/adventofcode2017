# https://adventofcode.com/2017/day/4
import sys

def p1():
    ans = 0
    for line in data:
        seen = set()
        passphrase = line.split()
        all_unique = True
        for word in passphrase:
            if word in seen:
                all_unique = False
                break
            seen.add(word)
        if all_unique:
            ans = ans + 1
    return ans

def p2():
    ans = 0
    for line in data:
        seen = set()
        passphrase = line.split()
        all_unique = True
        for word in passphrase:
            sorted_word = "".join(sorted(word))
            if sorted_word in seen:
                all_unique = False
                break
            seen.add(sorted_word)
        if all_unique:
            ans = ans + 1
    return ans

if __name__ == "__main__":
    data = open(sys.argv[1]).read().splitlines()
    print(f"Part 1 All valid passphrases with no duplicate words: {p1()}")
    print(f"Part 2 All valid passphrases with no words that are anagrams of each other: {p2()}")