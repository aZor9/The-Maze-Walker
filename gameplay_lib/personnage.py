from copy import deepcopy
#from temps import __convertisseur__

class character():
	def __init__(self, pdv, p, m, v, board):
		self.point_de_vie = pdv
		self.position = list(deepcopy(p))
		self.main = m
		self.speed = v
		self.board = board

	def __str__(self):
		return "P"

#renvoi des points de vie avec/sans avec changement de valement
	def vie(self, *args):
		if args != None :
			self.point_de_vie += args
		return self.point_de_vie

#changement de la position du personnage <- déplacement
	def droite(self):
		
		self.position[1] += self.speed
		if (self.board[self.position[0]][self.position[1]].state == 'X'):
			self.position[1] -= self.speed
		return self.position
		
	def gauche(self):
		
		self.position[1] -= self.speed
		if (self.board[self.position[0]][self.position[1]].state == 'X'):
			self.position[1] += self.speed
		return self.position
	def haut(self):
		
		self.position[0] -= self.speed
		if (self.board[self.position[0]][self.position[1]].state == 'X'):
			self.position[0] += self.speed
		return self.position
	
	def bas(self):
		
		self.position[0] += self.speed
		if (self.board[self.position[0]][self.position[1]].state == 'X'):
			self.position[0] -= self.speed
		return self.position

#renvoi de la vitesse avec/sans avec changement de valement
	def vitesse(self, new):
		if args != None :
			self.speed = new
		return self.speed
