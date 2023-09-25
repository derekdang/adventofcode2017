# https://adventofcode.com/2017/day/1
from tqdm import tqdm
import sys

def p1():
    ans = 0
    for idx,ch in tqdm(enumerate(data)):
        if idx == len(data)-1:
            if ch == data[0]:
                ans = ans + int(ch)
        elif ch == data[idx+1]:
            ans = ans + int(ch)
    return ans

def p2():
    ans = 0
    size = len(data)
    offset = int(size/2)
    for idx,ch in tqdm(enumerate(data)):
        if ch == data[(idx+offset)%size]:
            ans = ans + int(ch)
    return ans

if __name__ == "__main__":
    data = open(sys.argv[1]).read()
    ans_p1 = p1()
    print(f"Part 1 Sum: {ans_p1}")
    ans_p2 = p2()
    print(f"Part 2 Sum: {ans_p2}")