import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.integrate import odeint
from solvers.parametres import *

parameters_1Dcyl = init_parameters_1Dcyl()


def visualise_1Dcyl():
    # parametres de simulations
    R1 = float(parameters_1Dcyl['R1'])
    R2 = float(parameters_1Dcyl['R2'])
    R3 = float(parameters_1Dcyl['R3'])
    K1 = float(parameters_1Dcyl['K1'])
    K2 = float(parameters_1Dcyl['K2'])
    K3 = float(parameters_1Dcyl['K3'])
    materiaux = [(K1, R1), (K2, R2), (K3, R3)]

    # parametres discretisation
    L = materiaux[-1][1]
    Rint = 0.3
    nbPoints = 100
    dx = L/nbPoints

    extremites = np.linspace(0, L, nbPoints+1)
    points = (extremites[1:]+extremites[:-1])/2

    T = 5
    dt = 0.01
    temps = np.arange(0.0, T, dt)

    K = 0.5
    # fonction permettant de renvoyer l'indice de diffusivite du materiaux voulu en fonction de sa distance a zero

    def K(i, mate=materiaux):  # x = i*dx
        rayons = [item[1] for item in mate]
        if i*dx < rayons[0]:
            return mate[0][0]
        for j in range(len(mate)-1):
            if rayons[j] <= i*dx and i*dx < rayons[j+1]:
                return mate[j+1][0]
        return mate[-1][0]

    # donnees initiales si on veut en imposer dans le milieu
    # il faut alors modifier la ligne "U0[1:-1] = parameters_1Dcarte['T0']" par U0[1:-1] = donneeIni(points)
    def donneeIni(x):
        return 5*x**2

    U0 = np.zeros(nbPoints+2)
    U0[1:-1] = parameters_1Dcyl['T0']
    U0[0] = parameters_1Dcyl['T1']
    U0[-1] = parameters_1Dcyl['T2']

    # derivee seconde// espace

    def flux(U, t):
        retour = np.zeros_like(U)
        deriv_simples = (U[1:]-U[:-1])/dx
        rxderiv = np.array([K(i)*deriv_simples[i]*(i*dx+Rint)
                            for i in range(len(deriv_simples))])
        for i in range(nbPoints):
            retour[i+1] = ((rxderiv[i+1]-rxderiv[i])/dx)/((i+1)*dx+Rint)
        retour[0], retour[-1] = 0, 0
        return retour

    # creation de la figure pour l'animation
    fig, axes = plt.subplots()
    line, = axes.plot(points, U0[1:-1])

    # creation des lignes pour visualiser les interfaces entre materiaux
    def separation(mate=materiaux):
        for i in range(len(mate)-1):
            axes.plot([mate[i][1], mate[i][1]],
                      [min(U0)-1, max(U0)+1], color='k')
    separation()
    plt.xlim(0, L)
    plt.ylim(min(U0)-1, max(U0)+1)

    resultat = odeint(func=flux, y0=U0, t=temps)
    # print(resultat)

    def update(i):
        line.set_data(points, resultat[i, 1:-1])
        return line,

    # creation de l'animation
    ani = FuncAnimation(fig, update, frames=len(temps),
                        interval=25, blit=True, repeat=True)
    # plt.show()
    return fig, ani


#visualise_1Dcyl()
