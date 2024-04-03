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

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    fringe = util.Stack()
    graph = GraphSearch(problem, fringe)
    completedPath = graph.search()
    print("completedPath:",completedPath)
    print("CompletedPathLen:",len(completedPath))
    return completedPath
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    fringe = util.Queue()
    graph = GraphSearch(problem, fringe)
    completedPath = graph.search()
    print("completedPath:",completedPath)
    print("CompletedPathLen:",len(completedPath))
    return completedPath
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    fringe = util.PriorityQueue()
    graph = GraphSearch(problem, fringe)
    completedPath = graph.search()
    print("completedPath:",completedPath)
    print("CompletedPathLen:",len(completedPath))
    return completedPath
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
    fringe = util.PriorityQueue()
    graph = GreedyBFS(problem, fringe, heuristic)
    completedPath = graph.search()
    return completedPath
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch

# Node
class Node:
    def __init__(self, state, parent,direction, pathcost, totalPathcost):
        self.state = state # Store the coordinate of the path
        self.parent = parent
        self.direction = direction
        self.pathcost = pathcost # Store the pathcost to the previous node
        self.totalPathcost = totalPathcost # Store the total pathcost from the starting node
    def __str__(self):
        # For debug
        return str(self.state) + " " + str(self.parent) + " " + str(self.direction) + " " + str(self.pathcost) + " " + str(self.totalPathcost)

# GraphSearch
class GraphSearch:
    def __init__(self, problem, fringe, heuristic=None):
        self.problem = problem
        self.fringe = fringe
        self.explored = set() #Check whether the node has been explored
        self.orderOfExp = [] #Check the order of exploration
        self.heuristic = heuristic
        self.expanded = set() #Check if a node has expanded
        self.path = [] #Store the final path

    def _addToFringe(self, node):
        #Add node to the fringe. Be careful with the type of fringe, you should check it for a suitable addition.
        if(type(self.fringe) == util.Stack or type(self.fringe) == util.Queue):
            self.fringe.push(node)
        if(type(self.fringe) == util.PriorityQueue):
            self.fringe.update(node, node.totalPathcost)
        return
        util.raiseNotDefined()
    
    def search(self): 
        #Implement main graph search algorithm
        startNode = Node(self.problem.getStartState(), None,None, 0,0)
        print("start:",startNode.state)
        self._addToFringe(startNode)

        counter = 5000 # In case of infinity loop
        while(not self.fringe.isEmpty() and counter > 0):
            node = self.fringe.pop()
            self.orderOfExp.append(node)
            self.explored.add(node.state)
            checkGoal = self.problem.isGoalState(node.state)
            # If the node is the last goal
            if(checkGoal and checkGoal != '0'): 
                self.path += self.___extractPath(node)
                return self.path
            # If the node is one of the goals
            elif(checkGoal=='0'):
                # Save the path 
                self.path += self.___extractPath(node)
                # Enpty everything
                self._emptyFringe()
                self.explored.clear()
                self.expanded.clear()
                self.orderOfExp.clear()
                # Add the first new node to explored and expanded
                self.explored.add(node.state)
                self.expanded.add(node.state)
                self.___expand(node)
            # If the node is not the goal and is not expanded
            elif(node.state not in self.expanded): 
                self.expanded.add(node.state)
                self.___expand(node)
            counter -=1
        return 
        util.raiseNotDefined()
        
    def ___extractPath(self, node):
        #extract the path to a specific node
        #this function should return the path (list) to the node
        parentNode = node.parent
        path = []

        path.append(node.direction)
        counter = 1000 # In case of infinity loop
        while(parentNode != None and counter > 0):
            for i in self.orderOfExp:
                if(i.state == parentNode):
                    path.insert(0,i.direction)
                    node = i
                    parentNode = node.parent
                    break
            counter -=1
        # Remove the node with None direction
        for i in path:
            if (i is None):
                path.remove(None)
        return path
        util.raiseNotDefined()

    def ___expand(self, node):
        #expand the branch from a node
        if(node.state == None):
            print("None:", node)
        for i in self.problem.getSuccessors(node.state):
            if(i[0] not in self.explored):
                tempNode = Node(i[0],node.state,i[1],i[2],i[2]+node.totalPathcost)
                self.explored.add(node.state)
                self._addToFringe(tempNode)
        return 
        util.raiseNotDefined()
    def _emptyFringe(self):
        # Empty the fringe in case of arriving at one of the goal
        while(not self.fringe.isEmpty()):
            self.fringe.pop()
        return 

class GreedyBFS(GraphSearch):
    def __init__(self, problem, fringe, heuristic=None):
        super(GreedyBFS, self).__init__(problem, fringe, heuristic)

    def _addToFringe(self, node):
        #Add node to the fringe. Be careful with the type of fringe, you should check it for a suitable addition.
        priority = node.totalPathcost + self.heuristic(node.state, self.problem)
        self.fringe.update(node, priority)
        return 
        util.raiseNotDefined()