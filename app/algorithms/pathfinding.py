import heapq
from collections import deque
from dataclasses import dataclass
from typing import List, Tuple, Set, Dict, Optional

@dataclass
class Node:
    position: Tuple[int, int]
    g_cost: float = 0
    h_cost: float = 0
    parent: Optional['Node'] = None
    
    @property
    def f_cost(self) -> float:
        return self.g_cost + self.h_cost
    
    def __lt__(self, other):
        return self.f_cost < other.f_cost

def get_neighbors(grid: List[List[int]], node: Node) -> List[Tuple[int, int]]:
    rows, cols = len(grid), len(grid[0])
    row, col = node.position
    neighbors = []
    
    for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        new_row, new_col = row + dr, col + dc
        if (0 <= new_row < rows and 0 <= new_col < cols and 
            grid[new_row][new_col] != 3):  # 3 represents a wall
            neighbors.append((new_row, new_col))
    
    return neighbors

def manhattan_distance(pos1: Tuple[int, int], pos2: Tuple[int, int]) -> float:
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

def reconstruct_path(node: Node) -> List[Tuple[int, int]]:
    path = []
    current = node
    while current:
        path.append(current.position)
        current = current.parent
    return path[::-1]

def dijkstra(grid: List[List[int]], start: Dict[str, int], end: Dict[str, int]) -> Tuple[List[Tuple[int, int]], List[Dict]]:
    rows, cols = len(grid), len(grid[0])
    start_pos = (start['row'], start['col'])
    end_pos = (end['row'], end['col'])
    
    distances = {start_pos: 0}
    visited = set()
    pq = [(0, start_pos, None)]
    steps = []
    
    while pq:
        dist, current_pos, parent = heapq.heappop(pq)
        
        if current_pos in visited:
            continue
            
        visited.add(current_pos)
        steps.append({'type': 'visit', 'position': current_pos})
        
        if current_pos == end_pos:
            path = reconstruct_path(Node(current_pos, dist, 0, parent))
            return path, steps
        
        for neighbor in get_neighbors(grid, Node(current_pos)):
            if neighbor not in visited:
                new_dist = dist + 1
                if neighbor not in distances or new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    heapq.heappush(pq, (new_dist, neighbor, Node(current_pos, dist, 0, parent)))
    
    return [], steps

def astar(grid: List[List[int]], start: Dict[str, int], end: Dict[str, int]) -> Tuple[List[Tuple[int, int]], List[Dict]]:
    start_pos = (start['row'], start['col'])
    end_pos = (end['row'], end['col'])
    
    open_set = []
    closed_set = set()
    start_node = Node(start_pos, 0, manhattan_distance(start_pos, end_pos))
    heapq.heappush(open_set, start_node)
    steps = []
    
    while open_set:
        current = heapq.heappop(open_set)
        
        if current.position == end_pos:
            path = reconstruct_path(current)
            return path, steps
            
        closed_set.add(current.position)
        steps.append({'type': 'visit', 'position': current.position})
        
        for neighbor_pos in get_neighbors(grid, current):
            if neighbor_pos in closed_set:
                continue
                
            g_cost = current.g_cost + 1
            h_cost = manhattan_distance(neighbor_pos, end_pos)
            neighbor = Node(neighbor_pos, g_cost, h_cost, current)
            
            if not any(node.position == neighbor_pos and node.g_cost <= g_cost 
                      for node in open_set):
                heapq.heappush(open_set, neighbor)
    
    return [], steps

def bfs(grid: List[List[int]], start: Dict[str, int], end: Dict[str, int]) -> Tuple[List[Tuple[int, int]], List[Dict]]:
    start_pos = (start['row'], start['col'])
    end_pos = (end['row'], end['col'])
    
    queue = deque([(start_pos, None)])
    visited = {start_pos: None}
    steps = []
    
    while queue:
        current_pos, parent = queue.popleft()
        steps.append({'type': 'visit', 'position': current_pos})
        
        if current_pos == end_pos:
            path = []
            while current_pos:
                path.append(current_pos)
                current_pos = visited[current_pos]
            return path[::-1], steps
        
        for neighbor in get_neighbors(grid, Node(current_pos)):
            if neighbor not in visited:
                visited[neighbor] = current_pos
                queue.append((neighbor, current_pos))
    
    return [], steps

def dfs(grid: List[List[int]], start: Dict[str, int], end: Dict[str, int]) -> Tuple[List[Tuple[int, int]], List[Dict]]:
    start_pos = (start['row'], start['col'])
    end_pos = (end['row'], end['col'])
    
    stack = [(start_pos, None)]
    visited = {start_pos: None}
    steps = []
    
    while stack:
        current_pos, parent = stack.pop()
        steps.append({'type': 'visit', 'position': current_pos})
        
        if current_pos == end_pos:
            path = []
            while current_pos:
                path.append(current_pos)
                current_pos = visited[current_pos]
            return path[::-1], steps
        
        for neighbor in get_neighbors(grid, Node(current_pos)):
            if neighbor not in visited:
                visited[neighbor] = current_pos
                stack.append((neighbor, current_pos))
    
    return [], steps 