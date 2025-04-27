import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
# from features import *
from solvers.deuxdcarte.features import *

data = {}  # dictionnaire contenant les types d'évolution de la température à l'interface, et les paramètres associés
# Initialisation du dictionnaire : un dictionnaire par interface
data["g"] = {}
data["d"] = {}
data["h"] = {}
data["b"] = {}
# Initialisation gauche
data["g"]["type"] = 2
data["g"]["k"] = 0
data["g"]["T0"] = 0
data["g"]["T1"] = 100
data["g"]["Tmin"] = 20
data["g"]["Tmax"] = 200
# Initialisation droite
data["d"]["type"] = 0
data["d"]["k"] = 0
data["d"]["T0"] = 0
data["d"]["T1"] = 100
data["d"]["Tmin"] = 20
data["d"]["Tmax"] = 200
# Initialisation haut
data["h"]["type"] = 0
data["h"]["k"] = 0
data["h"]["T0"] = 0
data["h"]["T1"] = 0
data["h"]["Tmin"] = 20
data["h"]["Tmax"] = 200
# Initialisation bas
data["b"]["type"] = 0
data["b"]["k"] = 0
data["b"]["T0"] = 0
data["b"]["T1"] = 0
data["b"]["Tmin"] = 20
data["b"]["Tmax"] = 200
# Initialisation des paramètres du matériau/ de l'objet
data["K"] = 5e-4  # diffusivité thermique
data["rho"] = 1000
data["c"] = 1000
data["Lx"] = 1  # longueur (horizontale)
data["Ly"] = 1  # verticale
data["Tini"] = 0
# temps de résolution
data["time"] = 100

# Paramètres fixés ou liés:

# Pas
dx = 0.02
dy = 0.02
dt = 0.05
# découpages spatiaux
Nx = int(data["Lx"]/dx)
Ny = int(data["Ly"]/dy)
# découpage temporel
nt = int(data["time"]/dt)
# Initialisation du terme source
data["S"] = np.zeros([int(data["Ly"]/dy), int(data["Lx"]/dx)])
data["sources"] = []
# Paramétrage de la fenêtre de chaleur
data["Tmin"] = 0
data["Tmax"] = 100


def air_20d():
    data["K"] = 20e-6
    data["rho"] = 0.0013e3
    data["c"] = 1.01e3


def aluminium():
    data["K"] = 98.8e-6
    data["rho"] = 2.7e3
    data["c"] = 0.888e3


def plomb():
    data["K"] = 23.9e-6
    data["rho"] = 11.34e3
    data["c"] = 0.129e3


def bronze():
    data["K"] = 18.7e-6
    data["rho"] = 8.8e3
    data["c"] = 0.377e3


def animcarte2D():
    def condition_initiales():
        T = init_temperature(data, Nx, Ny, nt)
        return T

    # Ajoute les sources de chaleur
    def ajoute_source(x0, y0, r, Pv):
        source_rond(x0, y0, r, Nx, Ny, dx, dy, data, Pv)

    for i in range(len(data["sources"])):
        ajoute_source(data["sources"][i][0], data["sources"]
                      [i][1], data["sources"][i][2], data["sources"][i][3])

    # Permet de passer du portrait de température d'un instant t à un instant t+dt
    def resolution():
        T = condition_initiales()
        for t in range(1, nt):
            for i in range(1, Ny - 1):
                for j in range(1, Nx - 1):
                    T[t, i, j] = T[t-1, i, j] + data["S"][i, j]*dt + data["K"]*dt * \
                        ((T[t-1, i, j+1]-2*T[t-1, i, j]+T[t-1, i, j-1])/(dx**2) +
                         (T[t-1, i+1, j]-2*T[t-1, i, j]+T[t-1, i-1, j])/(dy**2))
        return T

    # Calcul de la température en tout point à tout instant
    T = resolution()

    # Création de la figure pour l'animation
    fig, ax = plt.subplots()
    vmin, vmax = 0, 100

    # Fonction d'animation
    def animate(t):
        ax.clear()
        plt.clf()
        plt.title(
            'Evolution de la température dans le plan\nTemps : {:.2f}'.format(10*t * dt))
        plt.xlabel('Echelle horizontale')
        plt.ylabel('Echelle verticale')
        instant = plt.imshow(
            T[10*t], cmap='viridis', interpolation='none', aspect='equal', vmin=vmin, vmax=vmax)
        instant.set_array(T[10*t])
        plt.colorbar()
        return [T]

    anim = FuncAnimation(fig, animate, frames=nt//10,
                         interval=1e-10, repeat=True)

    return fig, anim
