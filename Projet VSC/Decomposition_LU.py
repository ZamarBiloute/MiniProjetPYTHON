
# Importation de la bibliothèque numpy pour la manipulation des matrices
import numpy as np

def Construction_Matrices_L_U(MatriceA, Matriceb, Taille):
    
    global MatriceL, MatriceU

    #Définition  des matrices L et U
    # MatriceL = np.zeros((Taille, Taille))
    # MatriceU = np.zeros((Taille, Taille))
    MatriceL = []
    MatriceU = []
    for Ligne in range(0,Taille,1):
        MatriceL.append([0]*Taille)
        MatriceU.append([0]*Taille)

    #Initialisation de la matrice L et U
    for Ligne in range(0,Taille,1):
        MatriceL[Ligne][Ligne] = 1
        for Colonne in range(0,Taille,1):
                MatriceU[Ligne][Colonne] = MatriceA[Ligne][Colonne]

    #Construction de la matrice U et L
    for Indice in range(0,Taille,1):
        pivot = MatriceU[Indice][Indice]
        if pivot == 0:
            print("Le pivot est nul en U[" + str(Indice + 1) + "][" + str(Indice + 1) + "], la décomposition LU n'est pas possible !")
            return False
        for Ligne in range(Indice+1,Taille,1):
            coeffcient = MatriceU[Ligne][Indice]/pivot
            for Colonne in range(0,Taille,1):
                MatriceU[Ligne][Colonne] = MatriceU[Ligne][Colonne] - (coeffcient*MatriceU[Indice][Colonne])
            MatriceL[Ligne][Indice] = coeffcient
    
    for Ligne in range(0,Taille,1):
        for Colonne in range(0,Taille,1):
            print("U[" + str(Ligne + 1) + "][" + str(Colonne + 1) + "] = " + str(MatriceU[Ligne][Colonne]), end=" ")
        print("\r")
    for Ligne in range(0,Taille,1):
        for Colonne in range(0,Taille,1):
            print("L[" + str(Ligne + 1) + "][" + str(Colonne + 1) + "] = " + str(MatriceL[Ligne][Colonne]), end=" ")
        print("\r")
 
    return True

def Construction_Matrice_y(MatriceL, Matriceb, Taille):
    global Matricey
    #initialisation de la matrice y
    Matricey = [0]*Taille

    #Construction de la matrice y
    Matricey[0] = Matriceb[0]/MatriceL[0][0]
    for Ligne in range(1,Taille,1):
        Matricey[Ligne] = Matriceb[Ligne]
        for Colonne in range(0,Ligne,1):
            Matricey[Ligne] = Matricey[Ligne] - (MatriceL[Ligne][Colonne]*Matricey[Colonne])
        if MatriceL[Ligne][Ligne] == 0:
            print("Erreur : Matrice de L nul détécté a MatriceL[" + str(Ligne + 1) + "][" + str(Ligne + 1) + "]")
            return False
        Matricey[Ligne] = Matricey[Ligne]/MatriceL[Ligne][Ligne]
    
    for Ligne in range(0,Taille,1):
        print("Y[" + str(Ligne + 1) + "] = " + str(Matricey[Ligne]))

    return True 
    
def Construction_Matrice_x(MatriceU, Matricey, Taille):
    global Matricex
    #initialisation de la matrice x
    Matricex = [0]*Taille

    #Construction de la matrice x
    Matricex[Taille-1] = (Matricey[Taille-1])/(MatriceU[Taille-1][Taille-1])
    for Ligne in range(Taille-1,0,-1):
        Matricex[Ligne] = Matricey[Ligne]
        for Colonne in range(Taille-1,Ligne,-1):
            Matricex[Ligne] = Matricex[Ligne] - MatriceU[Ligne][Colonne]*Matricex[Colonne]
        if MatriceU[Ligne][Ligne] == 0:
            print("Erreur : Matrice de U nul détécté a MatriceU[" + str(Ligne + 1) + "][" + str(Ligne + 1) + "]")
            return False 
        Matricex[Ligne] = Matricex[Ligne]/MatriceU[Ligne][Ligne]
    
    # for Ligne in range(0,Taille,1):
    #     print("X[" + str(Ligne + 1) + "] = " + str(Matricex[Ligne]))

    return True

def main():
    # saisie de la taille des matrice de ce code
    Taille = int(input("Entrer la taille de la matrice A : "))
    
    while  Taille <= 0 or Taille != int(Taille):
        print("La taille doit être superieur à 0 et un entier")
        Taille = int(input("Entrer la taille de la matrice A : "))
    
    # initialisation des matrices A et b
    MatriceA = []
    for Ligne in range(0,Taille,1):
        MatriceA.append([0]*Taille)
    Matriceb = [0]*Taille
    # MatriceA = np.zeros((Taille, Taille))
    # Matriceb = [0]*Taille
    
    #Saisie des éléments de la matrice A et b
    for Ligne in range(0,Taille,1):
        for Colonne in range(0,Taille,1):
            MatriceA[Ligne][Colonne] = float(input("Entrer l'element A[" + str(Ligne + 1) +"][" + str(Colonne + 1) + "] : "))
        Matriceb[Ligne] = float(input("Entrer l'element B[" + str(Ligne + 1) + "] : "))

    # for i in range(0,Taille,1):
    #     for j in range(0,Taille,1):
    #         print("A[" + str(i + 1) + "][" + str(j + 1) + "] = " + str(MatriceA[i][j]))
    # for i in range(0,Taille,1):
    #         print("b[" + str(i + 1) + "] = " + str(Matriceb[i]))

    if(Construction_Matrices_L_U(MatriceA, Matriceb, Taille) == False):
        print ("Erreur lors de la construction des matrices L et U !")
        return 
    
    if(Construction_Matrice_y(MatriceL, Matriceb, Taille) == False):
        print ("Erreur lors de la construction de la matrice y !")
        return
    
    if(Construction_Matrice_x(MatriceU, Matricey, Taille) == False):
        print ("Erreur lors de la construction de la matrice x !")
        return
    
    print("Voici les solutions du système linéaire : ")
    for Ligne in range(0,Taille,1):
        print("X[" + str(Ligne + 1) + "] = " + str(Matricex[Ligne]))
    
if __name__ == "__main__":
    main()
