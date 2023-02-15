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
		if self.board[(self.position[0], self.position[1] + 1)].state == "X": return True
		self.board[self.position].update(' ')
		self.position[1] += self.speed
		self.board[self.position].update('P')
		return 
		
	def gauche(self):
		if self.board[(self.position[0], self.position[1]-1)].state == "X": return True
		self.board[self.position].update(' ')
		self.position[1] -= self.speed
		self.board[self.position].update('P')
		return 
		
	def haut(self):
		if self.board[(self.position[0] - 1, self.position[1])].state == "X": return True
		self.board[self.position].update(' ')
		self.position[0] -= self.speed
		self.board[self.position].update('P')
		return 
	
	def bas(self):
		if self.board[(self.position[0] + 1, self.position[1])].state == "X": return True
		self.board[self.position].update(' ')
		self.position[0] += self.speed
		self.board[self.position].update('P')
		return 

#renvoi de la vitesse avec/sans avec changement de valement
	def vitesse(self, *args):
		if args != None :
			self.speed += args
		return self.speed
