# https://adventofcode.com/2017/day/3
import math
from tqdm import tqdm
spiral_order = ['R', 'U', 'L', 'D']
spiral_dir = {'R':(1,0), 'U': (0,1), 'L': (-1,0), 'D': (0,-1)}

def p1():
    plot_points = {1: [0,0], 2: [1,0], 3: [1,1], 4: [0,1]}
    target_square_size = math.ceil(math.sqrt(square_no))
    num = 5
    spiral_ind = 2
    last_point = plot_points[4]
    for i in range(3, target_square_size + 1):
        move = spiral_dir[spiral_order[spiral_ind]]
        plot_points[num] = [move[0] + last_point[0], move[1] + last_point[1]]
        last_point = plot_points[num]

        num += 1
        spiral_ind += 1
        spiral_ind = 0 if spiral_ind % 4 == 0 else spiral_ind
        move = spiral_dir[spiral_order[spiral_ind]]

        for j in range(i-1):
            plot_points[num] = [move[0] + last_point[0], move[1] + last_point[1]]
            last_point = plot_points[num]
            num += 1
        
        spiral_ind += 1
        spiral_ind = 0 if spiral_ind % 4 == 0 else spiral_ind
        move = spiral_dir[spiral_order[spiral_ind]]

        for j in range(i-1):
            plot_points[num] = [move[0] + last_point[0], move[1] + last_point[1]]
            last_point = plot_points[num]
            num += 1

    return abs(plot_points[square_no][0]) + abs(plot_points[square_no][1])

def p2():
    neighbors = [[0,1], [0,-1], [1,0], [-1,0], [1,1], [1,-1], [-1,1], [-1,-1]]
    plot_points = {(0,0): 1, (1,0): 1, (1,1): 2, (0,1):  4}
    target_square_size = math.ceil(math.sqrt(square_no))
    spiral_ind = 2
    last_point = (0,1)
    for i in range(3, target_square_size + 1):
        move = spiral_dir[spiral_order[spiral_ind]]
        new_move = (move[0] + last_point[0], move[1] + last_point[1])
        value = 0
        for n in neighbors:
            neighbor = (new_move[0] + n[0], new_move[1] + n[1])
            if neighbor in plot_points:
                value += plot_points[neighbor]
        if value > square_no:
            return value
        plot_points[new_move] = value
        last_point = new_move

        spiral_ind += 1
        spiral_ind = 0 if spiral_ind % 4 == 0 else spiral_ind
        move = spiral_dir[spiral_order[spiral_ind]]

        for j in range(i-1):
            new_move = (move[0] + last_point[0], move[1] + last_point[1])
            value = 0
            for n in neighbors:
                neighbor = (new_move[0] + n[0], new_move[1] + n[1])
                if neighbor in plot_points:
                    value += plot_points[neighbor]
            if value > square_no:
                return value
            plot_points[new_move] = value
            last_point = new_move
            
        spiral_ind += 1
        spiral_ind = 0 if spiral_ind % 4 == 0 else spiral_ind
        move = spiral_dir[spiral_order[spiral_ind]]

        for j in range(i-1):
            new_move = (move[0] + last_point[0], move[1] + last_point[1])
            value = 0
            for n in neighbors:
                neighbor = (new_move[0] + n[0], new_move[1] + n[1])
                if neighbor in plot_points:
                    value += plot_points[neighbor]
            if value > square_no:
                return value
            plot_points[new_move] = value
            last_point = new_move
    
if __name__ == "__main__":
    square_no = 289326
    print(f"Part 1 Manhattan distance from origin for our square number: {p1()}")
    print(f"Part 2 First value for a cell that is greater than our input: {p2()}")