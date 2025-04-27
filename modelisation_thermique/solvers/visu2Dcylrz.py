from tkinter import ttk
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from solvers.parametres import *
from tkinter import ttk
import affichage.interface as affinter

def visualise_2D_cylrz():
    #importation et définition des paramètres par défaut de la simulation
    parameters_2Dcylrz=init_parameters_2Dcylrz()
    global radius
    global height
    global alpha
    radius = parameters_2Dcylrz['radius']
    height = parameters_2Dcylrz['height']
    pas = parameters_2Dcylrz['pas']
    global fct
    fct = parameters_2Dcylrz['fonction']
    alpha = parameters_2Dcylrz['alpha']
    global taille
    taille = parameters_2Dcylrz['taille']
    global temperature
    temperature=parameters_2Dcylrz['temperature']
    #Création de la fenêtre graphique et des éléments personnalisables
    root=tk.Tk()
    root.title('2D cylindrique à r et z variables')
    slider_frame = ttk.Frame(root, width=300, height=900)
    menu1 = ttk.Frame(slider_frame, width=300, height=200,
                      relief='sunken', borderwidth=5)
    titre_menu1 = ttk.Label(menu1, foreground='black', font=(
        "Arial black", 13), text='Menu de selection du thermostat')
    menu2 = ttk.Frame(slider_frame, width=300, height=200,
                      relief='sunken', borderwidth=5)
    titre_menu2 = ttk.Label(menu2, foreground='black', font=(
        "Arial black", 13), text='Menu de selection des propriétés physiques du matériau')
    taille_text = ttk.Label(menu1, foreground='black',
                            font=("Arial black", 9), text='taille')
    taille_entry = ttk.Entry(menu1, width=15)
    taille_entry.insert(0, str(parameters_2Dcylrz['taille']))
    height_text = ttk.Label(menu2, foreground='black',
                            font=("Arial black", 9), text='hauteur')
    height_entry = ttk.Entry(menu2, width=15)
    height_entry.insert(0, str(parameters_2Dcylrz['height']))
    radius_text = ttk.Label(menu2, foreground='black',
                            font=("Arial black", 9), text='rayon')
    radius_entry = ttk.Entry(menu2, width=15)
    radius_entry.insert(0, str(parameters_2Dcylrz['radius']))
    temperature_text = ttk.Label(menu1, foreground='black', font=(
        "Arial black", 9), text='temperature')
    temperature_entry = ttk.Entry(menu1, width=15)
    temperature_entry.insert(0, str(parameters_2Dcylrz['temperature']))
    titre_menu1.grid(row=0, column=0, columnspan=2)
    titre_menu2.grid(row=1, column=0, columnspan=2)
    taille_text.grid(row=2, column=0, pady=5)
    taille_entry.grid(row=2, column=1)
    height_text.grid(row=5, column=0, pady=5)
    height_entry.grid(row=5, column=1)
    radius_text.grid(row=4, column=0, pady=5)
    radius_entry.grid(row=4, column=1)
    temperature_text.grid(row=3, column=0, pady=5)
    temperature_entry.grid(row=3, column=1)
    difu_slider = tk.Scale(menu2, from_=0, to_=1000, resolution=5,
                           orient='horizontal', length=300, label='diffusivité thermique (x10^(-6))')
    difu_slider.set(parameters_2Dcylrz['alpha'])
    difu_slider.grid(row=3, column=0, pady=15)
    menu1.grid(row=0, column=0, pady=15)
    menu2.grid(row=1, column=0, pady=15)
    slider_frame.grid(column=0, row=0)
    #applique les paramètres du thermostat lors du clic sur le bouton
    def update1():
        global taille
        taille = int(taille_entry.get())
        global temperature
        temperature = int(temperature_entry.get())
    #applique les paramètres du materiau lors du clic sur le bouton
    def update2():
        radius = int(radius_entry.get())
        height = int(height_entry.get())
        alpha = difu_slider.get()*10**(-6)
        #discrétisation temporelle
        dt = 0.02  # Pas temporel
        duration = 10 # Durée totale de simulation
        nt = int(duration / dt) + 1
        # Discrétisation spatiale
        nr = radius*pas  # Nombre de points radiaux
        nz = height*pas  # Nombre de points axiaux
        dr = radius / nr #pas radial
        dz = height / nz #pas axial
        # fonction choisie pour le thermostat
        def CI(T,fct,r,z,taille,temperature):
            return fct(T,r,z,taille,temperature)
        # initialisation de la matrice des températures
        T = np.zeros((nt,nz, nr))
        #affichage du thermostat lors du clic sur la figure
        def mouse_event(event):
            T = np.zeros((nt, nz, nr))
            global R
            global Z
            #détection du lieu du clic
            R=int(event.xdata) 
            Z=int(event.ydata)
            #affichage du thermostat
            T=CI(T,fct,R,Z,taille,temperature) 
            ax.clear()
            plt.clf()
            # formatage des axes
            plt.title(
                'Evolution de la température dans le cylindre\nTemps : {:.2f}'.format(0))
            plt.xlabel('Position radiale')
            plt.ylabel('Position axiale')
            #affichage de l'image à l'instant 0
            plt.imshow(T[0,:,:], cmap = 'viridis', interpolation='none',aspect='equal', vmin=0, vmax=temperature)
            plt.colorbar()
            #incrustation de la fenêtre pyplot sur tkinter
            canvas_animation = FigureCanvasTkAgg(fig, master=root)
            canvas_animation.get_tk_widget().grid(column=0, row=0)
        #création de la fenêtre graphique pyplot
        fig, ax = plt.subplots()
        #détection du clic
        cid = fig.canvas.mpl_connect('button_press_event', mouse_event)
        #affichage de la figure avec des températures nulles à l'instant 0 avant la création du thermostat
        ax.clear()
        plt.clf()
        #formatage des axes
        plt.title('Evolution de la température dans le cylindre\nTemps : {:.2f}'.format(0))
        plt.xlabel('Position radiale')
        plt.ylabel('Position axiale')
        #affichage de l'image à l'instant 0
        plt.imshow(T[0,:,:], cmap = 'viridis', interpolation='none',aspect='equal', vmin=0, vmax=temperature)
        plt.colorbar()
        #fonction appellé lors du clic sur le bouton "apply" de validation
        def apply_new_parameter():
            root.destroy() #fermeture de l'ancienne fenêtre tkinter
            window=tk.Tk() #ouverture de la nouvelle fenêtre
            window.title('2D cylindrique à r et z variables: animation')
            #Réslution numérique de l'équation de la chaleur en 2D cylindrique pour r et z variables
            T = np.zeros((nt,nz, nr))
            T=CI(T,fct,R,Z,taille,temperature)  
            def resolution(U):
                T=U
                for t in range (1,nt):
                    for r in range (1,nr-1):
                        for z in range (1,nz-1):
                            laplacienr=(1/(r*dr))*((r+1)*(U[t-1,z,r+1]-U[t-1,z,r])-r*(U[t-1,z,r]-U[t-1,z,r-1]))
                            laplacienz=(U[t-1,z+1,r]-2*U[t-1,z,r]+U[t-1,z-1,r])/(dz**2)
                            T[t,z,r]=T[t-1,z,r]+(laplacienr+laplacienz)*alpha*dt
                            T=CI(T,fct,R,Z,taille,temperature)
                    print("avancée:",t/nt*100) #affichage de la progression des calculs
                return T
            #création et affichage de l'animation de la diffusion 
            fig, ax = plt.subplots()
            T=resolution(T)
            #fonction d'affichage de chaque frame de l'image
            def update(frame):
                # réinitialisation de l'image
                ax.clear()
                plt.clf()
                # formatage des axes
                plt.title('Evolution de la température dans le cylindre\nTemps : {:.2f}'.format(
                    frame * 10*dt))
                plt.xlabel('Position radiale')
                plt.ylabel('Position axiale')
                # affichage de l'image à l'instant "frame"
                instant = plt.imshow(T[10*frame, :, :], cmap='viridis',
                                     interpolation='none', aspect='equal', vmin=0, vmax=100)
                instant.set_array(T[10*frame, :, :])
                # affichage de la barre de couleur
                plt.colorbar()
            # Création de l'animation
            animation = FuncAnimation(fig, update, frames=nt//10+1, interval=5, blit=False,repeat=False)
            # Incrustation de l'animation dans tkinter
            canvas_animation = FigureCanvasTkAgg(fig, master=window)
            canvas_animation.get_tk_widget().grid(column=0, row=0)
            window.mainloop()
        #Création du bouton de validation
        apply_button = ttk.Button(slider_frame,text = "Apply",command = apply_new_parameter)
        apply_button.grid(column=0, row=2, pady=25)
        slider_frame.grid(column=1,row=0)
        canvas_animation = FigureCanvasTkAgg(fig, master=root)   # Incrustation de l'animation
        canvas_animation.get_tk_widget().grid(column=0, row=0)
    update2()
    def return_menu():
        root.destroy()
        affinter.menu()
    button1 = ttk.Button(menu1,text="Apply",command=update1)
    button1.grid(column=0, row=4, pady=25)
    button2 = ttk.Button(menu2, text="Apply", command=update2)
    button2.grid(column=0, row=6, pady=25)
    quit_button = ttk.Button(slider_frame, text="Quit", command=exit)
    quit_button.grid(column=1, row=2, pady=10, padx=30)
    menu_button = ttk.Button(slider_frame, text="Menu", command=return_menu)
    menu_button.grid(column=1, row=3, pady=10, padx=30)
    #fonction appellée pour choisir la forme du thermostat
    def action(event):
        global fct
        # Obtention de l'élément sélectionné dans le menu déroulant
        select = listeCombo.get()
        if select=='cercle':
            fct=boule
        elif select=='barre horizontale':
            fct=barre2
        elif select=='barre verticale':
            fct=barre1
        elif select=='pixel':
            fct=pixel
        elif select=='carré':
            fct=carre
    #Création du texte associé au menu déroulant
    labelChoix = tk.Label(menu1, text = "Choix de la forme")
    labelChoix.grid(row=1,column=0)

    #création de la liste Python contenant les éléments de la liste Combobox
    listeProduits=["cercle", "carré","barre verticale","barre horizontale","pixel"]

    #Création de la Combobox
    listeCombo = ttk.Combobox(menu1, values=listeProduits)
    
    # Choix de l'élément qui s'affiche par défaut
    listeCombo.current(0)

    listeCombo.grid(row=1, column=1)
    listeCombo.bind("<<ComboboxSelected>>", action)
    root.mainloop()
