import random
class Grid:
	def __init__(self,x0=0):
		self.taille=x0
		valeurs_pieces=[5,10,20,50,100,200]
		self.Grid=[[valeurs_pieces[random.randint(0,5)]for j in range(x0)] for i in range(x0)]
	def affiche_element(self,i=0,j=0):
		print(self.Grid[i][j])
	def affiche_taille(self):
		print(self.taille)
	def set_element(self,i=0,j=0,valeur=None):
		self.Grid[i][j]=valeur
	def __contains__(self,p):
		if (p[0]>=0 and p[0]<self.taille and p[1]>=0 and p[1]<self.taille):
			return True 
		else:
			return False
class Player:
	def __init__(self,nom=None):
		self.nom=nom
		self.score=0
	def affiche_nom(self):
		print(self.nom)
	def affiche_score(self):
		print(self.score)
	def incrementer_score(self,valeur=0):
		self.score+=valeur
class Game:
	def __init__(self,taille=0,noms=[]):
		liste_joueurs=[]
		for i in noms:
			liste_joueurs=liste_joueurs+[Player(i)]
		self.liste_joueurs=liste_joueurs
		self.grille=Grid(taille)
		self.identite_joueur_courant=liste_joueurs[0]
		self.tour=0
		self.x=int(taille/2)
		self.y=int(taille/2)
		self.deplacement_possible=False
	def translate(self,dx=0,dy=0):
		self.x+=dx
		self.y+=dy
	def deplacement(self,dx,dy):
		if((self.x+dx,self.y+dy)in self.grille and self.grille.Grid[self.x+dx][self.y+dy]!=None):
			self.translate(dx,dy)
			self.identite_joueur_courant.incrementer_score(self.grille.Grid[self.x][self.y])
			self.grille.Grid[self.x][self.y]=None
			self.deplacement_possible=True
			self.tour+=1
			self.identite_joueur_courant=self.liste_joueurs[self.tour%len(self.liste_joueurs)]
	def jouer_un_coup(self):
		self.deplacement_possible=False
		while(self.deplacement_possible==False):
			var=input(" à "+ self.identite_joueur_courant.nom+" de jouer : ")
			if(var=="e"):
				self.deplacement(0,1)
			elif(var=="o"):
				self.deplacement(0,-1)
			elif(var=="n"):
				self.deplacement(-1,0)
			elif(var=="s"):
				self.deplacement(1,0)
			elif(var=="se"):
				self.deplacement(1,1)
			elif(var=="so"):
				self.deplacement(1,-1)
			elif(var=="ne"):
				self.deplacement(-1,1)
			elif(var=="no"):
				self.deplacement(-1,-1)
	def afficher_grille(self):
		self.grille.set_element(self.x,self.y,'##')
		for i in range(self.grille.taille):
			affichage=[]
			for j in range(self.grille.taille):
				affichage+=[" "*(4-len(str(self.grille.Grid[i][j]))-2*int(i==self.x and j==self.y)),self.grille.Grid[i][j]]
			print(affichage)
		self.grille.set_element(self.x,self.y,None)
	def partie_terminee(self):
		for dx in range(-1,2):
			for dy in range(-1,2):
				if((self.x+dx,self.y+dy)in self.grille and self.grille.Grid[self.x+dx][self.y+dy]!=None):
					return(False)
		return(True)	
	def affichage_des_scores(self):
		for joueur in self.liste_joueurs:
			print(joueur.nom+" : "+ str(joueur.score))
g=Game(5,["jean","pierre"])
while(not g.partie_terminee()):
	g.affichage_des_scores()
	g.afficher_grille()
	g.jouer_un_coup()
print("la partie est terminée! ")
g.affichage_des_scores()
if g.liste_joueurs[0].score>g.liste_joueurs[1].score:
	print(g.liste_joueurs[0].nom+" a gagné")
elif g.liste_joueurs[0].score==g.liste_joueurs[1].score:
	print("match nul")
else:
	print(g.liste_joueurs[1].nom+" a gagné")



