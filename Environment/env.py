from dataclasses import dataclass
from random import uniform

@dataclass
class Case:
    x_position: int = 0
    y_position: int = 0
    fire: bool = False #Feu
    heat: bool = False #Chaleur
    dust: bool = False #Poussière
    rubble: bool = False #décombre


class CLI_Environment:

    def __init__(self, gridSize):
        self.gridSize = gridSize
        self.grid = [[Case(k, i) for i in range(gridSize)] for k in range(gridSize)]
        self.isNew = False

    # Function that enable to display the actual grid
    def DisplayGrid(self):
        print("-----------------NEW GRID-------------------")
        print("[")
        for y_position in range(5):
            for x_position in range(5):
                print("[" + self.isFire(x_position, y_position) + "," + self.isHeat(x_position, y_position) + "," + self.isDust(x_position, y_position) + "," + self.isRubble(x_position, y_position) + "], ",
                      end='')
            print("")
        print("]")

# Function which is used to display the grid
    def isFire(self, x_position, y_position):
        if self.grid[x_position][y_position].fire:
            return "Fire"
        else:
            return "00000"

    # Function which is used to display the grid
    def isHeat(self, x_position, y_position):
        if self.grid[x_position][y_position].heat:
            return "Heat"
        else:
            return "00000"

    # Function which is used to display the grid
    def isDust(self, x_position, y_position):
        if self.grid[x_position][y_position].dust:
            return "Dust"
        else:
            return "00000"

    # Function which is used to display the grid
    def isRubble(self, x_position, y_position):
        if self.grid[x_position][y_position].rubble:
            return "Rubble"
        else:
            return "00000"

    # Function that clear all the object in the case, diamond will be set to false
    # and dust too
    def ClearCase(self, x_position, y_position):
        self.grid[x_position][y_position].fire = False
        self.grid[x_position][y_position].heat = False
        self.grid[x_position][y_position].rubble = False
        self.grid[x_position][y_position].dust = False

    # Function which will give the neighbours of one case
    def get_neighboors(self, case):
        list_neighbors = []
        if case.x_position + 1 <= 4:
            list_neighbors.append(self.grid[case.x_position + 1][case.y_position])
        if case.x_position - 1 >= 0:
            list_neighbors.append(self.grid[case.x_position - 1][case.y_position])
        if case.y_position + 1 <= 4:
            list_neighbors.append(self.grid[case.x_position][case.y_position + 1])
        if case.y_position - 1 >= 0:
            list_neighbors.append(self.grid[case.x_position][case.y_position - 1])
        return list_neighbors

    # Diamond Setter
    def SetFire(self, x, y):
        self.grid[x][y].fire = True

    # Dust Setter
    def SetHeat(self, x, y):
        self.grid[x][y].heat = True

    # Diamond Setter
    def SetRubble(self, x, y):
        self.grid[x][y].rubble = True

    # Dust Setter
    def SetDust(self, x, y):
        self.grid[x][y].dust = True

    # Function that will creat a new grid with a random probability to creat
    # a Dust or a Diamond for each case
    def GenerateNewGrid(self, proba_fire, proba_heat, proba_rubble, proba_dust):
        for x in range(self.gridSize):
            for y in range(self.gridSize):
                # ajout d'un fire
                if uniform(0, 1 / proba_fire) <= 1:
                    self.SetFire(x, y)
                # ajout d'un heat
                if uniform(0, 1 / proba_heat) <= 1:
                    self.SetHeat(x, y)
                # ajout d'un rubble
                if uniform(0, 1 / proba_rubble) <= 1:
                    self.SetRubble(x, y)
                # ajout de Dust
                if uniform(0, 1 / proba_dust) <= 1:
                    self.SetDust(x, y)

