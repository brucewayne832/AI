def dfs(graph, start, visited=None):
   
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=' ')
    for neighbor in graph.get(start, []):  
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    return visited

def create_graph():
    
    graph = {}
    num_nodes = int(input("Enter the number of nodes: "))
    for i in range(num_nodes):
        node = input(f"Enter node {i + 1}: ").strip()
        neighbors = input(f"Enter neighbors of {node} (comma separated): ").split(',')
        graph[node] = [neighbor.strip() for neighbor in neighbors if neighbor.strip()]
    return graph

def main():
    
    graph = create_graph()
    print("\nGraph representation:")
    for node, neighbors in graph.items():
        print(f"{node}: {', '.join(neighbors)}")

    start_node = input("\nEnter the start node for DFS: ").strip()
    if start_node not in graph:
        print("Error: Start node not found in the graph.")
        return

    print("\nDFS Traversal:")
    dfs(graph, start_node)

if __name__ == "__main__":
    main()
