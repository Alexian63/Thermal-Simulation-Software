import numpy as np
    

    

def init_temperature(data, Nx, Ny, nt):
    T = np.zeros([nt,Ny,Nx])
    for i in range(0,Ny):
        for j in range(0,Nx):
            T[0,i,j] = data["Tinit"]
    return T


def ajoute_source(Nx,Ny,dx,dy,data):
    for i in range (Ny):
        for j in range(Nx):
            x = i*dx - (Nx)/2*dx
            y = j*dy - (Ny)/2*dy
            if x**2+y**2 < (data["Rayon_fil"])**2:
                data["S"][i,j] = data["Rho_fil"]*((data["Intensité"]*10**4/(np.pi*data["Rayon_fil"]**2))**2)/(data["Cp1"]*data["Mass_vol1"])
                #data["S"][i,j] = 10