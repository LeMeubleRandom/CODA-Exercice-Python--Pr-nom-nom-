# Exemple avec un seul exercice
# Exercice 1 clear, 
def exercice1():
    print("Exercice 1 : Bonjour le monde !")
    print("Hello World !")

def exercice2():
    prenom = input ("Entrez votre prénom : ")
    print(f"bonjour {prenom}!")

def exercice3():
    print("Première ligne\nDeuxième ligne\nTroisième ligne")

def exercice4():
    try:
        année = int(input ("entrez votre année de naissance : "))
        if année > 2025:
            print("t'es trop dans le turfu mais écris une date valide stp")
        else:
            print(f"vous avez {2025 - année} ans")
    except ValueError:
        print("réessayez avec une date valide")

def exercice5():
    try:
        chiffreadd = int(input("entrez un chiffre à additionner : "))
        chiffre2add = int(input("entrez un second chiffre à additionner : "))
        print(f"le résultat est {chiffreadd + chiffre2add}")
    except ValueError:
        print("je suis incapable d'additionner tes machins")

def exercice6():
    try:
        chiffresous = int(input("entrez un chiffre à soustraire : "))
        chiffre2sous = int(input("entrez un chiffre à soustraire : "))
        print(f"le résultat est {chiffresous - chiffre2sous}")
    except ValueError:
        print("je suis incapable de soustraire tes trucs")



def main():
    # Demande à l'utilisateur quel exercice exécuter
    choix = input("Entrez le numéro de l'exercice à exécuter : ")
    if choix == "1":
        exercice1()
    if choix == "2":
        exercice2()
    if choix == "3":
        exercice3()
    if choix == "4":
        exercice4()
    if choix == "5":
        exercice5()
    if choix == "6":
        exercice6()
    else:
        print("Exercice non reconnu.")
        
if __name__ == "__main__":
    main()