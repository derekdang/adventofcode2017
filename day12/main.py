# https://adventofcode.com/2017/day/12
import sys

def build_graph(input: list[str]) -> dict:
    graph = {}
    for line in input:
        arr = line.split("<->")
        node1 = int(arr[0].strip())
        connected_nodes = [int(node2) for node2 in arr[1].split(',')]
        graph[node1] = set(connected_nodes)
        for connected_node in connected_nodes:
            if connected_node not in graph:
                graph[connected_node] = set()
            graph[connected_node].add(connected_node)
    return graph

def p1(graph: dict) -> int:
    stack = []
    visited = set()
    stack.append(0)
    nodes_connected_to_zero = 0
    while stack:
        curr_node = stack.pop()
        visited.add(curr_node)
        nodes_connected_to_zero += 1
        for adj_node in graph[curr_node]:
            if adj_node in visited or adj_node in stack:
                continue
            stack.append(adj_node)
    return nodes_connected_to_zero

def p2(graph: dict) -> int:
    num_groups = 0
    visited = set()
    while len(visited) != len(graph):
        for node,_ in graph.items():
            if node not in visited:
                num_groups += 1
                stack = []
                stack.append(node)
                while stack:
                    curr_node = stack.pop()
                    visited.add(curr_node)
                    for adj_node in graph[curr_node]:
                        if adj_node in visited or adj_node in stack:
                            continue
                        stack.append(adj_node)
    return num_groups

if __name__ == "__main__":
    raw = open(sys.argv[1]).read().splitlines()
    graph = build_graph(raw)
    print(f"Part 1 Number of Programs Connected to Program 0: {p1(graph)}")
    print(f"Part 2 Number of Graphs/Groups: {p2(graph)}")