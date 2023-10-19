# https://adventofcode.com/2017/day/13
import sys
import copy
from tqdm import tqdm

def process_scanner(map: dict):
    for layer in map:
        layer_size, increasing, scanner_pos = map[layer][0], map[layer][1], map[layer][2]
        if increasing:
            if scanner_pos == layer_size - 1:
                map[layer] = layer_size, False, scanner_pos - 1
            else:
                map[layer] = layer_size, True, scanner_pos + 1
        else:
            if scanner_pos == 0:
                map[layer] = layer_size, True, scanner_pos + 1
            else:
                map[layer] = layer_size, False, scanner_pos - 1

# map[key] = (size of layer, True = increasing, scanner pos)
def p1(map: dict) -> int:
    ans = 0
    start, stop = min(map.keys()), max(map.keys())
    for pos in range(start, stop+1):
        if pos in map:
            if map[pos][2] == 0:
                ans += (pos * map[pos][0])
        process_scanner(map)
    return ans    

def mod_p1(map: dict) -> bool:
    start, stop = min(map.keys()), max(map.keys())
    for pos in range(start, stop+1):
        if pos in map:
            if map[pos][2] == 0:
                return False
        keys_to_pop = [key for key in map if key < pos]
        for key in keys_to_pop:
            map.pop(key)
        process_scanner(map)
    return True

def p2(map: dict) -> int:
    cpy = copy.deepcopy(map)
    for i in tqdm(range(1,10000000)):
        if i > 1:
            cpy = cpy_for_next
        process_scanner(cpy)
        cpy_for_next = copy.deepcopy(cpy)
        if mod_p1(cpy):
            return i
    return -1

if __name__ == "__main__":
    raw = open(sys.argv[1]).read().splitlines()
    map = {}
    for line in raw:
        arr = line.split(':')
        layer = int(arr[0])
        size = int(arr[1].strip())
        map[layer] = size, True, 0
    print(f"Part 1 Severity Score: {p1(copy.deepcopy(map))}")
    print(f"Part 2 # of Picoseconds to wait to make it without getting caught: {p2(copy.deepcopy(map))}") # takes 12-15 mins