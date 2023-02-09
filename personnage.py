from copy import deepcopy

class character():
	def __init__(self, pdv, p, m, v, board):
		self.point_de_vie = pdv
		self.position = p
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
		old = deepcopy(self.position)
		self.board[self.position].update(' ')
		self.position[1] += self.speed
		self.board[self.position].update('P')
		return old, self.position
	def gauche(self):
		old = deepcopy(self.position)
		self.board[self.position].update(' ')
		self.position[1] -= self.speed
		self.board[self.position].update('P')
		return old, self.position
	def haut(self):
		old = deepcopy(self.position)
		self.board[self.position].update(' ')
		self.position[0] -= self.speed
		self.board[self.position].update('P')
		return old, self.position
	def bas(self):
		old = deepcopy(self.position)
		self.board[self.position].update(' ')
		self.position[0] += self.speed
		self.board[self.position].update('P')
		return old, self.position

#renvoi de la vitesse avec/sans avec changement de valement
	def vitesse(self, *args):
		if args != None :
			self.speed += args
		return self.speed
