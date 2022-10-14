from math import pow, sqrt
from queue import PriorityQueue

def shortest_path(map_graph: object, start: int, goal:int) -> list:
    """
    The function find the shortest path between start and goal in map_graph using A* method. Priority Queue is used to store and keep tracks of next path to test.
    :param map_graph: map with nodes and connection
    :param start: starting node
    :param end: destination node
    :return result: list of node 
    """
    print("shortest path called")
    
    # Define PriorityQueue and initialize it with starting node
    path_priorityqueue = PriorityQueue()
    path_priorityqueue.put(start, 0)
    
    # Initialize the record of explored and path cost
    path_history = {start: None}
    score = {start: 0}

    while not path_priorityqueue.empty():
        current = path_priorityqueue.get()
        if current == goal:
            # not adding new data but check other available path by skipping the for loop
            continue

        for node in map_graph.roads[current]:
            # Calculate path cost and update total score
            path_cost = score[current] + euclidean_distance(map_graph.intersections[current], map_graph.intersections[node])
            
            # Adding the node if the node has not visited or update with shortest path (only shortest path is kept)
            if node not in score or path_cost < score[node]:
                score[node] = path_cost
                # Calculate estimate cost(h)
                estimated_cost = euclidean_distance(map_graph.intersections[current], map_graph.intersections[node])
                
                # Get total cost
                total_cost = path_cost + estimated_cost
                
                # Add cost data input priorityqueue
                path_priorityqueue.put(node, total_cost)
                
                # 
                path_history[node] = current

    # recreate the path given the history of explored area
    result = generate_path(path_history, start, goal)
    
    return result

# Heuristic Function Choice
"""
Euclidean distance is used as it can measure movement to any direction not limited to specific direction like manhattan distance(4 directions) or diagonal distance(8 directions). When the movement is limited to 4 directions (Up, Down, Left, Right), manhattan distance should be used. When the movement is limited to 8 directions(Up, Down, Left, Right, left-up, left-down, right-up, right-down), diagonal distance should be used.  
"""

# Euclidean Distance
def euclidean_distance(start:int, goal:int) -> float:
    """
    Euclidean Distance is used
    :param start: starting node
    :param end: destination node
    :return: euclidean distance between two points 
    """
    return  sqrt(pow((start[0] - goal[0]), 2) + pow((start[1] - goal[1]), 2))

# Manhattan Distance
def manhattan_distance(start:int, goal:int) -> float:
    """
    Manhattan Distance is used
    :param start: starting node
    :param end: destination node
    :return: manhattan distance between two points 
    """
    x_distance = abs(start[0] - goal[0])
    y_distance = abs(start[1] - goal[1])
    
    return  x_distance + y_distance

# Diagonal Distance
def diagonal_distance(start:int, goal:int) -> float:
    """
    Diagonal Distance is used
    :param start: starting node
    :param end: destination node
    :return: diagonal distance between two points 
    """
    x_distance = abs(start[0] - goal[0])
    y_distance = abs(start[1] - goal[1])
    unit_distance = 1
    unit_diagonal_distance = sqrt(pow(unit_distance, 2) * 2)

    return  unit_distance * (x_distance + y_distance) + (unit_diagonal_distance - 2 * unit_distance) * min(x_distance, y_distance)

def generate_path(path_history: dict, start:int, goal:int) -> list:
    """
    Generate the path given history of shortest path visited
    :param start: starting node
    :param end: destination node
    :return path: list of node for shortest path 
    """
    # Initialize the node to visit as destination
    current = goal
    
    # adding the destination to path placeholder
    path = [current]
    
    # searching for the path backward
    while current != start:
        current = path_history[current]
        path.append(current)
        
    # reverse the list to start at the beginning node
    path.reverse()
    
    return path