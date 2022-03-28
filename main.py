from Environment.env import *
from Agent.agent import *
from Agent.captor import *

if __name__ == '__main__':
    ######### Gloable variable ##########
    SizeDepart = 3
    proba_fire = 1/5
    proba_rubble = 1/5
    X_pos_init_agent = 0
    Y_pos_init_agent = 0
    ###################################

    #creation of the l'environment
    env = CLI_Environment(SizeDepart)
    env.GenerateNewGrid(proba_fire, proba_rubble)
    env.DisplayGrid()

    # creation of the agent
    captor = Captor(proba_fire, proba_rubble, env)

    # creation of the agent
    agent = Agent(X_pos_init_agent, Y_pos_init_agent, captor)
    captor.ChainageAvant()
    captor.DisplayProbaGrid()
    
    agent.UpdateAgentPosition(0,1)
    agent.DisplayAgent()
    captor.ChainageAvant()
    captor.DisplayProbaGrid()
        
    agent.UpdateAgentPosition(1,1)
    agent.DisplayAgent()
    captor.ChainageAvant()
    captor.DisplayProbaGrid()
    # bool = agent.On_Off()

    #bool = True
    #while bool is True:

        # creation of the l'environment
        # SizeDepart += 1
        # env = CLI_Environment(SizeDepart)
        # env.GenerateNewGrid(proba_fire, proba_rubble)
        # env.DisplayGrid()

        #creation of the agent
        #agent = Agent(X_pos_init_agent, Y_pos_init_agent, env, proba_fire, proba_rubble)
        #bool = agent.On_Off()



