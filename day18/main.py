# https://adventofcode.com/2017/day/18
import sys

def is_number(s: str) -> bool:
    try:
        int(s)
        return True
    except ValueError:
        return False
    
def set_register(registers: dict, r: str, val: str):
    if is_number(val):
        registers[r] = int(val)
    else:
        registers[r] = registers[val] if val in registers else 0

def add_register(registers: dict, r: str, val: str):
    num = registers[r] if r in registers else 0
    if is_number(val):
        registers[r] = num + int(val)
    else:
        num_v = registers[val] if val in registers else 0
        registers[r] = num + num_v

def mul_register(registers: dict, r: str, val: str):
    if r not in registers:
        registers[r] = 0
        return
    num = registers[r]
    if is_number(val):
        registers[r] = num * int(val)
    else:
        num_v = registers[val] if val in registers else 0
        registers[r] = num * num_v

def mod_register(registers: dict, r: str, val: str):
    num = registers[r] if r in registers else 0
    if is_number(val):
        registers[r] = num % int(val)
    else:
        num_v = registers[val]
        registers[r] = num % num_v

def jump_register(registers: dict, r: str, val: str, index: int) -> int:
    if is_number(r) and int(r) > 0 or (r in registers and registers[r] > 0):
        if is_number(val):
            index += int(val)
        else:
            num_v = registers[val] if val in registers else 0
            index += num_v
        index -= 1
    return index

def process_instr(registers: dict, instr: list[str], send: list[int], receive: list[int], index: int) -> (int, int):
    r = instr[1]
    if instr[0] == 'set':
        set_register(registers, r, instr[2])
    elif instr[0] == 'add':
        add_register(registers, r, instr[2])
    elif instr[0] == 'mul':
        mul_register(registers, r, instr[2])
    elif instr[0] == 'mod':
        mod_register(registers, r, instr[2])
    elif instr[0] == 'jgz':
        index = jump_register(registers, r, instr[2], index)
    elif instr[0] == 'snd':
        num = registers[r] if r in registers else 0
        send.append(num)
        return index + 1, 1
    elif instr[0] == 'rcv':
        if len(receive) == 0:
            return index, 0
        else:
            registers[r] = receive[0]
            receive.pop(0)
    return index + 1, 0

def p1(instructions: list[list[str]]) -> int:
    registers = {}
    most_recent_sound = 0
    index = 0
    while True:
        instr = instructions[index]
        r = instr[1]
        if instr[0] == 'set':
            set_register(registers, r, instr[2])
        elif instr[0] == 'add':
            add_register(registers, r, instr[2])
        elif instr[0] == 'mul':
            mul_register(registers, r, instr[2])
        elif instr[0] == 'mod':
            mod_register(registers, r, instr[2])
        elif instr[0] == 'jgz':
            index = jump_register(registers, r, instr[2], index)    
        elif instr[0] == 'rcv':
            if r in registers and registers[r] != 0:
                return most_recent_sound
        if instr[0] == 'snd':
            most_recent_sound = registers[r] if r in registers else 0
        index += 1

def p2(input: list[list[str]]) -> int:
    num_p1_sent = 0
    registers_p0 = {'p': 0}
    registers_p1 = {'p': 1}
    msq_p0, msq_p1 = [], []
    index_p0, index_p1 = 0, 0
    while True:
        prev_index_p0 ,prev_index_p1 = index_p0, index_p1
        instr_p0 = input[index_p0]
        instr_p1 = input[index_p1]
        index_p0, _ = process_instr(registers_p0, instr_p0, msq_p1, msq_p0, index_p0)
        index_p1, p1_sent = process_instr(registers_p1, instr_p1, msq_p0, msq_p1, index_p1)
        num_p1_sent += p1_sent
        # both waiting on a receive
        if prev_index_p0 == index_p0 and prev_index_p1 == index_p1: 
            return num_p1_sent 

if __name__ == "__main__":
    input = open(sys.argv[1]).read().splitlines()
    input = list(map(lambda s: s.split(' '), input))
    print(f"Part 1 Last Sound Recovered/Played: {p1(input)}")
    print(f"Part 2 Number of times Program 1 sent a value: {p2(input)}")