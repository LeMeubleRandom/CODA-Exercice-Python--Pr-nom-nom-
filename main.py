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
        chiffre2sous = int(input("entrez un second chiffre à soustraire : "))
        print(f"le résultat est {chiffresous - chiffre2sous}")
    except ValueError:
        print("je suis incapable de soustraire tes trucs")

def exercice7():
    try:
        chiffreX = int(input("entrez un chiffre à multiplier : "))
        chiffre2X = int(input("entrez un second chiffre à multiplier : "))
        print(f"le résultat est {chiffreX * chiffre2X}")
    except ValueError:
        print("je suis incapable de mutiplier tes carabistouilles")

def exercice8():
    try:
        chiffrediv = int(input("entrez un chiffre à diviser : "))
        chiffre2div = int(input("entrez un second chiffre à diviser : "))
        if chiffre2div == 0:
            print("invalide")
        else:
            print(f"le résultat est {chiffrediv/chiffre2div}")
    except ValueError:
        print("je suis incapable de diviser tes poubelles")

def exercice9():
    try:
        chiffrecarré = int(input("entrez un chiffre pour avoir son carré : "))
        print (f"le résultat est {chiffrecarré*chiffrecarré}")
    except ValueError:
        print("je suis incapable d'avoir le carré de ton ovni")

def exercice10():
    try:
        double = int(input("entrez un chiffre à doubler : "))
        print (f"le résultat est {double*2}")
    except ValueError:
        print ("je suis incapable de doubler ta Trueno")

def exercice11():
    try:
        moitié = int(input("entrez un chiffre pour avoir sa moitié : "))
        print (f"le résultat est {moitié/2}")
    except ValueError:
        print ("je suis incapable d'avoir la moitié de ta triforce (y a 3 morceaux t'as capté)")

def exercice12():
    echo = input("choisissez un message à dupliquer : ")
    duplicated_message = echo * 5
    print(duplicated_message)

def exercice13():
    n = 0
    liste = []
    while n < 5:
        n = n + 1
        liste.append(n)
    print(liste)

def exercice14():
    compteur = 1
    for compteur in range(compteur, 6):
        résultat = compteur * 2
        print(f"2 x {compteur} = {résultat}")

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
    if choix == "7":
        exercice7()
    if choix == "8":
        exercice8()
    if choix == "9":
        exercice9()
    if choix == "10":
        exercice10()
    if choix == "11":
        exercice11()
    if choix == "12":
        exercice12()
    if choix == "13":
        exercice13()
    if choix == "14":
        exercice14()
    else:
        print("Exercice non reconnu.")
        
if __name__ == "__main__":
    main()