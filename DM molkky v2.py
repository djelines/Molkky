# Créé par chari, le 02/11/2022 en Python 3.7
def new_score(score_score, nbr_points):
    new_score = score_score + nbr_points

    if new_score> 50:
        new_score=25
    elif new_score==50:
        print("Bravo")

    return new_score

def jeu():
    score_actuel = 0
    while score_actuel != 50:
        nbr_points = int(input("Donnez le nombre de points obtenus"))
        while nbr_points<0 or nbr_points>12:
            nbr_points = int(input("encore"))

        score_actuel = new_score(score_actuel,nbr_points)
        print("nouveau score :", score_actuel)

    print('GG')

jeu()