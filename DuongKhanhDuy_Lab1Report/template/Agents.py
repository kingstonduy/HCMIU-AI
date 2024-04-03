from game import Agent
from game import Directions

class DumbAgent(Agent):
    "An agent that goes East until it can't."
    def getAction(self, state):
        "The agent receives a GameState (defined in pacman.py)."
        print("Location: ", state.getPacmanPosition())
        print("Actions available: ", state.getLegalPacmanActions())
        if Directions.EAST in state.getLegalPacmanActions():
            print("Going East.")
            return Directions.EAST
        else:
            print("Stopping.")
            return Directions.STOP

class RandomAgent(Agent):
    "An agent that picks a random action from the set of legal actions."
    def getAction(self, state):
        import random
        legal = state.getLegalPacmanActions()
        print("Location: ", state.getPacmanPosition())
        print("Actions available: ", legal)
        print("Choosing random action.")
        return random.choice(legal)

class BetterRandomAgent(Agent):
    "An agent that picks a random action from the set of legal actions."
    def getAction(self, state):
        import random
        legal = state.getLegalPacmanActions()
        print("Location: ", state.getPacmanPosition())
        if Directions.STOP in legal: legal.remove(Directions.STOP)
        print("Actions available: ", legal)
        print("Choosing random action.")
        return random.choice(legal)
    
class ReflexAgent(Agent):
    "An agent that eats food if it can."
    def getAction(self, state):
        import random
        legal = state.getLegalPacmanActions()
        print("Location: ", state.getPacmanPosition())
        print("Actions available: ", legal)
        if Directions.STOP in legal: legal.remove(Directions.STOP)
        for action in legal:
            successor = state.generatePacmanSuccessor(action)
            if successor.getNumFood() < state.getNumFood():
                print("Eating food.")
                return action
        print("Choosing random action.")
        return random.choice(legal)