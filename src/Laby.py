from random import choice
from Pile import Pile
#cords (YX)

class Case:

    def __init__(self, e = False):
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

class Secteur:

    def __init__(self, Xsecteur: int, Ysecteur: int, entree = False, sortie = False) -> None:
        self.Xsecteur = Xsecteur
        self.Ysecteur = Ysecteur
        self.entree = entree
        self.sortie = sortie

    def __str__(self):
        for q in range(len(self.board)):
            for s in range(len(self.board[0])):
                pointer = str(self.board[q][s])
                try: pointer = int(pointer)
                except : pass
                if pointer == 0: print(" ", end="")
                if pointer == 'X': print("▓", end="")
                else:
                    print(pointer)
            print("") # gestion de l'affichage si mur ou vide
        return ""

    def __getitem__(self, i):
        return self.board[i] # renvoie la ligne[i] du secteur ( pour parcours notamment )


    def voisins(self, v): #fonction interne mais réutilisable, revoie les voisins d'une case (v) ! 2 de distance !
        V = []
        i, j = v[0], v[1]
        for a in (-2, 2):
            if 0 <= i + a < self.Ysecteur:
                if str(self.board[i + a][j]) == ' ':
                    #self.board[i + a][j] = '*'
                    V.append((i + a, j))
            if 0 <= j + a < self.Xsecteur:
                if str(self.board[i][j + a]) == ' ':
                    #self.board[i][j + a] = '*'
                    V.append((i, j + a))
        return V


    def gen(self): #génère un labyrinthe avec les coordonnées du secteur (constante, X and Y = 41)

        # Part 1 : initialize
        self.board = [[Case() for k in range(self.Xsecteur)] for l in range(self.Ysecteur)] # que des murs
        for l in range(1, self.Ysecteur):
            for k in range(1, self.Xsecteur):
                if l % 2 != 0 and k % 2 != 0: self.board[l][k].update(' ') #trous en quadrillage, 1 murs entre chaque trou (bordure ignorée)

        # Part 2 : generate
        # L'algorithme de génération en lui-même (exploration exhaustive) 
        stack = Pile()
        voisins = []

        cords = (int((self.Ysecteur-1)/2)-1, int((self.Xsecteur-1)/2)+1) #position angle superieur droit par rapport au centre de self.board
        voisins = self.voisins((cords[0], cords[1]))
        #self.board[cords[0]][cords[1]] = "5" #start point

        stack.add(cords)


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

        sel = []
        # creusage entree et sortie
        #si entree ou sortie pas définit dans l'appel de la class, on en génère deux
        if not self.entree or not self.sortie:
            directions = ['N', 'E', 'S', 'W']
            sel.append(choice(directions))
            directions.remove(sel[0])
            sel.append(choice(directions))
            #4C2, directions des i/o

        else:
            sel.append(self.entree)
            sel.append(self.sortie)

        #on casse les block N/E/S/W selon les choisis
        for d in sel:
            if d == 'N': self.board[0][int((self.Xsecteur+1)/2)].update(0)
            elif d == 'S': self.board[-1][int((self.Xsecteur+1)/2)].update(0)
            elif d == 'W': self.board[int((self.Ysecteur+1)/2)][0].update(0)
            elif d == 'E': self.board[int((self.Ysecteur+1)/2)][-1].update(0)
            else:
                pass

        return "Generated !"


class Labyrinthe:

    def __init__(self):

        #liste entrées
        params = [('S', 'E'), ('W', 'E'), ('W', 'S'), ('N', 'S'), (0, 0), ('N', 'S'), ('N', 'E'), ('W', 'E'), ('N', 'W')]

        # on défini labyrinthe comme étant une liste de 9 secteurs
        self.megaboard = []
        for i in range(9):
            self.megaboard.append(Secteur(41, 41, params[i][0], params[i][1]))
            self.megaboard[i].gen()

        # comme le secteur 4 (le bloc) doit être relié horizontalement et verticalement aux autres:
        self.megaboard[4][-1][21].update(0)
        self.megaboard[4][21][-1].update(0)
        self.megaboard[4][21][0].update(0)
        self.megaboard[4][0][21].update(0)

        self.megaboard[1][-1][21].update(0)
        self.megaboard[3][21][-1].update(0)
        self.megaboard[5][21][0].update(0)
        self.megaboard[7][0][21].update(0)

        # le secteur 4 (le bloc) n'est pas un labyrinthe, c'est un espace vide (bordures ignorées)
        for i in range(41):
            for j in range(41):
                if i != 0 and i != 40 and j != 0 and j != 40:
                    self.megaboard[4][i][j].update(0)
    
    def __getitem__(self, y, x, z=None):
        if z == None:
            newz = 0
            if y > 2*41+1:
                newz = 6
            elif y >= 41:
                newz = 3
            
            if x >= 2*41+1:
                newz += 2
            elif x >= 41:
                newz += 1                

        return self.megaboard[newz][y][x]

    def __str__(self):
        """
        Cette fonction d'affichage est très lourde pour des raisons de compléxité:
        ╔═════════╦════════════╗
        ║  avant  ║ maintenant ║
        ╠═════════╬════════════╣
        ║ O(n^4)  ║   O(n^2)   ║
        ╚═════════╩════════════╝
        // non ce n'est pas un copié collé

        On prend les secteurs par 3 (une "grande" ligne) et on affiche les lignes une à une (en changeant de secteur si la ligne du secteur est finie)
        C'est peut-être pas clair comment j'explique mais c'est compliqué (Labyrinthe est en 4 dimensions, 2° dimension de 2° dimension)
        """

        for k in range(41):

            for q in range(41):
                pointer = str(self.megaboard[0][k][q])
                try: pointer = int(pointer)
                except: pass
                if pointer == 0:
                    print(" ", end="")
                else:
                    print(pointer, end="")

            for q in range(41):
                pointer = str(self.megaboard[1][k][q])
                try: pointer = int(pointer)
                except: pass
                if pointer == 0:
                    print(" ", end="")
                else:
                    print(pointer, end="")

            for q in range(41):
                pointer = str(self.megaboard[2][k][q])
                try: pointer = int(pointer)
                except: pass
                if pointer == 0:
                    print(" ", end="")
                else:
                    print(pointer, end="")

            print("")

        for k in range(41):

            for q in range(41):
                pointer = str(self.megaboard[3][k][q])
                try: pointer = int(pointer)
                except: pass
                if pointer == 0:
                    print(" ", end="")
                else:
                    print(pointer, end="")

            for q in range(41):
                pointer = str(self.megaboard[4][k][q])
                try: pointer = int(pointer)
                except: pass
                if pointer == 0:
                    print(" ", end="")
                else:
                    print(pointer, end="")

            for q in range(41):
                pointer = str(self.megaboard[5][k][q])
                try: pointer = int(pointer)
                except: pass
                if pointer == 0:
                    print(" ", end="")
                else:
                    print(pointer, end="")

            print("")

        for k in range(41):

            for q in range(41):
                pointer = str(self.megaboard[6][k][q])
                try: pointer = int(pointer)
                except: pass
                if pointer == 0:
                    print(" ", end="")
                else:
                    print(pointer, end="")

            for q in range(41):
                pointer = str(self.megaboard[7][k][q])
                try: pointer = int(pointer)
                except: pass
                if pointer == 0:
                    print(" ", end="")
                else:
                    print(pointer, end="")

            for q in range(41):
                pointer = str(self.megaboard[8][k][q])
                try: pointer = int(pointer)
                except: pass
                if pointer == 0:
                    print(" ", end="")
                else:
                    print(pointer, end="")

            print("")

        return ""


    def getMegaIndex(z, y, x):
        if z == 0: return (y, x)
        elif z == 1: return (y, 41 + x)
        elif z == 2: return (y, 2 * 41 + x)
        elif z == 3: return (41 + y, x)
        elif z == 4: return (41 + y, 41 + x)
        elif z == 5: return (41 + y, 2 * 41 + x)
        elif z == 6: return (2 * 41 + y, x)
        elif z == 7: return (2 * 41 + y, 41 + x)
        elif z == 8: return (2 * 41 + y, 2 * 41 + x)
        else: return None
    
    def getBoardIndex(z, y, x):
        if z == None:
            newz = 0
            if y > 2*41+1:
                newz = 6
            elif y >= 41:
                newz = 3
            
            if x >= 2*41+1:
                newz += 2
            elif x >= 41:
                newz += 1                

        return (newz, y, x)
        
    def note (self):
        sauv = []          
        for i in range(self.Xsecteur):
            for j in range(self.Ysecteur):
                if self.board[i][j] == 0:
                    sauv.append(1)
                else :
                    sauv.append(0)
        sauvstr = ''.join(map(str, sauv))
        #print(sauvstr)
        sauvints = int(sauvstr)
        print(sauvints)
        s = hex(sauvints)
        with open ("save.txt", "w") as fichier:
            fichier.write(s) # sauvegarde le èlaby dans un fichier texte autre 
        #with open ("save.txt", "r") as fichier:
            #fichier.read()   
    
    def denote(self):
        with open("save.txt", "r" ) as fichier :
            note = fichier.read()
        #print (note)
        notebin = note.split()
        print(notebin[0])
        notebin = int(notebin[0], 16)
        print (notebin)
        for i in range(self.Xsecteur):
            for j in range(self.Ysecteur):
                if self.board[i][j] == 0:
                    sauv.append(1)
                else :
                    .append(0)

LABY = Labyrinthe()
print(LABY)

"""
Perfs :
~1100ms pour générer et afficher un labyrinthe sur un ordinateur fixe type lycée. 
"""
