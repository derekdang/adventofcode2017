# https://adventofcode.com/2017/day/5
import sys

def p1():
    step_no,idx = 0,0
    input_copy = input.copy()
    while idx < len(input_copy):
        tmp = input_copy[idx]
        input_copy[idx] = input_copy[idx] + 1
        idx = idx + tmp
        step_no = step_no + 1
    return step_no

def p2():
    step_no,idx = 0,0
    input_copy = input.copy()
    while idx < len(input_copy):
        tmp = input_copy[idx]
        if tmp >= 3:
            input_copy[idx] = input_copy[idx] - 1
        else:
            input_copy[idx] = input_copy[idx] + 1
        idx = idx + tmp
        step_no = step_no + 1
    return step_no

if __name__ == "__main__":
    data = open(sys.argv[1]).read().splitlines()
    input = []
    for line in data:
        input.append(int(line))
    print(f"Part 1 Number of Steps to Exit: {p1()}")
    print(f"Part 2 Number of Steps to Exit: {p2()}")