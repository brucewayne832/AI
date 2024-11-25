import heapq

class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_edge(self, from_node, to_node, cost):
        if from_node not in self.adjacency_list:
            self.adjacency_list[from_node] = []
        if to_node not in self.adjacency_list:
            self.adjacency_list[to_node] = []
        self.adjacency_list[from_node].append((to_node, cost))
        self.adjacency_list[to_node].append((from_node, cost))

    def best_first_search(self, start, goal, heuristic):
        open_set = []
        closed_set = set()

        heapq.heappush(open_set, (heuristic[start], start))
        came_from = {}
        came_from[start] = None

        while open_set:
            _, current = heapq.heappop(open_set)

            if current == goal:
                path = []
                while current:
                    path.append(current)
                    current = came_from[current]  
                return path[::-1]

            closed_set.add(current)

            for neighbor, cost in self.adjacency_list[current]:
                if neighbor not in closed_set:
                    heapq.heappush(open_set, (heuristic[neighbor], neighbor))
                    if neighbor not in came_from:
                        came_from[neighbor] = current

        return None

if __name__ == "__main__":
    # Create a graph
    g = Graph()

    g.add_edge("A", "B", 1)
    g.add_edge("A", "C", 4)
    g.add_edge("B", "D", 2)
    g.add_edge("C", "D", 5)
    g.add_edge("B", "E", 3)
    g.add_edge("D", "E", 1)
    g.add_edge("D", "F", 2)
    g.add_edge("E", "F", 4)

    heuristic = {
        "A": 7,
        "B": 6,
        "C": 2,
        "D": 1,
        "E": 4,
        "F": 0  # Goal node
    }

    start = "A"
    goal = "F"
    path = g.best_first_search(start, goal, heuristic)

    if path:
        print("Path found:", " -> ".join(path))
    else:
        print("No path found.")