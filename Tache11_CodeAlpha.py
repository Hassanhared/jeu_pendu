import random
mots = ["python", "java", "html", "css"]
mot_secret = random.choice(mots)
lettres_trouves = []
lettre_unique = set(mot_secret)
tentative_restant = len(lettre_unique)
trouve = False
print("Bienvenue dans le jeu du pendu ! \n")
print(f"Deviner le mot de ({len(mot_secret)} lettre). vous avez {tentative_restant} tentative.\n")
affichage = ""
for lettre in mot_secret:
    affichage += "_"
while tentative_restant > 0 and not trouve:
    lettre = input("Proposez une lettre :\n").lower()
    if len(lettre) != 1 or not lettre.isalpha():
        print("veillez saisir une seule lettre valide\n")
        continue
    if lettre in lettres_trouves:
        print("vous avez déja proposé cette lettre\n")
        tentative_restant -= 1
        print(f" il vous reste {tentative_restant} tentative")
        continue
    lettres_trouves.append(lettre)
    if lettre in mot_secret:
        print(f"bien joué cette lettre {lettre} est bien dans le mot \n")
        tentative_restant -= 1
        print(f" il vous reste {tentative_restant} tentative")
    else:
        tentative_restant -= 1
        print(f"Mauvaise reponse, il vous reste {tentative_restant} tentative")
    affichage = ""
    for l in mot_secret:
        if l in lettres_trouves:
            affichage += l + ""
        else:
            affichage += "_"
    print(affichage.strip())
    if "_" not in affichage:
        trouve = True
if trouve:
    print(f" BRAVO !! vous avez trouvé le mot {mot_secret}\n")
else:
    print(f"vous avez perdu, le mot était {mot_secret}\n")
