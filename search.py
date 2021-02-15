# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
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
                
            
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
