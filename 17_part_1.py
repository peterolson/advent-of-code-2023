with open("input/17.txt", "r") as f:
    lines = [[int(c) for c in line.strip()] for line in f.readlines()]

map_size = len(lines) * len(lines[0])

start = (0,0)
end = (len(lines)-1, len(lines[0])-1)

directions = [(1,0), (0,1), (-1,0), (0,-1)]

max_straight = 3

min_costs = {
    end: 0
}

queue = [(end, 0)]
visited = set()

while len(queue) > 0:
    node_with_smallest_cost = min(queue, key=lambda x: x[1])
    queue.remove(node_with_smallest_cost)
    current, total_cost = node_with_smallest_cost
    if current in visited:
        continue

    for direction in directions:
        next = (current[0] + direction[0], current[1] + direction[1])
        if next[0] < 0 or next[1] < 0 or next[0] > end[0] or next[1] > end[1] or next in visited:
            continue
        cost = total_cost + lines[next[0]][next[1]]
        if next in min_costs and min_costs[next] <= cost:
            continue
        min_costs[next] = cost
        queue.append((next, cost))
    visited.add(current)
    
print("Heuristic finished")
    
def heuristic(current):
    point, direction = current
    return min_costs[point]

open_set = [(start, (1,0)), (start, (0,1))]
g_score = {
    open_set[0]: 0,
    open_set[1]: 0
}
f_score = {
    open_set[0]: heuristic(open_set[0]),
    open_set[1]: heuristic(open_set[1])
}
open_set = set(open_set)
came_from = {}

iterations = 0

while len(open_set) > 0:
    iterations += 1
    if iterations % 5000 == 0:
        print(f"Map size: {map_size}\t\tIterations: {iterations}\t\tOpen set size: {len(open_set)}\t\tg_score size: {len(g_score)}")
    current = min(open_set, key=lambda x: f_score[x])
    open_set.remove(current)
    
    point, direction = current
    for new_direction in directions:
        if new_direction == direction:
            continue
        if new_direction == (-direction[0], -direction[1]):
            continue
        distance = 0
        for i in range(1, max_straight+1):
            new_point = (point[0] + new_direction[0] * i, point[1] + new_direction[1] * i)
            if new_point[0] < 0 or new_point[1] < 0 or new_point[0] > end[0] or new_point[1] > end[1]:
                continue
            neighbor = (new_point, new_direction)
            distance += lines[new_point[0]][new_point[1]]
            tentative_g_score = g_score[current] + distance
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor)
                if neighbor not in open_set:
                    open_set.add(neighbor)
                
def reconstruct_path(current):
    total_path = [current]
    while current in came_from:
        current = came_from[current]
        total_path.append(current)
    return list(reversed(total_path))
        
end_nodes = {node for node in f_score if node[0] == end}
min_g_score = min(g_score[node] for node in end_nodes)
min_f_score = min(f_score[node] for node in end_nodes)

print(min_g_score)
print(min_f_score)

# best_node = min(end_nodes, key=lambda x: g_score[x])
# print(reconstruct_path(best_node))