# 1 mq M est inversible <-- pivot de Gauss
# 2 trouve M^-1 <-- pivot de Jordan

# valable matrice carrée <-- logique
import numpy as np

M = np.array([[5, 8, 1],
              [6, 7, 3],
              [2, 5, 9]])
I3 = np.array([[1, 0, 0],
               [0, 1, 0],
               [0, 0, 1]])
MI3 = np.array([[5, 8, 1, 1, 0, 0],
                [6, 7, 1, 0, 1, 0],
                [2, 5, 9, 0, 0, 1]])


def forward_elimination(M):
    nxn = len(M)  # forcement car n*n  n'existe que pour Mn(K)
    for k in range(diag - 1):  # itérate k fois
        for i in range(k + 1, len(M)):  # ligne   
            ratio = M[i][k] / M[k][k]
            for j in range(len(M[0])):  # colonne
                M[i][j] -= ratio * M[k][j]

    return M

#pour la beauté
def diag_1(M): #on veut que tous les mkk soient = 1
    M = forward_elimination(M)
    for k in range(len(M)):
        if M[k][k] != 1.:
            ratio = 1 / M[k][k]
            for i in range(k, len(M)):  # ligne
                for j in range(len(M[0])):  # colonne
                    M[i][j] *= ratio
    return M

  
def Jordan(M):
    M = diag_1(M)
    for k in range(len(M)):  # =3
        for i in range(k, len(M)):  # ligne
            for j in range(len(M[0])):  # colonne
                if (i < 3 and j < 3) and i!=j and M[i][j] != 0:
                        jArr = np.array([j, j])
                        iArr = np.arange(0, len(M))
                        zeroIndexArr = np.array(i)
                        new_iArr = np.setdiff1d(iArr, zeroIndexArr)

                        for c in range(len(jArr)):
                            mij = M[new_iArr[c]][jArr[c]]
                            if mij != 0:
                                ratioForLrow = -(M[i][j] / M[j][j])
                                M[i, :] = M[i, :] + ratioForLrow * M[j, :]
                                break
    return M
