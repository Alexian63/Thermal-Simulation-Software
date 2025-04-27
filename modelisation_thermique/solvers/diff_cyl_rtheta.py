import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from solvers.parametres import *

parameters_2Drtheta = init_parameters_2Drtheta()


def visualise_2Drtheta():
    # prise en compte des parametres de simulation
    T0 = parameters_2Drtheta['T0']
    T1 = parameters_2Drtheta['T1']
    T2 = parameters_2Drtheta['T2']
    theta1 = int(parameters_2Drtheta['theta1'])
    theta2 = int(parameters_2Drtheta['theta2'])
    radius = int(parameters_2Drtheta['radius'])

    # Discrétisation temporelle
    dt = 0.1  # Pas temporel
    duree = 40  # Durée totale de simulation
    nt = int(duree / dt) + 1

    # Discrétisation spatiale
    nr = 50  # Nombre de points radiaux
    ntheta = 50  # Nombre de points axiaux

    dr = radius / (nr - 1)
    dtheta = 2*np.pi / (ntheta - 1)

    # Initialisation de la matrice de température
    # theta +4 pour assurer la continuité en theta=0/360
    T = np.zeros((nt, nr, ntheta + 4))
    T.fill(T0)

    # Conditions aux limites aux bord du cylindre
    T[:, -2:, theta1] = T1
    T[:, -2:, theta2] = T2

    # Coefficient de diffusion thermique
    alpha = 0.0001  # doit rester faible pour rester stable, on peut alors augmenter la vitesse de l'animation en diminuant l'interval dans funcanim et au augmentant dt

    # matrices pour multiplier un vecteur par r ou 1/r (dans le laplacien selon r)

    def matr(k):
        return np.diag([i+1 for i in range(k)])

    def invmatr(k):
        return np.linalg.inv(matr(k))

    # Boucle de résolution de l'équation de la chaleur
    for t in range(1, nt):
        lapr = np.zeros((nr, ntheta+4))  # laplacien selon r
        laptheta = np.zeros((nr, ntheta+4))  # laplacien selon theta
        for r in range(1, nr):
            derivethe = (T[t-1, r, 1:]-T[t-1, r, :-1]) / \
                dtheta  # de taille ntheta+3
            laptheta[r, 1:-1] = (derivethe[1:]-derivethe[:-1]
                                 )/(dtheta * (r*dr)**2)

        for theta in range(1, ntheta + 4):
            # le dr se simplifie en multipliant par i*dr
            # deriver = (T[t-1, 1:, theta]-T[t-1, :-1, theta])  # de taille nr-1
            rxderiver = matr(nr-1)@(T[t-1, 1:, theta]-T[t-1, :-1, theta])
            lapr[1:-1, theta] = (1/dr)**2 * invmatr(nr -
                                                    2)@(rxderiver[1:]-rxderiver[:-1])

        # on update la matrice en t
        # (le 1.3 permet de compenser le fait qu'on "rogne" les valeurs de T)
        T[t, :, :] = T[t-1, :, :] + alpha*(lapr + 1.3*laptheta)
        # ces 2 lignes permettent d'eviter des erreurs d'overflow ou des valeurs absurdes
        T[t, :, :] = (T[t, :, :]*100).astype(int) / 100
        T[t, :, :] = np.clip(T[t, :, :], 0, max(T0, T1, T2))

        # on assure la continuité en theta = 0/360 deg et en Rext
        T[t, :, 0:1] = T[t, :, -4:-3]
        T[t, :, -2:-1] = T[t, :, 2:3]
        T[t, -1, :] = T[t, -2, :]

        # terme source
        T[:, -2:, theta1] = T1
        T[:, -2:, theta2] = T2

        # print(T[t, :, :])
        print(f"avancement: {100*t/nt}%")

    # Création de la figure pour l'animation
    fig, ax = plt.subplots()
    # Création de la vue de coupe colorée en fonction de la température
    R, The = np.meshgrid(np.linspace(0, radius, nr),
                         np.linspace(0, 2*np.pi, ntheta))
    X = The * np.cos(2 * np.pi * R / (radius+dr))
    Y = The * np.sin(2 * np.pi * R / (radius+dr))

    # Fonction d'animation

    def update(frame):
        ax.clear()
        plt.title(
            'Evolution de la température dans le cylindre\nTemps : {:.2f}'.format(frame * dt))

        colors = plt.cm.plasma(T[frame, :, 2:-2])
        ax.pcolormesh(X, Y, colors, cmap='viridis')

    # Création de l'animation
    animation = FuncAnimation(fig, update, frames=nt, interval=1, blit=False)

    # Affichage de l'animation
    # plt.show()
    return fig, animation
