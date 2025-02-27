
import random
import colorama
from colorama import Fore, Style


colorama.init(autoreset=True)


def dessinPendu(nb):
    tab=[
    """
       +-------+
       |
       |
       |
       |
       |
    ==============
    """,
    """
       +-------+
       |       |
       |       O
       |
       |
       |
    ==============
    """,
    """
       +-------+
       |       |
       |       O
       |       |
       |
       |
    ==============
    """,
    """
       +-------+
       |       |
       |       O
       |      -|
       |
       |
    ==============
    """,
    """
       +-------+
       |       |
       |       O
       |      -|-
       |
       |
    ==============
    """,
    """
       +-------+
       |       |
       |       O
       |      -|-
       |      |
       |
    ==============
    """,
    """
       +-------+
       |       |
       |       O
       |      -|-
       |      | |
       |
    ==============
    """
    ]
    return tab[min(nb, len(tab) - 1)]


def charger_mots(fichier):
    try:
        with open(fichier, "r", encoding="utf-8") as f:
            mots = [ligne.strip().upper() for ligne in f.readlines() if ligne.strip()]
        return mots
    except FileNotFoundError:
        print("❌ Fichier de mots introuvable ! Vérifiez son emplacement.")



def jouer_pendu():
    
    fichier_mots = "dico.txt"
    mots = charger_mots(fichier_mots)

    
    mot_a_deviner = random.choice(mots)
    mot_cache = ["_"] * len(mot_a_deviner)
    lettres_trouvees = set()
    lettres_ratees = set()
    max_erreurs = 6
    nb_erreurs = 0

    while nb_erreurs < max_erreurs and "_" in mot_cache:
        print("\nMot à deviner :", " ".join(mot_cache))
        print(dessinPendu(nb_erreurs))
        print("Lettres déjà essayées :", " ".join(sorted(lettres_trouvees | lettres_ratees)))

        lettre = input(Fore.MAGENTA + "Proposez une lettre : ").upper().strip()

        if not lettre.isalpha() or len(lettre) != 1:
            print(Fore.RED + "❌ Erreur : Entrez UNE seule lettre valide (A-Z).")
            continue

        if lettre in lettres_trouvees or lettre in lettres_ratees:
            print(Fore.YELLOW + "⚠️ Vous avez déjà essayé cette lettre.")
            continue

        if lettre in mot_a_deviner:
            lettres_trouvees.add(lettre)
            for i, char in enumerate(mot_a_deviner):
                if char == lettre:
                    mot_cache[i] = lettre
        else:
            lettres_ratees.add(lettre)
            nb_erreurs += 1

    
    if "_" not in mot_cache:
        print(Fore.BLUE+ "\n🎉 Félicitations ! Le mot était :", Fore.YELLOW + mot_a_deviner)
    else:
        print(Fore.RED + "\n😞 Dommage ! Vous avez perdu. Le mot était :")
        print(dessinPendu(nb_erreurs))

   
    rejouer = input(Fore.GREEN + "\nVoulez-vous rejouer ? (O/N) : ").strip().upper()
    if rejouer == "O":
        jouer_pendu()  


jouer_pendu()