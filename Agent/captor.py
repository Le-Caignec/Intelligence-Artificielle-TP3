from asyncio.windows_events import NULL
from dataclasses import dataclass
from Environment.env import Case

@dataclass
class ProbaCase:
    x_position: int = 0
    y_position: int = 0
    fire: int = -1  # Feu
    heat: int = -1  # Chaleur
    dust: int = -1  # Poussière
    rubble: int = -1  # Décombre
    scream: int = -1 # crie
    people: int = -1 # Victime
    known: int = 0 # assess the level of knowing 
                    # 0 : not all the values are sure
                    # 1 : all the values are known and analysed

class Captor:

    def __init__(self,  proba_fire, proba_rubble, environment):
        self.proba_fire = proba_fire
        self.proba_rubble = proba_rubble
        self.environment = environment
        self.agent = NULL
        self.probaGrid = [[ProbaCase(k, i) for i in range(environment.gridSize)] for k in range(environment.gridSize)]
        self.attributesProbaCase = [a for a in dir(self.probaGrid[0][0]) if not a.__contains__('_') and not callable(getattr(self.probaGrid[0][0], a))]

    def setAgent(self, agent):
        self.agent = agent

    def getNeighboorslist(self):
        return self.environment.get_neighboors(Case(self.agent.x_position, self.agent.y_position))


    def DisplayProbaGrid(self):
        print("-----------------NEW GRID-------------------")
        print("[")
        for y_position in range(self.environment.gridSize):
            for x_position in range(self.environment.gridSize):
                print(self.probaGrid[x_position][y_position])
            print("")
        print("]")

    def ChainageAvant(self):
        toAnalyse = []
        # update the proba grid after moving with sure values
        L = self.getNeighboorslist()
        L.append(self.environment.grid[self.agent.x_position][self.agent.y_position])
        for case in L:
            x = case.x_position
            y = case.y_position
            probaCase = self.probaGrid[x][y]
            if probaCase.known == 0:
                self.updateProbaCase(case)
                toAnalyse.append(probaCase)
                
        # update the rest of the grid with unsure values from values with knowing level 1
        for probaCase in toAnalyse:
            listUnsureNeighboors = self.getUnsureNeighboors(probaCase)
            n = listUnsureNeighboors
            if probaCase.heat == 3:
                for neighboor in listUnsureNeighboors:
                    if neighboor.fire <= 0:
                        neighboor.fire = 1
                    elif neighboor.fire >=1:
                        neighboor.fire = 2                    
            if probaCase.dust == 3:
                for neighboor in listUnsureNeighboors:
                    if neighboor.rubble <= 0:
                        neighboor.rubble = 1
                    elif neighboor.rubble >=1:
                        neighboor.rubble = 2     
            if probaCase.scream == 3:
                for neighboor in listUnsureNeighboors:
                    if neighboor.people <= 0:
                        neighboor.people = 1
                    elif neighboor.people >=1:
                        neighboor.people = 2     
        
    # on update une case voisine qu'on a pu observer (une case voisine de la case ou 
    # ce trouve l'agent ou encore la case elle meme ou se trouve l'agent)
    def updateProbaCase(self, case):
        x = case.x_position
        y = case.y_position
        probaCase = self.probaGrid[x][y]
        for attr in self.attributesProbaCase:
            if attr ==  "known":
                probaCase.known = 1
            elif getattr(case, attr):
                setattr(probaCase, attr, 3)
            else:
                setattr(probaCase, attr, 0)
    
    def getUnsureNeighboors(self, probaCase):
        L=[]
        for neihboor in self.environment.get_neighboors(self.environment.grid[probaCase.x_position][probaCase.y_position]):
            probaCase = self.probaGrid[neihboor.x_position][neihboor.y_position]
            if probaCase.known == 0:
                L.append(probaCase)
        return L