import random as rd
import time


class Grid:
    def __init__(self, hauteur, longueur):
        self.hauteur = hauteur
        self.longueur = longueur
        self.grid = [[0 for i in range(longueur)] for j in range(hauteur)]
        self.grid_ = [[0 for i in range(longueur+2)] for j in range(hauteur+2)]

    def input(self,g):
        self.grid = g
        self.sync()

    def gen(self):
        self.grid = [[rd.randint(0,1) for i in range(self.longueur)] for j in range(self.hauteur)]
        return self.grid

    def sync(self):
        for i in range(self.hauteur):
            for j in range(self.longueur):
                self.grid_[i+1][j+1] = self.grid[i][j]

    def affichage(self):
        string = "--"
        for j in range(self.longueur):
            string+= "--"
        string+= "-\n"
        for j in range(len(self.grid)):
            string+="| "
            for i in range(len(self.grid[j])):
                #translate
                if self.grid[j][i] == 1:
                    string += "⬛" + " "
                else:
                    string += "⬜" + " "
            string+= "|\n"
        string += "---"
        for j in range(self.longueur):
            string+= "--"
        return string

    def neighbor(self,i,j):
        neighbor = 0
        self.sync()
        for a in range(-1,2):
            for b in range(-1, 2):
                neighbor += self.grid_[i+1+a][j+1+b]
        return neighbor-self.grid[i][j]

    def rules(self,i,j):
        neighbor = self.neighbor(i,j)
        if self.grid[i][j]==0 and neighbor == 3:
                return 1
        elif self.grid[i][j]==0 :
                return 0
        elif self.grid[i][j] == 1:
            if neighbor < 2 or neighbor>3:
                return 0
            else:
                return 1

    def start(self,n):
        timer = time.time()
        print(self.affichage())
        for t in range(n):
            moy = 0
            gridd = [[0 for i in range(self.longueur)] for j in range(self.hauteur)]
            for i in range(self.hauteur):
                for j in range(self.longueur):
                    gridd[i][j] = self.rules(i,j)
            self.grid = gridd
            print(self.affichage())
            print(time.time()-timer)
            moy+=time.time()-timer
        print(moy/n)
