print("hello world")


class character():
	def __init__(self, pdv, p, m, v, board):
		self.point_de_vie = pdv
		self.position = p
		self.main = m
		self.speed = v
		self.blit(board)

	def __str__(self):
		return "P"
	
	def blit(self, board):
		board[self.position]
		return board

#renvoi des points de vie avec/sans avec changement de valement
	def vie(self, *args):
		if args != None :
			self.point_de_vie += args
		return self.point_de_vie

#changement de la position du personnage <- déplacement
	def droite(self):
		self.position[1] += self.speed
		return self.position
	def gauche(self):
		self.position[1] -= self.speed
		return self.position
	def haut(self):
		self.position[0] -= self.speed
		return self.position
	def bas(self):
		self.position[0] += self.speed
		return self.position

#renvoi de la vitesse avec/sans avec changement de valement
	def vitesse(self, *args):
		if args != None :
			self.speed += args
		return self.speed
