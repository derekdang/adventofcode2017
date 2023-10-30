# https://adventofcode.com/2017/day/15
from tqdm import tqdm

def p1(NUM_PAIRS: int) -> int:
    a_val, b_val = A_START, B_START
    count = 0
    for _ in tqdm(range(NUM_PAIRS)):
        a_val = (a_val * A_FACTOR) % DENOMINATOR
        b_val = (b_val * B_FACTOR) % DENOMINATOR
        a_str, b_str = bin(a_val), bin(b_val)
        if a_str[-16:] == b_str[-16:]: # last 16 bits match
            count += 1
    return count

def p2(NUM_PAIRS: int) -> int:
    a_val, b_val = A_START, B_START
    count = 0
    a_list, b_list = [], []
    while len(a_list) < NUM_PAIRS or len(b_list) < NUM_PAIRS:
        a_val = (a_val * A_FACTOR) % DENOMINATOR
        b_val = (b_val * B_FACTOR) % DENOMINATOR
        if a_val % A_CRITERIA == 0 and len(a_list) < NUM_PAIRS:
            a_list.append(bin(a_val))
        if b_val % B_CRITERIA == 0 and len(b_list) < NUM_PAIRS:
            b_list.append(bin(b_val))

    for a_str, b_str in zip(a_list, b_list):
        if a_str[-16:] == b_str[-16:]: # last 16 bits match
            count += 1
    return count

if __name__ == "__main__":
    A_FACTOR, B_FACTOR = 16807, 48271
    A_START, B_START = 722, 354
    A_CRITERIA, B_CRITERIA = 4, 8
    DENOMINATOR = 2147483647
    NUM_PAIRS_P1, NUM_PAIRS_P2 = 40000000, 5000000
    print(f"Part 1 Matching pairs: {p1(NUM_PAIRS_P1)}")
    print(f"Part 2 Matching pairs with criteria: {p2(NUM_PAIRS_P2)}")