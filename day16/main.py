# https://adventofcode.com/2017/day/16
import sys
import re

def swap(line_dance: list[str], i: int, j: int) -> str:
    tmp = line_dance[i]
    line_dance[i] = line_dance[j]
    line_dance[j] = tmp
    return "".join(line_dance)

def swap_chars(line_dance: list[str], i: str, j: str) -> str:
    i_ind = line_dance.index(i)
    j_ind = line_dance.index(j)
    line_dance[j_ind] = i
    line_dance[i_ind] = j
    return "".join(line_dance)

def spin(line_dance: str, i: int):
    return line_dance[-i:] + line_dance[:len(line_dance)-i]

def p1(line_dance: str, instructions: list[str]) -> str:
    for instruction in instructions:
        if instruction[0] == 's':
            num = int(re.findall(r'\d+', instruction[1:])[0])
            line_dance = spin(line_dance, num)
        elif instruction[0] == 'x':
            nums = re.split(r'\/', instruction[1:])
            line_dance = swap(list(line_dance), int(nums[0]), int(nums[1]))
        elif instruction[0] == 'p':
            programs = re.split(r'\/', instruction[1:])
            line_dance = swap_chars(list(line_dance), programs[0], programs[1])
    return line_dance

def p2(line_dance: str, instructions: list[str]) -> str:
    DANCE_TOTAL = 1_000_000_000
    program_orders = {}
    
    for i in range(DANCE_TOTAL):
        line_dance = p1(line_dance, instructions)
        # entered a cycle
        if line_dance in program_orders and i != program_orders[line_dance]:
            break
        if line_dance not in program_orders:
            program_orders[line_dance] = i+1
    for line, index in program_orders.items():
        if index == DANCE_TOTAL % len(program_orders):
            line_dance = line
            break
    return line_dance

if __name__ == "__main__":
    input = open(sys.argv[1]).read().split(',')
    line_dance = "abcdefghijklmnop"
    print(f"Part 1 Program Order after 1 Dance: {p1(line_dance, input)}")
    print(f"Part 2 Order after 1 Billion Dances: {p2(line_dance, input)}")