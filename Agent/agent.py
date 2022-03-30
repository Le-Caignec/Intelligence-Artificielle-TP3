

class Agent:

    def __init__(self, x_position, y_position, captor):
        self.x_position = x_position
        self.y_position = y_position
        self.captor = captor
        self.captor.setAgent(self)
        self.peopleFound = False
        self.blockedAgent = False
        self.previousCase = self.captor.environment.grid[x_position][y_position]
        self.listForbidCases = []
        
    #function that enable to display in the console
    #the agent's position
    def DisplayAgent(self):
        print("---AGENT POSITION---")
        print("  - x_position : "+str(self.x_position))
        print("  - y_position : " + str(self.y_position))

    #function that enable to update the agent's position
    def UpdateAgentPosition(self, x_position, y_position):
        self.previousCase = self.captor.environment.grid[self.x_position][self.y_position]
        self.x_position = x_position
        self.y_position = y_position

    def extinguishFire(self, case):
        case.fire = False
        print("Le feu a bien été éteint")
        list_neighbors = self.captor.environment.get_neighboors(case)
        for heat_case in list_neighbors:
            bool = False
            heat_neighbors = self.captor.environment.get_neighboors(heat_case)
            for heat_neighbor in heat_neighbors:
                if heat_neighbor.fire:
                    bool = True
            if not bool:
                heat_case.heat = False

    # Evaluation Function : It will enable to evaluate the cost of a case and
    # improve the decision of the System Expert algorithm
    def Evaluation_single_case(self, probaCase):
        note = 0
        if probaCase.people>=0:
            note += probaCase.people * 200
        if probaCase.fire>=0:
            note += probaCase.fire * -10
        if probaCase.rubble>=0:
            note += probaCase.rubble * -100
        return note
    
    def Evaluation(self, probaCase):
        note = 0
        note += self.Evaluation_single_case(probaCase)
        list_neighboors = self.captor.getUnsureNeighboors(probaCase)
        for neighbor in list_neighboors:
            note += self.Evaluation_single_case(neighbor)
        return note

    #Tant qu'il n'est pas coincé et qu'il n'a pas trouvé la personne il continu
    # a parcourir la grille
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

    #il analyse -> il choisit sa case ->il se déplace(eteindre le feu si il arrive dessus & mettre a jour le booléan si il est coincé)
    def SystemExpert(self):
        self.captor.ChainageAvant()
        neightboorsList = self.captor.getNeighboorslist()
        for case in self.listForbidCases:
            if case in neightboorsList:
                neightboorsList.remove(case)
        if neightboorsList == []:
            self.blockedAgent = True
        else:
            BestNote = self.Evaluation(self.captor.probaGrid[neightboorsList[0].x_position][neightboorsList[0].y_position])
            BestCase = neightboorsList[0]
            for c in neightboorsList[1:]:
                note = self.Evaluation(self.captor.probaGrid[c.x_position][c.y_position])
                if c == self.previousCase:
                    note = note-100
                if BestNote < note:
                    BestNote = note
                    BestCase = c
            if BestCase == self.previousCase:
                self.listForbidCases.append(self.captor.environment.grid[self.x_position][self.y_position])
            if (BestCase.fire is True):
                self.extinguishFire(BestCase)
            self.UpdateAgentPosition(BestCase.x_position, BestCase.y_position)
            if (BestCase.people is True):
                self.peopleFound = True
            if (BestCase.rubble is True):
                self.blockedAgent = True