from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)  # For undirected graph

    def bfs_shortest_path(self, start, end):
        if start == end:
            return [start]

        visited = {start}
        queue = deque([(start, [])])

        while queue:
            node, path = queue.popleft()
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    if neighbor == end:
                        return path + [node, neighbor]
                    queue.append((neighbor, path + [node]))

        return None  # If no path is found

# Example usage:
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(3, 4)

start_node = 0
end_node = 4
shortest_path = g.bfs_shortest_path(start_node, end_node)

if shortest_path:
    print(f"Shortest path between {start_node} and {end_node}: {shortest_path}")
else:
    print(f"No path exists between {start_node} and {end_node}.")
