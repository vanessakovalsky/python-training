from utilisateur import Utilisateur

class Membre(Utilisateur):
    is_membre = True
    def isMembre(self):
        return True

    def modifieMesInfos(self, dictionnaire_donnes):
        # On vérifie que l'utilisateur est connecté
        if self.connecte :
            print('connecte')
            # Vérifie que les informations saisies par l'utilisatuer correspondent aux siennes, on utilise le pseudo
            if self._pseudo == dictionnaire_donnes['_pseudo']:
                print('pseudo ok')
                dictionnaire_donnes['_nom'] = input('Nom')
                dictionnaire_donnes['_prenom'] = input('prenom')
                nouvelle_donnees = ','.join(dictionnaire_donnes.values())
                self.SupprimeUtilisateur(self._pseudo)
                self.AjoutUtilisateur(nouvelle_donnees)
                #return mes_donnees 
            else :
                return 'Vous ne pouvez modifier que vos propres données'
        else:
            return 'Merci de vous connecter'
