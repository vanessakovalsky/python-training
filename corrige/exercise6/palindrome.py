liste_mot_klingon = ['dfsqfhdqsk', 'jkgshjkg', 'jkgfhskg','fhdskksf']

def check_palindrome(v): 
    reverse = v[::-1]   
  
    if v in (liste_mot_klingon) and v == reverse: 
        return True
    return False
  
  
var = input(str("Entrez une valeur: "))
if check_palindrome(var):
    print("L'entrée est un palindrome")
else:
    print("L'entrée n'est pas un palindrome")