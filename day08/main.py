# https://adventofcode.com/2017/day/8
import sys
import re
def eval_condition(condition_expr, condition_reg):
    c_val = registers[condition_reg]
    ret = False
    if condition_expr[0] == ">":
        ret = c_val > condition_expr[1]
    elif condition_expr[0] == ">=":
        ret = c_val >= condition_expr[1]
    elif condition_expr[0] == "<":
        ret = c_val < condition_expr[1]
    elif condition_expr[0] == "<=":
        ret = c_val <= condition_expr[1]
    elif condition_expr[0] == "==":
        ret = c_val == condition_expr[1]
    elif condition_expr[0] == "!=":
        ret = c_val != condition_expr[1]
    return ret

def perform_operation(operation, target_reg):
    t_val = registers[target_reg]
    if operation[0] == "inc":
        t_val = t_val + operation[1]
    else:
        t_val = t_val - operation[1]
    return t_val

if __name__ == "__main__":
    data = open(sys.argv[1]).read().splitlines()
    input = []
    registers = {}
    p2_max_value_seen = -sys.maxsize - 1
    for line in data:
        arr = line.split("if")
        arr = [s.strip() for s in arr]

        instr = arr[0].split()
        condition = arr[1].split()

        target_reg = instr[0]
        operation = (instr[1], int(instr[2]))
        
        condition_reg = condition[0]
        condition_expr = (condition[1], int(condition[2]))

        if target_reg not in registers:
            registers[target_reg] = 0
        if condition_reg not in registers:
            registers[condition_reg] = 0
        
        if eval_condition(condition_expr, condition_reg):
            t_val = perform_operation(operation,target_reg)
            p2_max_value_seen = max(p2_max_value_seen, t_val)
            registers[target_reg] = t_val
        
    max_reg_at_end = max(value for value in registers.values())
    print(f"Part 1 max value in register after instructions: {max_reg_at_end}")
    print(f"Part 2 max value recorded during all instructions: {p2_max_value_seen}")