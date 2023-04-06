class sacado():

    def __init__(self, taille):
        self.t = taille
        self.sac = []
        
    def ajoutersac(self, objet):
        if self.taillesac() < self.t:
            self.sac.append(objet)
            return f"Vous avez ajouté {objet} à votre sac ! Il vous reste {self.t - self.taillesac()} place(s)"
        elif self.taillesac() >= self.t:
            return f"Vous n'avez plus de place dans votre sac"
        else:
            return "Il y a eu une erreur"
    
    def taillesac(self):
        return len(self.sac)

    def __str__(self):
        if self.taillesac() == self.t:
            print("Attention votre sac n'a plus de place !")
        elif self.taillesac() == 0:
            return "Votre sac est vide"
        else:
            return f"Votre sac contient :{self.sac} Il vous reste {self.t - self.taillesac()} place(s)"