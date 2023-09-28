# https://adventofcode.com/2017/day/7
import sys
import copy
import re

# finds parent of node
def find_parent(lookup):
    for name,info in tree.items():
        children = info[1]
        if lookup in children:
            return find_parent(name)
    return lookup

# calculate the weight of all subtrees for a root node
def calculate_subtrees(root):
    children = tree[root][1]
    subtree_weights = tree[root][2]
    if len(children) == 0:
        return tree[root][0]
    for child in children:
        weight = calculate_subtrees(child)
        subtree_weights.append(weight)
    tree[root][0] = sum(subtree_weights) + tree[root][0]
    return tree[root][0]

def p1():
    ans = ""
    for name,info in tree.items():
        children = info[1]
        if len(children) == 0:
            ans = find_parent(name)
            break
    return ans

# use root and find weights of subtrees recursive, find lowest subtree that is invalid
def p2(root):
    calculate_subtrees(root)
    ans = ["",1000000,0]
    for name,info in tree.items():
        subtree_weights = info[2]
        if len(subtree_weights) == 0:
            continue

        for idx,subweight in enumerate(subtree_weights):
            if subweight != subtree_weights[0]:
                if subweight < ans[1]:
                    ans = [tree[name][1][idx-1],subweight,abs(subweight-subtree_weights[0])]
                    break
    return ans

if __name__ == "__main__":
    data = open(sys.argv[1]).read().splitlines()
    tree = {}
    for line in data:
        info = line.split("->")
        arr = info[0].split()
        name = arr[0]
        weight = int("".join(re.findall("\d+", arr[1])))
        children = []
        if len(info) == 2:
            children = info[1].strip().split(", ")
        tree[name] = [weight,children,[]]
    root = p1()
    print(f"Part 1 Root of the Tree is {root}")
    original_tree = copy.deepcopy(tree)
    ans_p2 = p2(root)
    print(f"Part 2 {ans_p2[0]}'s weight should be {original_tree[ans_p2[0]][0]-ans_p2[2]} instead of {original_tree[ans_p2[0]][0]}")