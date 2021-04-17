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


class Node:
    '''Node data structure for search space bookkeeping.'''

    def __init__(self, state, parent, action, path_cost):
        '''Constructor for the node state with the required parameters.'''
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost

    @classmethod
    def root(cls, init_state):
        '''Factory method to create the root node.'''
        return cls(init_state, None, None, 0)

    @classmethod
    def child(cls, state, parent, action):
        '''Factory method to create a child node.'''
        return cls(
            state,
            parent,
            action,
            parent.path_cost + 1)


# class Node:
#     '''Node data structure for search space bookkeeping.'''
#
#     def __init__(self, state, parent, action, path_cost, heuristic):
#         '''Constructor for the node state with the required parameters.'''
#         self.state = state
#         self.parent = parent
#         self.action = action
#         self.path_cost = path_cost
#         self.g = path_cost
#         self.h = heuristic
#         self.f = path_cost + heuristic
#
#     @classmethod
#     def root(cls, init_state):
#         '''Factory method to create the root node.'''
#         init_state = problem.init_state
#         return cls(init_state, None, None, 0, problem.heuristic(init_state))
#
#     @classmethod
#     def child(cls, problem, parent, action):
#         '''Factory method to create a child node.'''
#         child_state = problem.result(parent.state, action)
#         return cls(
#             problem.result(parent.state, action),
#             parent,
#             action,
#             parent.g + problem.step_cost(parent.state, action),
#             problem.heuristic(child_state))


def solution(node):
    '''A method to extract the sequence of actions representing the solution from the goal node.'''
    actions = []
    cost = node.path_cost
    while node.parent is not None:
        actions.append(node.action)
        node = node.parent
    actions.reverse()
    return actions, cost

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState())[0][0])
    if problem.isGoalState(problem.getStartState()) : return problem.getStartState()
    frontier = util.Stack()
    frontier.push(Node.root(problem.getStartState()))
    # node = Node.root(problem.getStartState())
    node =  frontier.pop()
    print(node.state)
    explored = { problem.getStartState() }
    '''Depth-first graph search implementation.'''
    if problem.isGoalState(problem.getStartState()): return problem.getStartState()
    frontier = util.Queue()
    frontier.push(Node.root(problem.getStartState()))
    explored = {problem.getStartState()}
    while frontier:
        node = frontier.pop()
        for sucessor in problem.getSuccessors(node.state):
            child = Node.child(sucessor[0], node, sucessor[1])
            if child.state not in explored:
                if problem.isGoalState(child.state):
                    print('hi')
                    return solution(child)[0]
                frontier.push(child)
                explored.add(child.state)



    "*** YOUR CODE HERE ***"


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    # if problem.goal_test(problem.init_state): return `solution(problem.init_state)
    # frontier = Queue.push([Node.root(problem.init_state)])
    # explored = {problem.init_state}
    # while frontier:
    #     node = frontier.pop()
    #     for action in problem.actions(node.state):
    #         child = Node.child(problem, node, action)
    #         if child.state not in explored:
    #             if problem.goal_test(child.state):
    #                 return solution(child)
    #             frontier.appendleft(child)
    #             explored.add(child.state)
    '''Breadth-first graph search implementation.'''
    if problem.isGoalState(problem.getStartState()): return problem.getStartState()
    frontier = util.Queue()
    frontier.push(Node.root(problem.getStartState()))
    explored = {problem.getStartState()}
    while frontier:
        node = frontier.pop()
        print(node.state)
        for sucessor in problem.getSuccessors(node.state):
            child = Node.child(sucessor[0], node, sucessor[1])
            if child.state not in explored:
                if problem.isGoalState(child.state):
                    print(solution(child)[0])
                    return solution(child)[0]
                frontier.push(child)
                explored.add(child.state)

from itertools import count
counter = count()
def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    '''ucs search implementation.'''
    if problem.isGoalState(problem.getStartState()): return problem.getStartState()
    frontier = util.PriorityQueue()
    frontier.push((None, None, Node.root(problem.getStartState())))
    # frontier = [(None, None, Node.root(problem))]
    explored = set()
    # if verbose: visualizer = Visualizer(problem)
    while frontier:
        #   if verbose: visualizer.visualize(frontier)
        _, _, node = frontier.pop()
        if node.state in explored: continue
        if problem.isGoalState(node.state):
            return solution(node)[0]
        explored.add(node.state)
        for sucessor in problem.getSuccessors(node.state):
            child = Node.child(sucessor[0], node, sucessor[1])
            # child = Node.child(problem, node, action)
            if child.state not in explored:
                frontier.push((1, next(counter), Node.root(problem.getStartState())))
                # heappush(frontier, (child.g, next(counter), child))

    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
