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

def exercice15():
    try:
        côté = int(input("entrez la longueur d'un côté d'une figure : "))
        print(f"le périmètre de cette figure est de {côté * 4}cm, m, etc...")
    except ValueError:
        print("ce n'est visiblement pas d'une longueur suffisante")

def exercice16():
    try:
        côté1 = int(input("entrez la longueur d'un côté : "))
        côté2 = int(input("entrez une seconde longueur : "))
        print(f"l'aire de cette figure est de {côté1*côté2}cm, m, etc...")
    except ValueError:
        print("il n'en a pas l'air mais ce n'est pas une longueur")

def exercice17():
    try:
        euro = int(input("valeur à convertir : "))
        print(f"le taux de convertion est fixé à 1€ = 1.1$\n{euro}€ = {euro * 1.1}$")
    except ValueError:
        print("No argent?")

def exercice18():
    try:
        minute = int(input("entrez autant de minute que souhaité : "))
        print(f"ça fait {minute*60} secondes")
    except ValueError:
        print("tic tac")

def exercice19():
    try:
        HT = int(input("entrez un prix hors-taxe : "))
        print(f"le prix est de {HT*1.2}€ TTC")
    except ValueError:
        print("eh oui faut raquer")

def exercice20():
    try:
        âge = int(input("quel est ton âge : "))
        nom = input("quel est ton nom : ")
        print(f"Tu t'appelles donc {nom} et tu as {âge}ans")
    except ValueError:
        print("alien")

def exercice21():
    try:
        number = int(input("donne-moi un chiffre à analyser : "))
        if number > 0:
            print("positif")
        if number < 0:
            print("négatif")
        if number == 0:
            print("nul")
    except ValueError:
        print("pov : tu sais pas lire")

def exercice22():
    try:
        age = int(input("donne-moi ton âge : "))
        if age < 18:
            print("mineur")
        else:
            print("majeur")
    except ValueError:
        print("reptilien")

def exercice23():
    try:
        note = int(input("t'as eu quelle note : "))
        if note >= 10:
            print("t'es passé")
        else:
            print("rip")
    except ValueError:
        print("pronote existe")

def exercice24():
    try:
        chiffre1 = int(input("entrez un chiffre à vérifier : "))
        chiffre2 = int(input("entrez un autre chiffre à vérifier : "))
        if chiffre1 > chiffre2:
            print(f"{chiffre1} est supérieur à {chiffre2}")
        elif chiffre2 > chiffre1:
            print(f"{chiffre2} est supérieur à {chiffre1}")
        else:
            print("ces chiffres sont égaux")
    except ValueError:
        print("un chiffre, tu sais ce que c'est?")

def exercice25():
    try:
        chiffre1 = int(input("entrez un chiffre à classer : "))
        chiffre2 = int(input("entrez un autre chiffre à classer : "))
        if chiffre1 < chiffre2:
            print("vous avez entrez ces chiffres dans l'ordre croissant")
        elif chiffre1 > chiffre2:
            print("vous n'avez pas entré ces chiffres dans l'ordre croissant")
        else:
            print("ces chiffres sont égaux")
    except ValueError:
        print("débrouille-toi pour classer tes hiéroglyphes")

def exercice26():
    try:
        chiffre = int(input("entrez un chiffre à vérifier : "))
        if chiffre % 5 == 0:
            print(f"{chiffre} est divisible par 5")
        else:
            print(f"{chiffre} n'est pas divisible par 5")
    except ValueError:
        print("ce pani n'est pas divisible tout court")

def exercice27():
    try:
        age1 = int(input("entrez un chiffre à classer : "))
        if age1 < 12:
            print("C'est un enfant")
        elif age1 > 17:
            print("C'est un adulte")
        else:
            print("C'est un adolescent")
    except ValueError:
        print("range ta chambre toi-même")

def exercice28():
    try:
        température = int(input("entrez une température à vérifier : "))
        if température < 0:
            print("C'est de la glace")
        elif température >= 100:
            print("C'est de la vapeur")
        else:
            print("C'est de l'eau")
    except ValueError:
        print("c'est de l'uranium")

def exercice29():
    try:
        note = int(input("entrez une note à évaluer : "))
        if note < 10:
            print("recalé")
        elif 10 <= note <14:
            print("passable")
        elif 14 <= note < 16:
            print("bien")
        else:
            print("très bien")
    except ValueError:
        print("F-")

def exercice30():
    compteur = 1
    try:
        chiffre = int(input("entrez un chiffre pour définir la fin de la liste : "))
        for compteur in range(compteur, chiffre + 1):
            print(compteur)
    except ValueError:
        print("il y a une fin à tout")

def exercice31():
    try:
        chiffre = int(input("entrez un chiffre pour définir le début de la liste : "))
        for compteur in range(chiffre, -1, -1):
            print(compteur)
    except ValueError:
        print("Il y a un début à presque tout")

def exercice32():
    compteur = 0
    total = 0
    try:
        chiffre = int(input("entrez un chiffre pour calculer la liste : "))
        for compteur in range(compteur, chiffre + 1):
            total = total + compteur
        print(total)
    except ValueError:
        print("cette liste ne sera pas listable")

def exercice33():
    compteur = 1
    try:
        chiffre = int(input("entrez un chiffre pour calculer la liste : "))
        for compteur in range(compteur, 11):
            total = compteur * chiffre
            print(f"{chiffre} x {compteur} = {total}")
    except ValueError:
        print("a pu ikea")

def exercice34():
    compteur = 0
    try:
        chiffre = int(input("entrez un chiffre pour calculer la liste : "))
        for compteur in range(compteur, chiffre + 1):
            if compteur % 2 == 0:
                print(compteur)
    except ValueError:
        print("des lettres paires???")

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
    if choix == "15":
        exercice15()
    if choix == "16":
        exercice16()
    if choix == "17":
        exercice17()
    if choix == "18":
        exercice18()
    if choix == "19":
        exercice19()
    if choix == "20":
        exercice20()
    if choix == "21":
        exercice21()
    if choix == "22":
        exercice22()
    if choix == "23":
        exercice23()
    if choix == "24":
        exercice24()
    if choix == "25":
        exercice25()
    if choix == "26":
        exercice26()
    if choix == "27":
        exercice27()
    if choix == "28":
        exercice28()
    if choix == "29":
        exercice29()
    if choix == "30":
        exercice30()
    if choix == "31":
        exercice31()
    if choix == "32":
        exercice32()
    if choix == "33":
        exercice33()
    if choix == "34":
        exercice34()
    else:
        print("Exercice non reconnu.")
        
if __name__ == "__main__":
    main()