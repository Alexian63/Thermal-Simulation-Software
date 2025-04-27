import numpy as np

#Initialise les températures aux interfaces en fonction des valeurs du dictionnaire
def init_interfaces(data, T, Nx, Ny):
    if data["h"]["type"] == 0:
        T[:,0,:] = data["h"]["k"]
    if data["h"]["type"] == 1:
        T[:,0,:] = np.linspace(data["h"]["T0"], data["h"]["T1"], Nx)
    if data["h"]["type"] == 2:
        T[:,0,:] = rampe(data["h"]["Tmin"],data["h"]["Tmax"], Nx)
    if data["b"]["type"] == 0:
        T[:,-1,:] = data["b"]["k"]
    if data["b"]["type"] == 1:
        T[:,-1,:] = np.linspace(data["b"]["T0"], data["b"]["T1"], Nx)
    if data["b"]["type"] == 2:
        T[:,-1,:] = rampe(data["b"]["Tmin"],data["b"]["Tmax"], Nx)
    if data["g"]["type"] == 0:
        T[:,:,0] = data["g"]["k"]
    if data["g"]["type"] == 1:
        T[:,:,0] = np.linspace(data["g"]["T0"], data["g"]["T1"], Ny)
    if data["g"]["type"] == 2:
        T[:,:,0] = rampe(data["g"]["Tmin"],data["g"]["Tmax"], Ny)
    if data["d"]["type"] == 0:
        T[:,:,-1] = data["d"]["k"]
    if data["d"]["type"] == 1:
        T[:,:,-1] = np.linspace(data["d"]["T0"], data["d"]["T1"], Ny)
    if data["d"]["type"] == 2:
        T[:,:,-1] = rampe(data["d"]["Tmin"],data["d"]["Tmax"], Ny)

#Initialise la température dans tout le matériau
def init_temperature(data, Nx, Ny, nt):
    T = np.zeros([nt,Ny,Nx])
    init_interfaces(data, T, Nx, Ny)
    for i in range(1,Ny-1):
        for j in range(1,Nx-1):
            T[0,i,j] = data["Tini"]
    return T

#Permet d'initialiser la température sous forme de rampe
def rampe(Tmin, Tmax, N):
    a = Tmax - Tmin
    L1 = [Tmin + 2*a/N*i for i in range (N//2)]
    L2 = [Tmax - 2*a/N*i for i in range (N//2)]
    return np.array(L1+L2)

#Permet d'ajouter une source de chaleur sur un certain rayon r
def source_rond(x0,y0,r,Nx,Ny,dx,dy,data,Pv):
    for i in range (Ny):
        for j in range(Nx):
            x = i*dx - (Nx)/2*dx + x0
            y = j*dy - (Ny)/2*dy - y0
            if np.sqrt(x**2+y**2) < r:
                data["S"][i,j] = Pv/(data["rho"]*data["c"])
