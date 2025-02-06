class Personne():
  def __init__(self,age,bonjour):
    self.age = age 
    self.bonjour = bonjour
 
  def afficher(self):
   print("Age :",self.age)
   print("Hello",self.bonjour)

p=Personne("14", "bonjour")
p.afficher()

class Eleve ( Personne ): 

 def afficher(self):
  print("je vais en cours", self.AllerEnCours)
  print("J'ai 14 ans", self.afficherAge)

  p=Eleve("self.AllerEnCours", "self.afficherAge")    
  p.afficher()

class Professeur():
 def __matiereEnseignee(self):

  def enseigner(self):
  print("Le cours va commencer", self.enseigner)

  p=Professeur("self.enseigner"):
  p.afficher 
