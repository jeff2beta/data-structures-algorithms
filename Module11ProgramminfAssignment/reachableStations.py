from collections import deque, defaultdict

def reachableStations(graph, n):
  # initialize empty set for reachable stations
  reachable_stations = [set() for _ in range(n)]

  # Iterate through all stations to perform BFS on each
  for i in range(n):
    # Initialise visited set with starting node
    visited = set([i])
    # Initialize queue with starting node and starting distance
    queue = deque([ (i, 0) ])

    # while queue is not empty
    while queue:
        # Pop the first node from the queue
        currentNode, distance = queue.popleft()
        # If distance is greater than 4 stop exploring 
        if distance > 4:
            continue

        # iterate through neighbors of current node
        for neighbor in graph[currentNode]:
            # check if node hasn't been visited
            if neighbor not in visited:
                # add neighbor to visited set
                visited.add(neighbor)
                # append neighbor and increment distance to the queue
                queue.append((neighbor, distance + 1))

    # Save visited set minus the starting node as a reachable station
    reachable_stations[i] = visited - {i}

  # return reachable stations within ≤ 4 links      
  return reachable_stations


# Helper function to build adjacency list
def build_graph(links):
    graph = {}

    for a, b in links:
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []

        graph[a].append(b)
        graph[b].append(a)

    return graph

# --------- Sample Test Cases ---------
test_cases = [
    {
        "name": "Case 1",
        "n": 8,
        "links": [(0, 1), (1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7), (4, 5), (5, 6), (6, 7)]
    },
    {
        "name": "Case 2",
        "n": 5,
        "links": [(0, 1), (1, 2), (2, 3), (3, 4)]
    }
]

# --------- Output to File ---------
with open("reachable_stations_output.txt", "w") as f:
    for case in test_cases:
        n = case["n"]
        links = case["links"]
        graph = build_graph(links)
        result = reachableStations(graph, n)

        f.write(f"{case['name']}:\n")
        for i, stations in enumerate(result):
            f.write(f"Reachable stations from station {i}: {stations}\n")
        f.write("\n")