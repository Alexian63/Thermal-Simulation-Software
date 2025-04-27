import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from solvers.features_fil import*
from solvers.parametres import *

data_fil = init_parameter_fil() #dictionnaire contenant les types d'évolution de la température à l'interface, et les paramètres associés
#Initialisation du dictionnaire : un dictionnaire par interface

def visualise_fil():

#Pas
    dx = 0.02
    dy = 0.02
    dt = 0.05
#découpages spatiaux
    Nx = data_fil["Nx"]
    Ny = data_fil["Ny"]
#découpage temporel
    nt = data_fil["nt"]
#Initialisation du terme source
    

    def condition_initiales():
        T = init_temperature(data_fil, Nx, Ny, nt)
        return T

    ajoute_source(Nx,Ny,dx,dy,data_fil)
    #Permet de passer du portrait de température d'un instant t à un instant t+dt
    def resolution():
        T = condition_initiales()
        for t in range(1, nt):
            for i in range(1, Ny - 1):
                for j in range(1, Nx - 1):
                    x = i*dx - (Nx)/2*dx
                    y = j*dy - (Ny)/2*dy
                    if x**2+y**2 < (data_fil["Rayon_fil"]+data_fil["Rgaine"]+data_fil["Delta"])**2:
                        flux_verticale = (data_fil["K"][i,j]*T[t-1,i+1,j] + data_fil["K"][i,j]*T[t-1,i-1,j] - 2*data_fil["K"][i,j]*T[t-1,i,j])/dy**2
                        flux_horizontale = (data_fil["K"][i,j]*T[t-1,i,j+1] + data_fil["K"][i,j]*T[t-1,i,j-1] - 2*data_fil["K"][i,j]*T[t-1,i,j])/dx**2
                        T[t, i, j] = T[t-1,i,j] + data_fil["S"][i,j]*dt + dt*(flux_verticale + flux_horizontale)
                    else :
                        T[t,i,j] = data_fil["Text"]
        return T

    T = resolution() #[Calcul de T si on affiche après calcul]

    # Création de la figure pour l'animation
    fig, ax = plt.subplots()
    vmin, vmax = 0, 50


# Fonction d'animation
    def animate(t):
        ax.clear()
        plt.clf()
        plt.title('Evolution de la température dans le plan\nTemps : {:.2f}'.format(10*t * dt))
        plt.xlabel('Echelle horizontale')
        plt.ylabel('Echelle verticale')
        instant = plt.imshow(T[10*t], cmap = 'viridis', interpolation='none',aspect='equal', vmin=vmin, vmax=vmax)
        instant.set_array(T[10*t])
        plt.colorbar()
        plt.scatter( 25 , 25 , s=(10.5*data_fil["Rayon_fil"]/dx)**2 ,  facecolors='none', edgecolors='white' )
        plt.scatter( 25 , 25 , s=(10.5*(data_fil["Rayon_fil"]+data_fil["Rgaine"])/dx)**2 ,  facecolors='none', edgecolors='white' )
        plt.scatter( 25 , 25 , s=(10.5*(data_fil["Rayon_fil"]+data_fil["Rgaine"]+data_fil["Delta"])/dx)**2 ,  facecolors='none', edgecolors='blue' )
        return [T], ax

    anim = FuncAnimation(fig,animate,frames = nt//10,interval =50, repeat = True, repeat_delay= 1000)
    plt.plot(T[:,25,25],)
    return fig,anim