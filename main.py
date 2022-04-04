from Environment.env import *
from Agent.agent import *
from Agent.captor import *
from time import sleep

if __name__ == '__main__':
    print('Enter la taille maximale que la grille pourra atteindre (rentrez un entier):')
    max_size = int(input())
    ######### Gloable variable ##########
    SizeDepart = 4
    proba_fire = 1/5
    proba_rubble = 1/5
    X_pos_init_agent = 0
    Y_pos_init_agent = 0
    ###################################

    #creation of the l'environment
    env = CLI_Environment(SizeDepart)
    env.GenerateNewGrid(proba_fire, proba_rubble)
    # env.GenerateFixGrid()
    env.DisplayGrid()

    # creation of the agent
    captor = Captor(proba_fire, proba_rubble, env)

    # creation of the agent
    agent = Agent(X_pos_init_agent, Y_pos_init_agent, captor)
    bool = agent.On_Off()

    i = 0
    while (bool is True) & (i < max_size):
        sleep(2)
        i += 1
        # creation of the l'environment
        SizeDepart += 1
        env = CLI_Environment(SizeDepart)
        env.GenerateNewGrid(proba_fire, proba_rubble)
        env.DisplayGrid()

        # creation of the agent
        captor = Captor(proba_fire, proba_rubble, env)

        # creation of the agent
        agent = Agent(X_pos_init_agent, Y_pos_init_agent, captor)
        bool = agent.On_Off()
