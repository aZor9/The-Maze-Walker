print("hello world")


class character():
	def __init__(self, pdv, p, m, v):
		point_de_vie = pdv
		position = p
		main = m
		speed = v

#renvois des points de vie avec/sans avec changement de valement
	def vie(self, *args):
		if *args != None :
			self.point_de_vie += *args
		return self.point_de_vie

#changement de la position du personnage <- déplacement
	def droite(self):
		self.position[1] += self.vitesse
		return self.position
	def gauche(self):
		self.position[1] -= self.vitesse
		return self.position
	def haut(self):
		self.position[0] -= self.vitesse
		return self.position
	def bas(self):
		self.position[0] += self.vitesse
		return self.position

#renvois de la vitesse avec/sans avec changement de valement
	def vitesse(self, *args):
		if *args != None :
			self.vitesse += *args
		return self.vitesse
