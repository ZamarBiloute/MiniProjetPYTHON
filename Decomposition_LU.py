
# Importation de la bibliothèque numpy pour la manipulation des matrices
import numpy as np

TAILLE_TABLEAU = 150


def Construction_Matrices_L_U(MatriceA, Matriceb, Taille):
    
    global MatriceL, MatriceU

    #Définition  des matrices L et U
    MatriceL = np.zeros((Taille, Taille))
    MatriceU = np.zeros((Taille, Taille))

    #Initialisation de la matrice L et U
    for Ligne in range(0,Taille,1):
        MatriceL[Ligne][Ligne] = 1
        for Colonne in range(0,Taille,1):
                MatriceU[Ligne][Colonne] = MatriceA[Ligne][Colonne]

    #Construction de la matrice U et L
    for Indice in range(0,Taille,1):
        pivot = MatriceU[Indice][Indice]
        if pivot == 0:
            print("Le pivot est nul, la décomposition LU n'est pas possible !")
        for Ligne in range(Indice+1,Taille,1):
            coeffcient = MatriceU[Ligne][Indice]/pivot
            for Colonne in range(0,Taille,1):
                MatriceU[Ligne][Colonne] = MatriceU[Ligne][Colonne] - (coeffcient*MatriceU[Indice][Colonne])
            MatriceL[Ligne][Indice] = coeffcient
    
    for i in range(0,Taille,1):
        for j in range(0,Taille,1):
            print("U[" + str(i + 1) + "][" + str(j + 1) + "] = " + str(MatriceU[i][j]))
    for i in range(0,Taille,1):
        for j in range(0,Taille,1):
            print("L[" + str(i + 1) + "][" + str(j + 1) + "] = " + str(MatriceL[i][j]))

    return MatriceL, MatriceU

def Construction_Matrice_y(MatriceL, Matriceb, Taille):
    global Matricey
    Colonne = 0
    #initialisation de la matrice y
    Matricey = [0]*Taille

    #Construction de la matrice y
    Matricey[0] = Matriceb[0]/MatriceL[0][0]
    for Ligne in range(1,Taille,1):
        Matricey[Ligne] = Matriceb[Ligne]
        for Colonne in range(0,Ligne,1):
            Matricey[Ligne] = Matricey[Ligne] - (MatriceL[Ligne][Colonne]*Matricey[Colonne])
        Matricey[Ligne] = Matricey[Ligne]/MatriceL[Ligne][Ligne]
    
    for i in range(0,Taille,1):
        print("Y[" + str(i + 1) + "] = " + str(Matricey[i]))

    return Matricey
    
def Construction_Matrice_x(MatriceU, Matricey, Taille):
    global Matricex
    #initialisation de la matrice x
    Matricex = [0]*Taille

    #Construction de la matrice x
    Matricex[Taille] = (Matricey[Taille])/(MatriceU[Taille][Taille])
    for Ligne in range(Taille-1,0,-1):
        Matricex[Ligne] = Matricey[Ligne]
        for Colonne in range(Taille,Ligne,-1):
            Matricex[Ligne] = Matricex[Ligne] - MatriceU[Ligne][Colonne]*Matricex[Colonne]
        Matricex[Ligne] = Matricex[Ligne]/MatriceU[Ligne][Ligne]

    
    for i in range(0,Taille,1):
        print("X[" + str(i + 1) + "] = " + str(Matricex[i]))

    return Matricex

def main():
    # saisie de la taille des matrice de ce code
    Taille = int(input("Entrer la taille de la matrice A : "))
    
    while Taille > TAILLE_TABLEAU or Taille <= 0 or Taille != int(Taille):
        print("La taille doit être un entier positif inférieur ou égal à " + str(TAILLE_TABLEAU) + " !")
        Taille = int(input("Entrer la taille de la matrice A : "))
    
    # initialisation des matrices A et b
    MatriceA = np.zeros((Taille, Taille))
    Matriceb = [0]*Taille
    
    #Saisie des éléments de la matrice A et b
    for Ligne in range(0,Taille,1):
        for Colonne in range(0,Taille,1):
            MatriceA[Ligne][Colonne] = float(input("Entrer l'element A[" + str(Ligne + 1) +"][" + str(Colonne + 1) + "] : "))
        Matriceb[Ligne] = float(input("Entrer l'element B[" + str(Ligne + 1) + "] : "))

    for i in range(0,Taille,1):
        for j in range(0,Taille,1):
            print("A[" + str(i + 1) + "][" + str(j + 1) + "] = " + str(MatriceA[i][j]))
    for i in range(0,Taille,1):
            print("b[" + str(i + 1) + "] = " + str(Matriceb[i]))

    Construction_Matrices_L_U(MatriceA, Matriceb, Taille)
    Construction_Matrice_y(MatriceL, Matriceb, Taille)
    Construction_Matrice_x(MatriceU, Matricey, Taille)
    """print("Voici les solutions du système linéaire : ")
    for i in range(0,Taille,1):
        print("x[" + str(i + 1) + "] = " + str(Matricex[i]))
    """
if __name__ == "__main__":
    main()
