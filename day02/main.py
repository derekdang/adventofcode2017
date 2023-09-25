# https://adventofcode.com/2017/day/2
import sys

def p1():
    ans = 0
    for row in input:
        lo = sys.maxsize
        hi = -sys.maxsize-1
        for num in row:
            lo = min(lo,num)
            hi = max(hi,num)
        ans = ans + (hi-lo)
    return ans

def p2():
    ans = 0
    for row in input:
        for idx,denominator in enumerate(row):
            for idy,numerator in enumerate(row):
                if idy == idx:
                    continue
                if numerator % denominator == 0:
                    ans = ans + numerator//denominator
    return ans
            
if __name__ == "__main__":
    data = open(sys.argv[1]).read().splitlines()
    input = []
    for line in data:
        input.append(list(map(int,line.split())))
    p1_checksum = p1()
    print(f"Part 1 Checksum: {p1_checksum}")
    p2_checksum = p2()
    print(f"Part 2 Checksum: {p2_checksum}")