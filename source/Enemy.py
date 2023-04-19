from random import randint, choice
from Pile import Pile
from deepcopy import deepcopy

class Enemy:

    def __init__(self, board, secteur):
        self.state = 'e'
        self.secteur = secteur
        self.coos = (randint(1, 40), randint(1, 40))
        board[self.secteur][self.coos[0]][self.coos[1]].update(self.state)

    def __str__(self):
        return str(self.state)

    def __calc_dist__(self, board, player_coos):
        pass

    def voisins1(xy, board): #fonction interne mais réutilisable, revoie les voisins d'une case (v) ! 2 de distance !
        V = []
        i, j = v[0], v[1]
        for a in (-1, 1):
            if 0 <= i + a < 3 * 41:
                if str(board[i + a][j]) == ' ':
                    #self.board[i + a][j] = '*'
                    V.append((i + a, j))
            if 0 <= j + a < 3 * 41:
                if str(board[i][j + a]) == ' ':
                    #self.board[i][j + a] = '*'
                    V.append((i, j + a))
        return V

    def move(self, board):
        voisins = Enemy.voisins1()
        new_pos = choice(voisins)
        board[self.secteur][self.coos[0]][self.coos[1]].update(' ')
        self.coos = deepcopy(new_pos)
        board[self.secteur][self.coos[0]][self.coos[1]].update(self.state)
