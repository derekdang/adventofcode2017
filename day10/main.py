# https://adventofcode.com/2017/day/10

def copy_reversed(arr,reversed_nums,idx):
    for j,num in enumerate(reversed_nums):
        arr[(idx + j) % len(arr)] = num

def execute_hash(input,arr,index,skip_size):
    for num in input:
        nums_to_reverse = []
        for i in range(num):
            nums_to_reverse.append(arr[(i + index) % len(arr)])
        copy_reversed(arr,list(reversed(nums_to_reverse)),index)
        index = (index + num + skip_size) % len(arr)
        skip_size = skip_size + 1
    return index,skip_size

def p1():
    skip_size = 0
    index = 0
    arr = [x for x in range(256)]
    execute_hash(input,arr,index,skip_size)
    return arr[0] * arr[1]

def p2():
    skip_size = 0
    index = 0
    arr = [x for x in range(256)]
    p2_in = "94,84,0,79,2,27,81,1,123,93,218,23,103,255,254,243" # Modify to test other example hashes
    p2_input = [ord(ch) for ch in p2_in]
    p2_input.extend([17, 31, 73, 47, 23])
    for _ in range(64):
        index,skip_size = execute_hash(p2_input,arr,index,skip_size)
    
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

if __name__ == "__main__":
    input = [94,84,0,79,2,27,81,1,123,93,218,23,103,255,254,243]
    print(f"Part 1 Product of the first two elements after one round: {p1()}")
    print(f"Part 2 Hash of my puzzle input: {p2()}")