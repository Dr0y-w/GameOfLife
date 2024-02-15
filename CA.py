import random as rd

class Grid:
    def __init__(self,longueur):
        self.longueur = longueur
        self.grid = [0 for i in range(longueur)]

    def setup(self,grid):
        if len(grid) == self.longueur:
            self.grid = grid

        elif len(grid)<self.longueur:
            for i in range(self.longueur-len(grid)):
                grid.append(0)
            self.grid = grid
        else:
            self.grid = grid[:self.longueur]

    def gen(self):
        self.grid = [rd.randint(0,1) for i in range(self.longueur)]

    def neighbour(self,i):
        sum = 0
        if i!=self.longueur-1 and i!= 0:
            sum += self.grid[i+1] + self.grid[i-1]
        elif i == 0:
            sum += self.grid[i + 1]
        else :
            sum += self.grid[i-1]
        return sum

    def rules(self,i):
        if self.grid[i] == 0:
            if self.neighbour(i) == 1:
                return 1
            else:
                return 0
        elif self.grid[i] == 1:
            return 0

    def affichage(self):
        string = ""
        for i in range(self.longueur):
            string += str(self.grid[i])+" "
        return  string

    def start(self,t):
        for i in range(t):
            newgrid = []
            print(self.translate())
            for j in range(self.longueur):
                newgrid.append(self.rules(j))
            self.grid = newgrid

    def translate(self):
        string = ""
        for i in range(self.longueur):
            if self.grid[i] == 0:
                string += "⬜"
            else:
                string += "⬛"
        return string


g1 = Grid(500)
g1.setup([0 for x in range(250)]+[1])
g1.start(1000)