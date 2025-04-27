# ce fichier permet de mettre des valeurs par defaut a nos differentes simulations
# ce qui permet de les lancer directement sans attendre que l'utilisateur inserte ses valeurs

import numpy as np
from solvers.fonction_conditions import *


def init_parameter_fil():
    global data_fil
    data_fil = {}
    data_fil["Lx"] = 1  # longueur (horizontale)
    data_fil["Ly"] = 1  # verticale
    data_fil["Rayon_fil"] = 0.1
    data_fil["Delta"] = 0.1
    data_fil["Rgaine"] = 0.2
    data_fil["Text"] = 0
    data_fil["Tinit"] = 25
# temps de résolution
    data_fil["time"] = 300
    data_fil["Rho_fil"] = 17e-9
    data_fil["Intensité"] = 100
    data_fil["Mass_vol1"] = 9e3
    data_fil["Cp1"] = 385
    data_fil["K1"] = 401
    data_fil["Mass_vol2"] = 900
    data_fil["Cp2"] = 3
    data_fil["K2"] = 500
    data_fil["Mass_vol3"] = 1.2
    data_fil["Cp3"] = 1004
    data_fil["K3"] = 0.03


# Paramètres fixés ou liés:

# Pas
    data_fil["dx"] = 0.02
    data_fil["dy"] = 0.02
    data_fil["dt"] = 0.05

    dx = data_fil["dx"]
    dy = data_fil["dy"]
    dt = data_fil["dt"]
# découpages spatiaux
    data_fil["Nx"] = int(data_fil["Lx"]/dx)
    data_fil["Ny"] = int(data_fil["Ly"]/dy)
# découpage temporel
    data_fil["nt"] = int(data_fil["time"]/dt)
    Nx = data_fil["Nx"]
    Ny = data_fil["Ny"]
# Initialisation du terme source
    data_fil["S"] = np.zeros([int(data_fil["Ly"]/dy), int(data_fil["Lx"]/dx)])
# Paramétrage de la fenêtre de chaleur
    data_fil["K"] = np.zeros((Ny, Nx))
    data_fil["K"][:, :] = data_fil["K3"] / \
        (data_fil["Mass_vol3"]*data_fil["Cp3"])
    for j in range(Ny):
        for i in range(Nx):
            y = dy*(j - Ny/2)
            x = dx*(i - Nx/2)
            if x**2 + y**2 <= (data_fil["Rayon_fil"])**2:
                data_fil["K"][j, i] = data_fil["K1"] / \
                    (data_fil["Cp1"]*data_fil["Mass_vol1"])
            elif x**2 + y**2 <= (data_fil["Rayon_fil"] + data_fil["Rgaine"])**2:
                data_fil["K"][j, i] = data_fil["K2"] / \
                    (data_fil["Cp2"]*data_fil["Mass_vol2"])

    data_fil["Tmin"] = 0
    data_fil["Tmax"] = 100
    data_fil["S"] = np.zeros((Ny, Nx))

    return data_fil

#initialisation par défaut des paramètres de simulation pour le cas 2D cylindrique à r et z variables
def init_parameters_2Dcylrz():
    global parameters_2Dcylrz
    parameters_2Dcylrz = {}
    parameters_2Dcylrz['temperature'] = 273
    parameters_2Dcylrz['taille'] = 5
    parameters_2Dcylrz['fonction'] = boule
    parameters_2Dcylrz['alpha'] = 0.005
    parameters_2Dcylrz['pas'] = 10 #discrétisation spatiale rapportée à l'unité de distance
    parameters_2Dcylrz['radius'] = 2
    parameters_2Dcylrz['height'] = 3
    return parameters_2Dcylrz


def init_parameters_1Dcarte():
    global parameters_1Dcarte
    parameters_1Dcarte = {}
    parameters_1Dcarte['T0'] = 273
    parameters_1Dcarte['T1'] = 2000
    parameters_1Dcarte['T2'] = 273
    parameters_1Dcarte['R1'] = 1
    parameters_1Dcarte['R2'] = 3
    parameters_1Dcarte['R3'] = 5
    parameters_1Dcarte['K1'] = 1
    parameters_1Dcarte['K2'] = 20
    parameters_1Dcarte['K3'] = 0.6
    return parameters_1Dcarte


def init_parameters_1Dcyl():
    global parameters_1Dcyl
    parameters_1Dcyl = {}
    parameters_1Dcyl['T0'] = 273
    parameters_1Dcyl['T1'] = 2000
    parameters_1Dcyl['T2'] = 273
    parameters_1Dcyl['R1'] = 1
    parameters_1Dcyl['R2'] = 3
    parameters_1Dcyl['R3'] = 5
    parameters_1Dcyl['K1'] = 1
    parameters_1Dcyl['K2'] = 20
    parameters_1Dcyl['K3'] = 0.6
    return parameters_1Dcyl

#


def init_parameters_2Drtheta():
    global parameters_2Drtheta
    parameters_2Drtheta = {}
    parameters_2Drtheta['T0'] = 0
    parameters_2Drtheta['T1'] = 100
    parameters_2Drtheta['T2'] = 100
    parameters_2Drtheta['theta1'] = 30
    parameters_2Drtheta['theta2'] = 40
    parameters_2Drtheta['radius'] = 1
    return parameters_2Drtheta
