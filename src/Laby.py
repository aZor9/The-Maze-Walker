from random import choice
from Pile import Pile
#cords (YX)

class Case:

    def __init__(self):
        pass


class Secteur:

    def __init__(self, Xsecteur: int, Ysecteur: int) -> None:
        self.Xsecteur = Xsecteur
        self.Ysecteur = Ysecteur

    def __str__(self): # monter le labyrinthe 
        for q in range(len(self.board)):
            for s in range(len(self.board[0])):
                pointer = self.board[q][s]
                if pointer == 0: print(" ", end="")
                if pointer == 'X': print("▓", end="")
                #print(self.board[q][s], end=' ')
            print("")
        return ""


    def voisins(self, v): # calculer les cases a coté 
        V = []
        i, j = v[0], v[1]
        for a in (-2, 2):
            if 0 <= i + a < self.Ysecteur:
                if self.board[i + a][j] == ' ':
                    #self.board[i + a][j] = '*'
                    V.append((i + a, j))
            if 0 <= j + a < self.Xsecteur:
                if self.board[i][j + a] == ' ':
                    #self.board[i][j + a] = '*'
                    V.append((i, j + a))
        return V


    def gen(self):

        # Part 1 : initialize que les murs 
        self.board = [['X' for k in range(self.Xsecteur)] for l in range(self.Ysecteur)]
        for l in range(1, self.Ysecteur): # doubke parcours de boucle et a certains case je fais des troues dans les murs retourne 
            for k in range(1, self.Xsecteur):
                if l % 2 != 0 and k % 2 != 0: self.board[l][k] = ' '
        print (self)
        # Part 2 : generate
        stack = Pile()# enregistre le chemin qui a ete parcourus reviens au depart donc pile vide
        voisins = []

        cords = (int((self.Ysecteur-1)/2)-1, int((self.Xsecteur-1)/2)+1) #position angle superieur droit par rapport au centre de self.board
        voisins = self.voisins((cords[0], cords[1]))
        #self.board[cords[0]][cords[1]] = "5" #start point

        stack.add(cords)


        while len(stack) > 0:# algorithme en lui meme tant que k pile n'est pas vide alors il n'as pas fini  
            voisins = self.voisins((stack[-1][0], stack[-1][1])) #


            if not len(voisins) == 0: # regarde si le voisin 
                nextcase = choice(voisins)

                # cassage des cases intermediaires
                if nextcase[0] == stack[-1][0] and nextcase[1] > stack[-1][1]: self.board[nextcase[0]][nextcase[1]-1] = 0 #droite
                if nextcase[0] == stack[-1][0] and nextcase[1] < stack[-1][1]: self.board[nextcase[0]][nextcase[1]+1] = 0 #gauche
                if nextcase[0] > stack[-1][0] and nextcase[1] == stack[-1][1]: self.board[nextcase[0]-1][nextcase[1]] = 0 #bas
                if nextcase[0] < stack[-1][0] and nextcase[1] == stack[-1][1]: self.board[nextcase[0]+1][nextcase[1]] = 0 #haut

                self.board[nextcase[0]][nextcase[1]] = 0 # case choix par voisin 
                stack.add(nextcase)

            else:
                stack.rem() # si il a pas de voisin il depile 

        # creusage entree et sortie
        directions = ['N', 'E', 'S', 'W']
        sel = []
        sel.append(choice(directions)) # il choisit deux directions 
        directions.remove(sel[0])
        sel.append(choice(directions))


        for d in sel:
            if d == 'N': self.board[0][int((self.Xsecteur+1)/2)] = 0
            elif d == 'S': self.board[-1][int((self.Xsecteur+1)/2)] = 0
            elif d == 'W': self.board[int((self.Ysecteur+1)/2)][0] = 0
            elif d == 'E': self.board[int((self.Ysecteur+1)/2)][-1] = 0
            else:
                pass
        
        #self.note()
        return "Generated !"

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
            fichier.write(s)
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

    

#def note():
    #for i in range 
X, Y = 41, 41
secteur_one = Secteur(X, Y)
secteur_one.gen()
sauv1 = secteur_one.note ()
sau2 = secteur_one.denote ()
print(secteur_one)
print(sauv1)

# convertir en base 16 a partir d la base 2 ce sera plus leger 
