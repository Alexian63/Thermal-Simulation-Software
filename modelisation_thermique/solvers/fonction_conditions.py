#Fichier répetoire de plusieurs formes de thermostats
#thermostat en forme de cercle
def boule(T,r,z,taille,temperature):
    if z-taille<0 or r-taille<0:
        print("Erreur: Sorti de la zone graphique. Changer la taille ou la position")
        return None
    for i in range (taille):
        for j in range (taille-i):
            #T[:,z+i,r]=temperature
            T[:,z+i,r-j]=temperature
            T[:,z+i,r+j]=temperature
        for j in range (taille-i):
            #T[:,z+i,r]=temperature
            T[:,z-i,r-j]=temperature
            T[:,z-i,r+j]=temperature
    return T 
#thermostat en forme de barre verticale
def barre1(T,r,z,taille,temperature):
    if r-taille<0:
        print("Erreur: Sorti de la zone graphique. Changer la taille ou la position")
        return None
    for k in range (taille):
        T[:,:,r+k]=temperature
        T[:,:,r-k]=temperature
    return T
#thermostat en forme de barre horizontale
def barre2(T,r,z,taille,temperature):
    if z-taille<0:
        print("Erreur: Sorti de la zone graphique. Changer la taille ou la position")
        return None
    for k in range (taille):
        T[:,z+k,:]=temperature
        T[:,z-k,:]=temperature
    return T
#thermostat en forme de carré
def carre(T,r,z,taille,temperature):
    if z-taille<0 or r-taille<0:
        print("Erreur: Sorti de la zone graphique. Changer la taille ou la position")
        return None
    for k in range (taille):
        for j in range(taille):
            T[:,z+k,r+j]=temperature
            T[:,z+k,r-j]=temperature
        for j in range(taille):
            T[:,z-k,r+j]=temperature
            T[:,z-k,r-j]=temperature
    return T
#thermostat en forme de pixel
def pixel(T,r,z,taille,temperature):
    T[:,z,r]=temperature
    return T