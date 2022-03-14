from Environment.env import *
from Agent.agent import *

if __name__ == '__main__':
    ######### Gloable variable ##########
    SizeDepart = 3
    proba_fire = 1/5
    proba_rubble = 1/5
    ###################################
    
    env = CLI_Environment(SizeDepart)
    env.GenerateNewGrid(proba_fire, proba_rubble)
    env.DisplayGrid()