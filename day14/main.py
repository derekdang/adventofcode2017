# https://adventofcode.com/2017/day/14

def copy_reversed(arr: list, reversed_nums: list, idx: int):
    for j,num in enumerate(reversed_nums):
        arr[(idx + j) % len(arr)] = num

def execute_hash(input:list, arr: list, index: int, skip_size: int):
    for num in input:
        nums_to_reverse = []
        for i in range(num):
            nums_to_reverse.append(arr[(i + index) % len(arr)])
        copy_reversed(arr, list(reversed(nums_to_reverse)), index)
        index = (index + num + skip_size) % len(arr)
        skip_size = skip_size + 1
    return index,skip_size

def knot_hash(input: str) -> str:
    skip_size = 0
    index = 0
    arr = [x for x in range(256)]
    p2_input = [ord(ch) for ch in input]
    p2_input.extend([17, 31, 73, 47, 23])
    for _ in range(64):
        index, skip_size = execute_hash(p2_input,arr,index,skip_size)
    
    xor_result = []
    for i,num in enumerate(arr):
        if i == 0:
            to_add = num
        elif i % 16 == 0:
            xor_result.append(to_add)
            to_add = num
        else:
            to_add = to_add ^ num
    xor_result.append(to_add)

    knot_hash = ""
    for xor_num in xor_result:
        hex_string = hex(xor_num)
        h_split = hex_string.split("x")
        hexidecimal = h_split[1]
        if len(hexidecimal) == 1:
            hexidecimal = "0" + hexidecimal
        knot_hash = knot_hash + hexidecimal
    return knot_hash

def hex_to_bin(c: str, num_bits) -> str:
    return str(bin(int(c, 16))[2:].zfill(num_bits))

def p1(input: str) -> (int,list):
    num_used_squares = 0
    NUM_BITS = 128
    grid = []
    for i in range(0,128):
        k_hash = knot_hash(input + '-' + str(i))
        bin_str = hex_to_bin(k_hash, NUM_BITS)
        grid.append(bin_str)
        for char in bin_str:
            num_used_squares = num_used_squares + 1 if char == '1' else num_used_squares
    return num_used_squares, grid

def helper(grid: list, visited: set, r: int, c: int):
    if (r,c) in visited or r < 0 or r == 128 or c < 0 or c == 128 or grid[r][c] == '0':
        return

    visited.add((r,c))
    helper(grid, visited, r-1, c)
    helper(grid, visited, r+1, c)
    helper(grid, visited, r, c-1)
    helper(grid, visited, r, c+1)

def p2(grid: list) -> int:
    num_regions = 0
    visited = set()
    for r in range(0,128):
        for c in range(0,128):
            if grid[r][c] == '1' and (r,c) not in visited:
                num_regions += 1
                visited.add((r,c))
                helper(grid, visited, r - 1, c)
                helper(grid, visited, r + 1, c)
                helper(grid, visited, r, c - 1)
                helper(grid, visited, r, c + 1)
    return num_regions

if __name__ == "__main__":
    input = "ffayrhll"
    p1_ans, grid = p1(input)
    print(f"Num of Used Sqaures: {p1_ans}")
    print(f"Num of regions/Islands: {p2(grid)}")