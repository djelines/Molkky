#Fonctions
def jeu() -> int:
    """
    rôle : Fonction principale qui permet de retourner le score du jeu du Mölkky
    entrée : aucun paramètre
    précondition : initialiser le score de départ
                    demander le nombre de quilles tombées (compris entre 0 et 12)
    sortie : le résultat du jeu en int
    """
    score_actuel = 0

    nombres_entiers = int(input("Combien de quilles sont tombées ?"))
    while nombres_entiers<0 or nombres_entiers>12:
        print( "C'est impossible. N'essayez pas de corrompre le programme !")
        nombres_entiers = int(input("Choisissez un nombre compris uniquement entre 0 et 12: "))
    print(nombres_entiers)
    n = new_score()

    return(n)


def new_score()->int:
    """
    rôle : Fonction secondaire qui permet de calculer le résultat de score actuel + le nombre de point
    entrée : aucun paramètre
    précondition : demander le score actuel (il ne doit pas dépasser 50)
                    demander le nombre de point (il ne doit pas dépasser 12)
    sortie : Une jolie phrase qui renvoie le score à la fonction principale
    """
    win = False

    score_actuel=int(input("Quel est votre score actuel ? "))

    if score_actuel >= 50 or score_actuel <0:
        print("Minute papillon, c'est impossible d'avoir un score supérieur à 50")
        while score_actuel >= 50 or score_actuel<0:
            print( "C'est impossible.")
            score_actuel = int(input("Quel est votre vrai score actuelle ? "))

    while win == False:

        nombres_points=int(input("Combien de points avez-vous gagné ? "))

        if nombres_points >12 or nombres_points<0:
            print("Minute papillon, c'est impossible d'avoir un score supérieur à 12")
            while nombres_points > 12 or nombres_points<0:
                print( "C'est impossible.")
                nombres_points = int(input("Combien de points avez-vous vraiment gagné ? "))

        new_score= score_actuel + nombres_points


        if new_score == 50:
            win = True
            print("Vous êtes à",new_score,"points ! Bravo, vous avez gagné !")

        elif new_score >= 50:
            win = False
            print("Vous êtes à", new_score, ". Vous avez dépassé les 50 points !")
            score_actuel = 25
            print ("Zut vous êtes redescendu à", score_actuel, "points !")
        else:
            win = False
            score_actuel = new_score
            print("Vous avez", new_score, "points")

#Main
jeu()