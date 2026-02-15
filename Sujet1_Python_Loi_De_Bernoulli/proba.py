# Loi de Bernoulli
# test unitaire dans fichier test Unitaire avec pour sorti vrai pour 1 ou 0
# functionalite lancer_piece return soit 1 soit 0
# request connexion avec connexion qui est verfifie avec si function lance piece = 1 reussi et echou si 0

# sujet: une pile lance 3 fois
import random
import statistics

#simulation en python de la loi de Bernoulli

def lancer_piece():# functionalite lancer piece
    #ici X est la variable aleatoire aussi l experience aleatoire
    x = 1 if random.random() < 0.5 else 0
    return x #issue ici soit 1 soit 0

repetition = 100
total_piles = 0
coReussi = 0
coEchoue = 0
Esperance_troi_lancer = []
Variance_troi_lancer = []

#ici on va relancer la pile 3*100 fois
for i in range(repetition):
    connexion = lancer_piece()
    if(connexion == 1):#co reussi
        coReussi += 1
        #resultat ici stock le resultat de obtenue soit PPP,PPF,PFF,FFF,FFP,FPP,FPF,PFP
        resultat = [lancer_piece() for j in range(3)]

        #esperance
        Esperance = statistics.mean(resultat)
        Esperance_troi_lancer.append(Esperance)
        #Variance
        Variance = Esperance*(1-Esperance)
        Variance_troi_lancer.append(Variance)

        total_piles += sum(resultat)

    else: #co echoue
        coEchoue += 1

t = 0
k = 0
#frequence total de pile obtenue diviser par le nombre total ou le pile a ete lancer
frequence = total_piles / (3*repetition)

#Affichage des resultat :

for i in Esperance_troi_lancer:
    t = t+1
    print("Esperance de 3 lancer de piece ",t,"fois = ",f"{i:.3f}")

for i in Variance_troi_lancer:
    k = k+1
    print("Variance de 3 lancer de piece ",k,"fois", f"{i:.3f}")

print("nombre total de connexion reussi ", coReussi)
print("nombre total de connexion echoue ", coEchoue)
print("nombre total de pile obtenue apres lancer pile 300fois", total_piles)
print("frequence ou pile est obtenue ",  f"{frequence: .3f}")
print("frequence ou face est obetnue ",  f"{1-frequence: .3f}")



#simulation en python de la loi de Bernoulli