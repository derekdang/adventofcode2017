# https://adventofcode.com/2017/day/9
import sys

def eval_input():
    stack = []
    score = 0
    chars_in_garbage = 0
    idx,size = 0,len(input)
    while idx < size:
        ch = input[idx]
        if ch == "{":
            if len(stack) != 0 and stack[len(stack)-1] == "<":
                chars_in_garbage = chars_in_garbage +1 
            else:
                stack.append(ch)
        elif ch == "}" and stack[len(stack)-1] != "<":
            # print(f"Adding {len(stack)} to score")
            score = len(stack) + score
            stack.pop()
        elif ch == "<" and stack[len(stack)-1] != "<":
            stack.append(ch)
        elif ch == ">" and stack[len(stack)-1] == "<":
            stack.pop()
        elif ch == "!":
            idx = idx + 1
        elif stack[len(stack)-1] == "<":
            chars_in_garbage = chars_in_garbage + 1
        idx = idx + 1
    return score,chars_in_garbage

if __name__ == "__main__":
    input = open(sys.argv[1]).read()
    score,chars_in_garbage = eval_input()
    print(f"Part 1 Score of all groups is: {score}")
    print(f"Part 2 Total non canceled chars in garbage is: {chars_in_garbage}")