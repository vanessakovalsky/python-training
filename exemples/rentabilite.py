class CalculatriceRentabilite: 
    # Propriété de ma classe
    montant_depart = 0
    taux_interet = 5
    somme_a_atteindre = 6000

    #Méthode de ma classe
    def calculRentabilite(self):
        self.montant_depart +=  self.montant_depart * (self.taux_interet / 100) 
        annee = 0

        annee_capital = {}
        if self.montant_depart != 0: 
            while self.montant_depart <= self.somme_a_atteindre :
                self.montant_depart = self.montant_depart + self.montant_depart * (self.taux_interet/100)
                annee += 1
                annee_capital[annee] = self.montant_depart

            return annee_capital
        else: 
            return 'Le montant de départ ne peut pas être 0'


