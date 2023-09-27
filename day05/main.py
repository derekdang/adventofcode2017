# https://adventofcode.com/2017/day/5
import sys

def p1():
    step_no,idx = 0,0
    p1_input = input.copy()
    while idx < len(p1_input):
        tmp = p1_input[idx]
        p1_input[idx] = p1_input[idx] + 1
        idx = idx + tmp
        step_no = step_no + 1
    return step_no

def p2():
    step_no,idx = 0,0
    p2_input = input.copy()
    while idx < len(p2_input):
        tmp = p2_input[idx]
        if tmp >= 3:
            p2_input[idx] = p2_input[idx] - 1
        else:
            p2_input[idx] = p2_input[idx] + 1
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