def depthFirstSearch(problem):
    initial_node = (problem.getStartState(), [])
    frontier = [initial_node]
    explored = []
    while True:
        if len(frontier) == 0:
            return False
        curr_node = frontier[-1]
        frontier.pop(-1)
        explored.append(curr_node[0])
        if problem.isGoalState(curr_node[0]):
            return curr_node[1]
        for pair in problem.getSuccessors(curr_node[0]):
            if pair[0] not in explored:
                state_in_frontier = []
                for node in frontier:
                    state_in_frontier.append(node[0])
                if pair[0] in state_in_frontier:
                    index = state_in_frontier.index(pair[0])
                    frontier.pop(index)
                frontier.append((pair[0], curr_node[1] + [pair[1]]))
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    initial_node = (problem.getStartState(), []) # Initial state node
    frontier = [initial_node] # Iitialize frontier
    explored = [] # Initialize explored set
    # Loop
    while True:
        if len(frontier) == 0:
            return False
        #Take first node from frontier and append it into explored set
        curr_node = frontier[0]
        frontier.pop(0)
        explored.append(curr_node[0])
        # Check if the goal has achieved
        if problem.isGoalState(curr_node[0]):
            return curr_node[1]
        # For loop
        for pair in problem.getSuccessors(curr_node[0]):
            # Create a list to store all the state in the nodes of frontier to make the check easier
            state_in_frontier = []
            for node in frontier:
                state_in_frontier.append(node[0])
            # Check the state and add next state
            if pair[0] not in explored and pair[0] not in state_in_frontier:
                frontier.append((pair[0], curr_node[1] + [pair[1]]))

    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    initial_node = (problem.getStartState(), [], 0)
    frontier = [initial_node]
    explored = []
    
    while True:
        if len(frontier) == 0:
            return False
        lowest_cost = uniformCostSearchHelper(frontier)
        curr_node = frontier[lowest_cost]
        frontier.pop(lowest_cost)
        explored.append(curr_node[0])
        if problem.isGoalState(curr_node[0]):
            return curr_node[1]

        for pair in problem.getSuccessors(curr_node[0]):
            next_cost = curr_node[2] + pair[2]
            next_node = (pair[0], curr_node[1] + [pair[1]], next_cost)
            if pair[0] not in explored:
                state_in_frontier = []
                for node in frontier:
                    state_in_frontier.append(node[0])
                if pair[0] not in state_in_frontier:
                    frontier.append(next_node)
                else:
                    index = state_in_frontier.index(pair[0])
                    if frontier[index][2] >= next_cost:
                        frontier[index] = next_node

    util.raiseNotDefined()

""" Help function: return the index of lowest cost node in frontier """
def uniformCostSearchHelper(frontier):
    costs = []
    for t in frontier:
        costs.append(t[2])
    return costs.index(min(costs))

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    initial_node = (problem.getStartState(), [], 0)
    frontier = util.PriorityQueue()
    frontier.push((initial_node, heuristic(problem.getStartState(), problem)), 0)
    explored = []

    while True:
        if frontier.isEmpty():
            return False
        curr_node = frontier.pop()[0]
        if problem.isGoalState(curr_node[0]):
            return curr_node[1]
        
        if curr_node[0] not in explored:
            explored.append(curr_node[0])
            for pair in problem.getSuccessors(curr_node[0]):
                next_cost = curr_node[2] + pair[2]
                next_node = (pair[0], curr_node[1] + [pair[1]], next_cost)
                next_priority = next_cost + heuristic(pair[0], problem)
                frontier.update((next_node, heuristic(pair[0], problem)), next_priority)
