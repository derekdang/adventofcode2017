# https://adventofcode.com/2017/day/6
import sys

def p1():
    seen_configurations = set()
    p1_input = input.copy()
    reconfig_no = 1
    while(True):
        max_block = -1
        i = -1
        size = len(p1_input)
        for idx,num in enumerate(p1_input):
            if num > max_block:
                i = idx
                max_block = num
        p1_input[i] = 0
        while max_block > 0:
            p1_input[(i+1)%size] = p1_input[(i+1)%size] + 1
            max_block = max_block - 1
            i = i + 1
        config = "".join(str(s) for s in p1_input)
        if config in seen_configurations:
            break
        seen_configurations.add(config)
        reconfig_no = reconfig_no + 1
    return reconfig_no

def p2():
    seen_configurations = {}
    reconfig_no = 1
    p2_input = input.copy()
    reconfig_no = 1
    while(True):
        max_block = -1
        i = -1
        size = len(p2_input)
        for idx,num in enumerate(p2_input):
            if num > max_block:
                i = idx
                max_block = num
        p2_input[i] = 0
        while max_block > 0:
            p2_input[(i+1)%size] = p2_input[(i+1)%size] + 1
            max_block = max_block - 1
            i = i + 1
        config = "".join(str(s) for s in p2_input)
        if config in seen_configurations:
            if seen_configurations[config] == 2:
                break
            seen_configurations[config] = seen_configurations[config] + 1
        else:
            seen_configurations[config] = 1
        reconfig_no = reconfig_no + 1
    return reconfig_no

if __name__ == "__main__":
    data = open(sys.argv[1]).read()
    input = list(map(int,data.split()))
    p1_ans = p1()
    print(f"Part 1 Num of Redistribution Cycles before a seen configuration: {p1_ans}")
    print(f"Part 2 Num of Redistribution Cycles for a cycle: {p2()-p1_ans}")