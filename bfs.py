from collections import deque

class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_edge(self, from_node, to_node):
        if from_node not in self.adjacency_list:
            self.adjacency_list[from_node] = []
        if to_node not in self.adjacency_list:
            self.adjacency_list[to_node] = []
        self.adjacency_list[from_node].append(to_node)
        self.adjacency_list[to_node].append(from_node)

    def bfs(self, start, goal):
        queue = deque([(start, [start])])  # Queue for BFS
        visited = set()  # Set to track visited nodes

        while queue:
            current_node, path = queue.popleft()
            if current_node == goal:
                return path  # Path found

            if current_node not in visited:
                visited.add(current_node)
                for neighbor in self.adjacency_list.get(current_node, []):
                    if neighbor not in visited:
                        queue.append((neighbor, path + [neighbor]))

        return None  # No path found

if __name__ == "__main__":
    # Create a graph
    g = Graph()

    # Add edges
    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.add_edge("B", "D")
    g.add_edge("C", "D")
    g.add_edge("B", "E")
    g.add_edge("D", "E")
    g.add_edge("D", "F")
    g.add_edge("E", "F")

    # Perform BFS to find the shortest path
    start = "A"
    goal = "F"
    path = g.bfs(start, goal)

    # Print the result
    if path:
        print("Path found:", " -> ".join(path))
    else:
        print("No path found.")