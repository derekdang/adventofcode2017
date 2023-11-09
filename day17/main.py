# https://adventofcode.com/2017/day/17

def find_new_pos(num_steps: int, index: int, buffer: list[int]) -> int:
    if index + num_steps >= len(buffer):
        index = (index + num_steps) % len(buffer)
    else:
        index += num_steps
    return index

def find_pos2(num_steps: int, index: int, buffer: int) -> int:
    if index + num_steps >= buffer:
        index = (index + num_steps) % buffer
    else:
        index += num_steps
    return index

def p1(num_steps: int) -> int:
    BUFFER_LIMIT = 2018
    buffer = [0]
    index = 0
    for i in range(1, BUFFER_LIMIT):
        index = find_new_pos(num_steps, index, buffer)
        buffer.insert(index + 1, i)
        index = index + 1
    return buffer[index + 1]

def p2(num_steps: int) -> int:
    BUFFER_LIMIT = 50_000_001
    buffer = 1
    last_insertion_after_zero = 0
    index = 0
    for i in range(1, BUFFER_LIMIT):
        index = find_pos2(num_steps, index, buffer)
        if index + i % buffer == 0:
            last_insertion_after_zero = i
        index = index + 1
        buffer += 1
    return last_insertion_after_zero

if __name__ == "__main__":
    input = 329
    print(f"Part 1 Num in buffer after 2017: {p1(input)}")
    # 20 seconds for part 2
    print(f"Part 2 Num after index 0 after 50 million insertions: {p2(input)}")