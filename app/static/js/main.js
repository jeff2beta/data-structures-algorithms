class Grid {
    constructor(canvas, rows = 20, cols = 20) {
        this.canvas = canvas;
        this.ctx = canvas.getContext('2d');
        this.rows = rows;
        this.cols = cols;
        this.cellSize = 30;
        this.grid = Array(rows).fill().map(() => Array(cols).fill(0));
        this.start = null;
        this.end = null;
        this.path = [];
        this.isVisualizing = false;
        this.visited = new Set();
        this.currentStep = 0;
        this.steps = [];
        
        // Set canvas size
        this.canvas.width = cols * this.cellSize;
        this.canvas.height = rows * this.cellSize;
        
        // Initialize event listeners
        this.initializeEventListeners();
        
        // Draw initial grid
        this.draw();
    }
    
    initializeEventListeners() {
        this.canvas.addEventListener('click', (e) => {
            if (this.isVisualizing) return;
            
            const rect = this.canvas.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            
            const col = Math.floor(x / this.cellSize);
            const row = Math.floor(y / this.cellSize);
            
            if (!this.start) {
                this.start = { row, col };
                this.grid[row][col] = 1;
            } else if (!this.end) {
                this.end = { row, col };
                this.grid[row][col] = 2;
            } else {
                this.grid[row][col] = this.grid[row][col] === 3 ? 0 : 3;
            }
            
            this.draw();
        });
    }
    
    draw() {
        this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
        
        // Draw grid lines
        this.ctx.strokeStyle = '#ddd';
        for (let i = 0; i <= this.rows; i++) {
            this.ctx.beginPath();
            this.ctx.moveTo(0, i * this.cellSize);
            this.ctx.lineTo(this.canvas.width, i * this.cellSize);
            this.ctx.stroke();
        }
        
        for (let i = 0; i <= this.cols; i++) {
            this.ctx.beginPath();
            this.ctx.moveTo(i * this.cellSize, 0);
            this.ctx.lineTo(i * this.cellSize, this.canvas.height);
            this.ctx.stroke();
        }
        
        // Draw visited cells
        this.visited.forEach(pos => {
            this.ctx.fillStyle = 'rgba(33, 150, 243, 0.3)';
            this.ctx.fillRect(
                pos[1] * this.cellSize + 1,
                pos[0] * this.cellSize + 1,
                this.cellSize - 2,
                this.cellSize - 2
            );
        });
        
        // Draw path
        if (this.path.length > 0) {
            this.ctx.strokeStyle = '#2196F3';
            this.ctx.lineWidth = 2;
            this.ctx.beginPath();
            
            const start = this.path[0];
            this.ctx.moveTo(
                (start[1] + 0.5) * this.cellSize,
                (start[0] + 0.5) * this.cellSize
            );
            
            for (let i = 1; i < this.path.length; i++) {
                const pos = this.path[i];
                this.ctx.lineTo(
                    (pos[1] + 0.5) * this.cellSize,
                    (pos[0] + 0.5) * this.cellSize
                );
            }
            
            this.ctx.stroke();
        }
        
        // Draw cells
        for (let row = 0; row < this.rows; row++) {
            for (let col = 0; col < this.cols; col++) {
                const cell = this.grid[row][col];
                if (cell === 1) { // Start
                    this.ctx.fillStyle = '#4CAF50';
                } else if (cell === 2) { // End
                    this.ctx.fillStyle = '#f44336';
                } else if (cell === 3) { // Wall
                    this.ctx.fillStyle = '#333';
                } else {
                    continue;
                }
                
                this.ctx.fillRect(
                    col * this.cellSize + 1,
                    row * this.cellSize + 1,
                    this.cellSize - 2,
                    this.cellSize - 2
                );
            }
        }
    }
    
    clear() {
        this.grid = Array(this.rows).fill().map(() => Array(this.cols).fill(0));
        this.start = null;
        this.end = null;
        this.path = [];
        this.visited.clear();
        this.isVisualizing = false;
        this.currentStep = 0;
        this.steps = [];
        this.draw();
    }
    
    async visualizePath(path, steps) {
        this.isVisualizing = true;
        this.path = path;
        this.steps = steps;
        this.currentStep = 0;
        this.visited.clear();
        this.draw();
        this.updateStepInfo();
        this.isVisualizing = false;
    }
    
    step() {
        if (this.currentStep < this.steps.length) {
            const step = this.steps[this.currentStep];
            if (step.type === 'visit') {
                this.visited.add(step.position);
            }
            this.currentStep++;
            this.draw();
            this.updateStepInfo();
            return true;
        }
        return false;
    }
    
    updateStepInfo() {
        const stepInfo = document.getElementById('step-info');
        stepInfo.textContent = `Step: ${this.currentStep} / ${this.steps.length}`;
    }
}

// Algorithm code templates
const algorithmCode = {
    dijkstra: `def dijkstra(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    start_pos = (start['row'], start['col'])
    end_pos = (end['row'], end['col'])
    
    distances = {start_pos: 0}
    visited = set()
    pq = [(0, start_pos, None)]
    
    while pq:
        dist, current_pos, parent = heapq.heappop(pq)
        
        if current_pos in visited:
            continue
            
        visited.add(current_pos)
        
        if current_pos == end_pos:
            return reconstruct_path(Node(current_pos, dist, 0, parent))
        
        for neighbor in get_neighbors(grid, Node(current_pos)):
            if neighbor not in visited:
                new_dist = dist + 1
                if neighbor not in distances or new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    heapq.heappush(pq, (new_dist, neighbor, Node(current_pos, dist, 0, parent)))
    
    return []`,
    
    astar: `def astar(grid, start, end):
    start_pos = (start['row'], start['col'])
    end_pos = (end['row'], end['col'])
    
    open_set = []
    closed_set = set()
    start_node = Node(start_pos, 0, manhattan_distance(start_pos, end_pos))
    heapq.heappush(open_set, start_node)
    
    while open_set:
        current = heapq.heappop(open_set)
        
        if current.position == end_pos:
            return reconstruct_path(current)
            
        closed_set.add(current.position)
        
        for neighbor_pos in get_neighbors(grid, current):
            if neighbor_pos in closed_set:
                continue
                
            g_cost = current.g_cost + 1
            h_cost = manhattan_distance(neighbor_pos, end_pos)
            neighbor = Node(neighbor_pos, g_cost, h_cost, current)
            
            if not any(node.position == neighbor_pos and node.g_cost <= g_cost 
                      for node in open_set):
                heapq.heappush(open_set, neighbor)
    
    return []`,
    
    bfs: `def bfs(grid, start, end):
    start_pos = (start['row'], start['col'])
    end_pos = (end['row'], end['col'])
    
    queue = deque([(start_pos, None)])
    visited = {start_pos: None}
    
    while queue:
        current_pos, parent = queue.popleft()
        
        if current_pos == end_pos:
            path = []
            while current_pos:
                path.append(current_pos)
                current_pos = visited[current_pos]
            return path[::-1]
        
        for neighbor in get_neighbors(grid, Node(current_pos)):
            if neighbor not in visited:
                visited[neighbor] = current_pos
                queue.append((neighbor, current_pos))
    
    return []`,
    
    dfs: `def dfs(grid, start, end):
    start_pos = (start['row'], start['col'])
    end_pos = (end['row'], end['col'])
    
    stack = [(start_pos, None)]
    visited = {start_pos: None}
    
    while stack:
        current_pos, parent = stack.pop()
        
        if current_pos == end_pos:
            path = []
            while current_pos:
                path.append(current_pos)
                current_pos = visited[current_pos]
            return path[::-1]
        
        for neighbor in get_neighbors(grid, Node(current_pos)):
            if neighbor not in visited:
                visited[neighbor] = current_pos
                stack.append((neighbor, current_pos))
    
    return []`
};

// Initialize the application
document.addEventListener('DOMContentLoaded', () => {
    const canvas = document.getElementById('grid');
    const grid = new Grid(canvas);
    
    // Initialize controls
    const startButton = document.getElementById('start');
    const stepButton = document.getElementById('step');
    const clearButton = document.getElementById('clear');
    const algorithmSelect = document.getElementById('algorithm');
    const codeElement = document.getElementById('algorithm-code');
    
    // Set initial code
    codeElement.textContent = algorithmCode.dijkstra;
    hljs.highlightElement(codeElement);
    
    // Update code when algorithm changes
    algorithmSelect.addEventListener('change', () => {
        codeElement.textContent = algorithmCode[algorithmSelect.value];
        hljs.highlightElement(codeElement);
    });
    
    startButton.addEventListener('click', async () => {
        if (!grid.start || !grid.end) {
            alert('Please set both start and end points');
            return;
        }
        
        const algorithm = algorithmSelect.value;
        try {
            const response = await fetch('/api/run-algorithm', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    algorithm,
                    grid: grid.grid,
                    start: grid.start,
                    end: grid.end
                })
            });
            
            const data = await response.json();
            if (data.status === 'success') {
                await grid.visualizePath(data.path, data.steps);
                stepButton.disabled = false;
            } else {
                alert(data.message || 'An error occurred');
            }
        } catch (error) {
            console.error('Error:', error);
            alert('An error occurred while running the algorithm');
        }
    });
    
    stepButton.addEventListener('click', () => {
        if (!grid.step()) {
            stepButton.disabled = true;
        }
    });
    
    clearButton.addEventListener('click', () => {
        grid.clear();
        stepButton.disabled = true;
    });
}); 