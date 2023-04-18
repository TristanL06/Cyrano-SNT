"""
DM navette autonome
Tristan LARGUIER, cours cyrano
"""

import matplotlib.pyplot as plt

# Exercice 1

freq = [24, 12, 16, 18, 32, 26, 23, 45, 31, 54, 50, 53, 53, 64, 36, 46, 60, 72, 74, 68, 68, 75, 59, 76, 63, 66, 95, 68, 64, 67, 75, 80, 100, 100, 95, 82, 88, 103, 93, 107, 103, 125, 121, 124, 116, 114, 136, 107, 134, 108, 120, 121, 133, 135, 117, 143, 133, 147, 147, 136, 151, 158, 152, 144, 169, 149, 149, 141, 164, 171, 147, 182, 158, 157, 188, 163, 172, 162, 165, 177, 165, 186, 197, 180, 191, 207, 175, 179, 205, 201, 181, 181, 186, 205, 212, 189, 216, 224, 204, 225, 205, 212, 223, 211, 212, 203, 234, 238, 225, 212, 227, 233, 235, 232, 222, 231, 249, 247, 235, 225, 222, 240, 224, 249, 252, 232, 244, 244, 235, 262, 256, 260, 262, 241, 243, 262, 251, 265, 265, 266, 238, 240, 256, 240, 247, 269, 254, 254, 264, 244, 253, 278, 265, 279, 268, 263, 261, 257, 276, 273, 275, 274, 252, 258, 267, 277, 284, 286, 276, 277, 265, 273, 277, 255, 259, 275, 266, 262, 272, 269, 287, 283, 272, 272, 266, 280, 286, 267, 280, 266, 266, 270, 259, 283, 264, 284, 257, 267, 284, 270, 254, 252, 282, 269, 268, 258, 265, 283, 283, 278, 270, 253, 273, 253, 248, 280, 273, 265, 254, 257, 242, 262, 263, 254, 263, 266, 266, 260, 271, 269, 245, 253, 242, 251, 249, 263, 242, 241, 238, 258, 258, 252, 251, 224, 236, 254, 251, 250, 244, 237, 216, 218, 216, 221, 219, 240, 211, 213, 239, 207, 212, 212, 205, 208, 197, 228, 226, 217, 198, 204, 212, 207, 213, 210, 205, 191, 187, 184, 181, 205, 188, 195, 172, 193, 165, 177, 172, 182, 192, 174, 175, 185, 163, 165, 150, 149, 151, 168, 163, 172, 161, 163, 137, 148, 134, 132, 131, 144, 153, 128, 118, 135, 150, 134, 119, 116, 128, 116, 123, 127, 102, 128, 122, 104, 101, 101, 101, 103, 87, 81, 83, 95, 87, 96, 101, 71, 97, 82, 85, 80, 83, 60, 76, 67, 55, 48, 65, 75, 62, 63, 42, 49, 44, 40, 44, 55, 53, 25, 51, 18, 50, 17, 19, 27, 13]


def maxi(L):
    M = L[0]
    for e in L:
        if "COMPLÉTER":
            "COMPLÉTER"
    return M

#print(maxi(freq))

def mini(L):
    "à vous de jouer"
    return

#print(mini(freq))

def moyenne(L):
    "à vous de jouer"
    return

#print(moyenne(freq))

def plus_de_50(L):
    "à vous de jouer"
    return

#print(plus_de_50(freq))


## Exercice 2

def trace(L):
    x, y = 0, 0
    sft = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    ori = 0
    Lx = [0]
    Ly = [0]
    for ordre in L:
        if ordre == "A":
            x += sft[ori][0]
            y += sft[ori][1]
            Lx.append(x)
            Ly.append(y)
        if ordre == "D":
            ori = (ori + 1)%4
        if ordre == "G":
            ori = (ori - 1)%4
    plt.plot(Lx, Ly)
    return plt.show()

C1 = ['A', 'A', 'D', 'A', 'A', 'A', 'G', 'A', 'D', 'A', 'D', 'A', 'A', 'D', 'A', 'G', 'A', 'D', 'A', 'D', 'A', 'G', 'A', 'G', 'A', 'D', 'A']
C2 = ['A', 'A', 'D', 'A', 'A', 'A', 'A', 'D', 'A', 'A', 'A', 'D', 'A', 'G', 'A', 'D', 'A', 'D', 'A', 'G', 'A', 'G', 'A', 'D', 'A']
C3 = ['A', 'A', 'D', 'A', 'A', 'A', 'A', 'G', 'A', 'D', 'D', 'A', 'A', 'D', 'A', 'G', 'A', 'D', 'A', 'D', 'A', 'G', 'A', 'G', 'A', 'D', 'A']

trace(C1)
trace(C2)
trace(C3)

def distance(L, d):
    "à vous de jouer"
    return

#print(distance(C1, 100))
#print(distance(C2, 100))
#print(distance(C3, 100))


def orientation(L):
    "à vous de jouer"
    return True

#print(orientation(C1))
#print(orientation(C2))
#print(orientation(C3))


def demi_tour(L):
    "à vous de jouer"
    return False

#print(demi_tour(C1))
#print(demi_tour(C2))
#print(demi_tour(C3))

def est_valide(L):
    if demi_tour(L):
        return "COMPLÉTER"
    if not orientation(L):
        return "COMPLÉTER"
    
    x, y = 0, 0 #on initialise la position de départ
    sft = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    ori = 0 # on initialise l'orientation à 0
    for ordre in L:
        if ordre == "COMPLÉTER":
            x += sft[ori]["COMPLÉTER"]
            y += sft[ori]["COMPLÉTER"]
        if ordre == "COMPLÉTER":
            ori = (ori + 1)%4
        if ordre == "COMPLÉTER":
            ori = (ori - 1)%4
    return "COMPLÉTER"

#print(est_valide(C1))
