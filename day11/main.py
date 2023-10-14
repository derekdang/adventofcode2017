# https://adventofcode.com/2017/day/11
import sys

def p1p2():
    x,y,z = 0,0,0
    p2 = 0
    for step in data:
        if step == "n":
            y -= 1
            z += 1
        elif step == "ne":
            x += 1
            y -= 1
        elif step == "nw":
            x -= 1
            z += 1
        elif step == "s":
            y += 1
            z -= 1
        elif step == "se":
            x += 1
            z -= 1
        elif step == "sw":
            x -= 1
            y += 1
        p2 = max(p2,(abs(x) + abs(y) + abs(z))//2)
    return (abs(x) + abs(y) + abs(z))//2,p2

if __name__ == "__main__":
    data = open(sys.argv[1]).read().split(',')
    p1,p2 = p1p2()
    print(f"Part 1 Min Number of Steps: {p1}")
    print(f"Part 2 Furthest Distance Away: {p2}")