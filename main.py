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

def main():
    # Demande à l'utilisateur quel exercice exécuter
    choix = input("Entrez le numéro de l'exercice à exécuter : ")
    if choix == "1":
        exercice1()
    if choix == "2":
        exercice2()
    if choix == "3":
        exercice3()
    else:
        print("Exercice non reconnu.")
        
if __name__ == "__main__":
    main()