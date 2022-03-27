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

class Agent:

    def __init__(self,  proba_fire, proba_rubble, environment):
        self.proba_fire = proba_fire
        self.proba_rubble = proba_rubble
        self.environment = environment
        self.probaGrid = [[ProbaCase(k, i) for i in range(environment.gridSize)] for k in range(environment.gridSize)]
        self.neighboorslist = self.environment.get_neighboors(Case(self.x_position, self.y_position))
        self.attributesProbaCase = [a for a in dir(self.probaGrid[0][0]) if not a.__contains__('_') and not callable(getattr(self.probaGrid[0][0], a))]

    def Analyse(self):
        toAnalyse = []
        # update the proba grid after moving with sure values
        for case in self.neighboorslist:
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
            if probaCase.heat == 1:
                for neighboor in listUnsureNeighboors:
                    neighboor.fire = 1/n
            if case.dust:
                for neighboor in listUnsureNeighboors:
                    neighboor.rubbble = 1/n
            if case.scream:
                for neighboor in listUnsureNeighboors:
                    neighboor.people = 1/n
        
    # on update une case voisine qu'on a pu observer (une case voisine de la case ou 
    # ce trouve l'agent ou encore la case elle meme ou se trouve l'agent)
    def updateProbaCase(self, case):
        x = case.x_position
        y = case.y_position
        probaCase = self.probaGrid[x][y]
        for attr in self.attributesProbaCase:
            if attr ==  "known":
                probaCase.known = 1
            if getattr(case, attr):
                setattr(probaCase, attr, 3)
            else:
                setattr(probaCase, attr, 0)
    
    def getUnsureNeighboors(self, probaCase):
        L=[]
        for neihboor in self.environnement.get_neighboors(self.environnement.grid[probaCase.x_position][probaCase.y_position]):
            probaCase = self.probaGrid[neihboor.x_position][neihboor.y_postion]
            if probaCase.known == 0:
                L.append(probaCase)
        return L