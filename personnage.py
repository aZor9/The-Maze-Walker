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
		return point_de_vie

#changement de la position du personnage <- déplacement
	def droite(self, var):
		position[1] =+ 1
		return position
	def gauche(self, var):
		position[1] =+ -1
		return position
	def haut(self, var):
		position[0] =+ -1
		return position
	def bas(self, var):
		position[0] =+ 1
		return position

#renvois de la vitesse avec/sans avec changement de valement
	def vie(self, *args):
		if *args != None :
			self.vitesse += *args
		return vitesse
