from tkinter import N
from Environment.env import Case

class Agent:

    def __init__(self, x_position, y_position, environment,):
        self.x_position = x_position
        self.y_position = y_position
        self.environment = environment
        self.peopleFound = False
        self.blockedAgent = False
        
    #function that enable to display in the console
    #the agent's position
    def DisplayAgent(self):
        print("---AGENT POSITION---")
        print("  - x_position : "+str(self.x_position))
        print("  - y_position : " + str(self.y_position))

    #function that enable to update the agent's position
    def UpdateAgentPosition(self, x_position, y_position):
        self.x_position = x_position
        self.y_position = y_position

    def extinguishFire(self, case):
        case.fire = False
        list_neighbors = self.environment.get_neighboors(case)
        for heat_case in list_neighbors:
            bool = False
            heat_neighbors = self.environment.get_neighbors(heat_case)
            for heat_neighbor in heat_neighbors:
                if heat_neighbor.fire:
                    bool = True
            if not bool:
                heat_case.heat = False

    # Evaluation Function : It will enable to evaluate the cost of a case and
    # improve the decision of the System Expert algorithm
    def Evaluation(self, case):
        if case.heat:
            case.note = 20
            if case.dust:
                case.note = 15
        elif case.dust:
            case.note = 20
        elif case.Fire:
            case.note = 10
            if case.rubble:
                case.note = 5
        elif case.rubble:
            case.note = 10
        else:
            case.note = 30

    def On_Off(self):
        while (self.peopleFound is False) & (self.blockedAgent is False):
            self.SystemExpert()
            self.DisplayAgent()
        if self.peopleFound:
            print("La personne a bien été secourue ")
            return True
        if self.blockedAgent:
            print("Le jeu s'arrete")
            return False

    def SystemExpert(self):
        print("J'avance d'une case vers la plus adéquate")
        self.peopleFound = True

    def ChainageAvant(self):
        self.regleRubble()
        self.regleDust()
        self.regleHeat()
        self.regleFire()
        self.reglePeople()

    def regleFire(self):
        for case in self.neighboorslist:
            if case.fire is True:
                if case.x_position + 1 <= self.gridSize - 1:
                    self.certainprobaGrid[case.x_position + 1][case.y_position].heat = 1.0
                if case.x_position - 1 >= 0:
                    self.certainprobaGrid[case.x_position - 1][case.y_position].heat = 1.0
                if case.y_position + 1 <= self.gridSize - 1:
                    self.certainprobaGrid[case.x_position][case.y_position + 1].heat = 1.0
                if case.y_position - 1 >= 0:
                    self.certainprobaGrid[case.x_position][case.y_position - 1].heat = 1.0

    def regleRubble(self):
        for case in self.neighboorslist:
            if case.rubble is True:
                if case.x_position + 1 <= self.gridSize - 1:
                    self.certainprobaGrid[case.x_position + 1][case.y_position].dust = 1.0
                if case.x_position - 1 >= 0:
                    self.certainprobaGrid[case.x_position - 1][case.y_position].dust = 1.0
                if case.y_position + 1 <= self.gridSize - 1:
                    self.certainprobaGrid[case.x_position][case.y_position + 1].dust = 1.0
                if case.y_position - 1 >= 0:
                    self.certainprobaGrid[case.x_position][case.y_position - 1].dust = 1.0

    def regleHeat(self):
        for case in self.neighboorslist:
            if case.heat is True:
                return True
            return False

    def regleDust(self):
        for case in self.neighboorslist:
            if case.Dusst is True:
                return True
            return False

    def reglePeople(self):
        for case in self.neighboorslist:
            if case.people is True:
                return True
            return False
