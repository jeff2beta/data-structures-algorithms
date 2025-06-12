from flask import Blueprint, render_template, jsonify, request
from .algorithms.pathfinding import dijkstra, astar, bfs, dfs

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/api/run-algorithm', methods=['POST'])
def run_algorithm():
    data = request.get_json()
    
    if not data:
        return jsonify({'status': 'error', 'message': 'No data provided'}), 400
    
    required_fields = ['algorithm', 'grid', 'start', 'end']
    for field in required_fields:
        if field not in data:
            return jsonify({'status': 'error', 'message': f'Missing required field: {field}'}), 400
    
    algorithm = data['algorithm']
    grid = data['grid']
    start = data['start']
    end = data['end']
    
    algorithm_map = {
        'dijkstra': dijkstra,
        'astar': astar,
        'bfs': bfs,
        'dfs': dfs
    }
    
    if algorithm not in algorithm_map:
        return jsonify({'status': 'error', 'message': 'Invalid algorithm selected'}), 400
    
    try:
        path, steps = algorithm_map[algorithm](grid, start, end)
        return jsonify({
            'status': 'success',
            'path': path,
            'steps': steps
        })
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500 