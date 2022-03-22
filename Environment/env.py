from dataclasses import dataclass
from random import uniform, randint

@dataclass
class Case:
    x_position: int = 0
    y_position: int = 0
    fire: bool = False #Feu
    heat: bool = False #Chaleur
    dust: bool = False #Poussière
    rubble: bool = False #Décombre
    people: bool = False #Victime
    note: int = -1


class CLI_Environment:

    def __init__(self, gridSize):
        self.gridSize = gridSize
        self.grid = [[Case(k, i) for i in range(gridSize)] for k in range(gridSize)]
        self.isNew = False

    # Function that enable to display the actual grid
    def DisplayGrid(self):
        print("-----------------NEW GRID-------------------")
        print("[")
        for y_position in range(self.gridSize):
            for x_position in range(self.gridSize):
                print("[" + self.isFire(x_position, y_position)[0] + "," + self.isHeat(x_position, y_position)[0] + "," + self.isDust(x_position, y_position)[0] + "," + self.isRubble(x_position, y_position)[0]+ "," + self.isPeople(x_position, y_position)[0] + "], ",
                      end='')
            print("")
        print("]")

    # Function which is used to display the grid
    def isFire(self, x_position, y_position):
        if self.grid[x_position][y_position].fire:
            return "F", True
        else:
            return "0", False

    # Function which is used to display the grid
    def isHeat(self, x_position, y_position):
        if self.grid[x_position][y_position].heat:
            return "h", True
        else:
            return "0", False

    # Function which is used to display the grid
    def isDust(self, x_position, y_position):
        if self.grid[x_position][y_position].dust:
            return "d", True
        else:
            return "0", False

    # Function which is used to display the grid
    def isRubble(self, x_position, y_position):
        if self.grid[x_position][y_position].rubble:
            return "R", True
        else:
            return "0", False

    # Function which is used to display the grid
    def isPeople(self, x_position, y_position):
        if self.grid[x_position][y_position].people:
            return "P", True
        else:
            return "0", False

    # Function that clear all the object in the case, diamond will be set to false
    # and dust too
    def ClearCase(self, x_position, y_position):
        self.grid[x_position][y_position].fire = False
        for case in self.get_neighboors(self.grid[x_position][y_position]):
            case.heat = False

    # Function which will give the neighbours of one case
    def get_neighboors(self, case):
        list_neighbors = []
        if case.x_position + 1 <= self.gridSize-1:
            list_neighbors.append(self.grid[case.x_position + 1][case.y_position])
        if case.x_position - 1 >= 0:
            list_neighbors.append(self.grid[case.x_position - 1][case.y_position])
        if case.y_position + 1 <= self.gridSize-1:
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

    #people Setter
    def Setpeople(self):
        y, x = 0, 0
        while (x, y) == (0, 0):
            x, y = randint(0, self.gridSize-1), randint(0, self.gridSize-1)
        self.grid[x][y].people = True

    # Function that will creat a new grid with a random probability to creat
    # a Dust or a Diamond for each case
    def GenerateNewGrid(self, proba_fire, proba_rubble):
        self.Setpeople()
        for x in range(self.gridSize):
            for y in range(self.gridSize):
                if x == 0 and y == 0:
                    pass
                # ajout d'un fire
                else:
                    if not self.grid[x][y].people and uniform(0, 1 / proba_fire) <= 1:
                        self.SetFire(x, y)
                        for case in self.get_neighboors(self.grid[x][y]):
                            self.SetHeat(case.x_position, case.y_position)
                    # ajout d'un rubble
                    if not self.grid[x][y].people and uniform(0, 1 / proba_rubble) <= 1:
                        self.SetRubble(x, y)
                        for case in self.get_neighboors(self.grid[x][y]):
                            self.SetDust(case.x_position, case.y_position)

