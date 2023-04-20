from random import choice, randint
from Pile import Pile
from copy import deepcopy
from os import _exit
from time import sleep
from gameplay import wincase
#self.mcords (YX)

class Case:

    def __init__(self, e = False):
        self.ttl_trace = 0
        if not e:
            self.state = 'X'
        else:
            self.state = e

    def __str__(self):
        return str(self.state)

    def __int__(self):
        if isinstance(self.state, int):
            return self.state
        else:
            return -418

    def update(self, e):
        self.state = e
        return self

    def set_trace(self, duree = 5, chg_state = 2):
        self.state = '+'
        self.ttl_trace = duree
        self.chg_state = chg_state

    def upt_trace(self):
        if self.ttl_trace > 0:
            self.ttl_trace -= 1
            if self.ttl_trace == self.chg_state:
                self.state = '•'
            elif self.ttl_trace == 0:
                self.state = 0

class Labyrinthe:

    def __init__(self, Xsecteur: int, Ysecteur: int, sortie = False) -> None:
        self.board = []
        self.X = 2*Xsecteur+1
        self.Y = 2*Ysecteur+1
        self.sortie = sortie
        self.player = None
        self.pcoos = []
        self.plast = 0
        self.mcords  = (int((self.Y-1)/2), int((self.X-1)/2))
        self.trace_lst = []

    def __str__(self):
        output = ""
        for q in range(len(self.board)):
            line = ""
            for s in range(len(self.board[0])):
                pointer = str(self.board[q][s])
                try: pointer = int(pointer)
                except : pass
                if pointer in (0, 'S'): line += ' '
                elif pointer == 'X': line += '█'
                else:
                    line += str(pointer)
            output += line
        print(output)
        return ""

    def __getitem__(self, i):
        return self.board[i] # renvoie la ligne[i] du secteur ( pour parcours notamment )


    def voisins(self, v): #fonction interne mais réutilisable, revoie les voisins d'une case (v) ! 2 de distance !
        V = []
        i, j = v[0], v[1]
        for a in (-2, 2):
            if 0 <= i + a < self.Y:
                if str(self.board[i + a][j]) == ' ':
                    #self.board[i + a][j] = '*'
                    V.append((i + a, j))
            if 0 <= j + a < self.X:
                if str(self.board[i][j + a]) == ' ':
                    #self.board[i][j + a] = '*'
                    V.append((i, j + a))
        return V


    def gen(self): #génère un labyrinthe avec les coordonnées du secteur (constante, X and Y = 41)

        # Part 1 : initialize
        self.board = [[Case() for k in range(self.X)] for l in range(self.Y)] # que des murs
        for l in range(1, self.Y):
            for k in range(1, self.X):
                if l % 2 != 0 and k % 2 != 0: self.board[l][k].update(' ') #trous en quadrillage, 1 murs entre chaque trou (bordure ignorée)

        # Part 2 : generate
        # L'algorithme de génération en lui-même (exploration exhaustive)
        stack = Pile()
        voisins = []

        voisins = self.voisins((self.mcords[0], self.mcords[1]))
        #self.board[self.mcords[0]][self.mcords[1]] = "5" #start point

        stack.add(self.mcords)


        while len(stack) > 0:
            voisins = self.voisins((stack[-1][0], stack[-1][1]))


            if not len(voisins) == 0:
                nextcase = choice(voisins)

                # calcul et cassage des cases intermediaires
                if nextcase[0] == stack[-1][0] and nextcase[1] > stack[-1][1]: self.board[nextcase[0]][nextcase[1]-1].update(0) #droite
                if nextcase[0] == stack[-1][0] and nextcase[1] < stack[-1][1]: self.board[nextcase[0]][nextcase[1]+1].update(0) #gauche
                if nextcase[0] > stack[-1][0] and nextcase[1] == stack[-1][1]: self.board[nextcase[0]-1][nextcase[1]].update(0) #bas
                if nextcase[0] < stack[-1][0] and nextcase[1] == stack[-1][1]: self.board[nextcase[0]+1][nextcase[1]].update(0) #haut

                self.board[nextcase[0]][nextcase[1]].update(0)
                stack.add(nextcase)
                #on choisit une case possible parmi la liste de voisins, on casse la case entre la position actuelle et cette nouvelle case et on "se déplace" sur cette case (ajout à la pile)

            else:
                stack.rem()

        for tx in (-3, -2, -1, 0, 1, 2, 3):
            for ty in (-3, -2, -1, 0, 1, 2, 3):
                self.board[self.mcords[0]+tx][self.mcords[1]+ty].update(0)


        if not self.sortie:
            self.sortie = choice(['N', 'E', 'S', 'W'])
        #on casse les block N/E/S/W selon les choisis

        yimp_lst, ximp_lst = [oy for oy in range(1, self.Y, 2)], [ox for ox in range(1, self.X, 2)]

        if self.sortie == 'N': self.board[0][choice(ximp_lst)].update('S')
        elif self.sortie == 'S': self.board[-1][choice(ximp_lst)].update('S')
        elif self.sortie == 'W': self.board[choice(yimp_lst)][0].update('S')
        elif self.sortie == 'E': self.board[choice(yimp_lst)][-1].update('S')

        return "Generated !"

    def set_player(self, p):
        self.player = p
        self.pcoos = [deepcopy(self.mcords[0]), deepcopy(self.mcords[1])]
        self.board[self.pcoos[0]][self.pcoos[1]].update('P')

    def move(self, newcoos):
        for trc in self.trace_lst:
            trc.upt_trace()
            if trc.ttl_trace == 0:
                self.trace_lst.remove(trc)

        #self.board[self.pcoos[0]][self.pcoos[1]].update(deepcopy(self.plast))
        self.board[self.pcoos[0]][self.pcoos[1]].set_trace(7)
        self.trace_lst.append(self.board[self.pcoos[0]][self.pcoos[1]])
        #self.plast = deepcopy(self.board[newcoos[0]][newcoos[1]])
        self.board[newcoos[0]][newcoos[1]].update('P')
        self.pcoos = [deepcopy(newcoos[0]), deepcopy(newcoos[1])]
        # END CASE //
        if str(self.plast) == 'S':
            # LE JOUEUR PASSE PAR LA SORTIE
            wincase()


        """def blind(self):
        output = ""
        for by in (-2, -1, 0, 1, 2):
            line = ""
            for bx in (-2, -1, 0, 1, 2):
                try:
                    pointer = str(self.board[self.pcoos[0] + by][self.pcoos[1] + bx])
                    try: pointer = int(pointer)
                    except : pass
                    if pointer in (0, 'S'): line += ' '
                    elif pointer == 'X': line += '█'
                    else:
                        line += str(pointer)
                except:
                    line += ' '
            output += line
        print(line)"""

    def first_print(self):
        output = ""
        for by in ([fy for fy in range(-10, 11)]):
            line = ""
            for bx in ([fx for fx in range(-10, 11)]):
                if (by in (-10, 10)) or (bx in (-10, 10)):
                    line += '▒'
                elif (by in (-9, -8, 8, 9)) or (bx in (-9, -8, 8, 9)):
                    line += '░'
                else:
                    try:
                        pointer = str(self.board[self.pcoos[0] + by][self.pcoos[1] + bx])
                        try: pointer = int(pointer)
                        except : pass
                        if pointer in (0, 'S'): line += ' '
                        elif pointer == 'X': line += '█'
                        else: line += str(pointer)
                    except:
                        line += '█'
            output += line + '\n'
        print(output)
        return ""

    def renderv2(self):
        rdrv2_ylst = [self.pcoos[0]+dy for dy in (-2, -1, 0, 1, 2)]
        rdrv2_xlst = [self.pcoos[1]+dx for dx in (-2, -1, 0, 1, 2)]
        output = ""
        for d in range(len(self.board)):
            line = ""
            for f in range(len(self.board[0])):
                if ((d in rdrv2_ylst) and (f in rdrv2_xlst)) or (str(self.board[d][f]) == '+') or (str(self.board[d][f]) == '•'):
                    pointer = str(self.board[d][f])
                    try: pointer = int(pointer)
                    except : pass
                    if pointer in (0, 'S'): line += ' '
                    elif pointer == 'X': line += '█'
                    else: line += str(pointer)
                else:
                    line += ' '
            output += line + '\n'
        print(output)
        return ""
