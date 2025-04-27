import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.animation import FuncAnimation
import numpy as np
import matplotlib.pyplot as plt
from modelisation_2D import * 

# Variables pour les fenêtres
interface_var = None
var_type = None
var_k = None
var_T0 = None
var_T1 = None
var_Tmin = None
var_Tmax = None

# Fonction pour mettre à jour les paramètres du dictionnaire data
def update_parameters(interface, param_type, var_type, var_k, var_T0, var_T1, var_Tmin, var_Tmax):
    data[interface]["type"] = var_type.get()
    data[interface]["k"] = float(var_k.get())
    data[interface]["T0"] = float(var_T0.get())
    data[interface]["T1"] = float(var_T1.get())
    data[interface]["Tmin"] = float(var_Tmin.get())
    data[interface]["Tmax"] = float(var_Tmax.get())


# Fonction pour créer et afficher la fenêtre principale
def create_main_window():
    global interface_var, var_type, var_k, var_T0, var_T1, var_Tmin, var_Tmax, root, K, rho, c, matCombo

    root = tk.Tk()
    root.title("Fenêtre Principale")

    # Menu déroulant pour choisir l'interface
    interface_var = tk.StringVar(root)
    interface_var.set("g")  # Valeur par défaut
    interface_menu = tk.OptionMenu(root, interface_var, "g", "d", "h", "b")
    interface_menu.pack()

    # Variables pour les cases à cocher
    var_type = tk.IntVar(root, value=data[interface_var.get()]["type"])
    var_k = tk.DoubleVar(root, value=data[interface_var.get()]["k"])
    var_T0 = tk.DoubleVar(root, value=data[interface_var.get()]["T0"])
    var_T1 = tk.DoubleVar(root, value=data[interface_var.get()]["T1"])
    var_Tmin = tk.DoubleVar(root, value=data[interface_var.get()]["Tmin"])
    var_Tmax = tk.DoubleVar(root, value=data[interface_var.get()]["Tmax"])

    # Checkbox pour choisir le type d'évolution
    checkbox_type0 = tk.Checkbutton(root, text="Constant", variable=var_type, onvalue=0, offvalue=1)
    checkbox_type0.pack()
    
    checkbox_type1 = tk.Checkbutton(root, text="Linéaire", variable=var_type, onvalue=1, offvalue=2)
    checkbox_type1.pack()
    
    checkbox_type2 = tk.Checkbutton(root, text="Rampe", variable=var_type, onvalue=2, offvalue=3)
    checkbox_type2.pack()

    # Bouton pour ouvrir la fenêtre de configuration des paramètres
    config_button = tk.Button(root, text="Configurer les paramètres", command=open_config_window)
    config_button.pack()
    
    #Curseurs des paramètres du matériau
    labelK = tk.Label(root,text= "Diffusivité thermique (µm²/s)")
    labelK.pack()
    K = tk.Scale(root, from_ = 0, to = 1e-4, resolution = 1e-7, orient = "horizontal")
    K.pack()
    labelrho = tk.Label(root, text= "Masse volumique (kg/m^3)")
    labelrho.pack()
    rho = tk.Scale(root, from_ = 0.01e3, to = 2e4, orient = "horizontal")
    rho.pack()
    labelc = tk.Label(root, text = "Capacité thermique massique (J/(kg.K))")
    labelc.pack()
    c = tk.Scale(root, from_ = 1e2, to = 2e3, orient = "horizontal")
    c.pack()
    
    #Action qui change le matériau courant
    def changeMateriau(event):
        mat = matCombo.get()
        if mat == "air":
            air_20d()
        if mat == "aluminium":
            aluminium()
        if mat == "plomb":
            plomb()
        if mat == "bronze":
            bronze()
        K.set(data["K"])
        rho.set(data["rho"])
        c.set(data["c"])
        if mat == "Libre":
            data["K"] = K.get()
            data["rho"] = rho.get()
            data["c"] = c.get()
        print("Vous avez sélectionné : '", mat,"'")
            
    #Menu déroulant pour choisir le matériau
    materiaux = ["Libre","air", "aluminium", "plomb", "bronze"]
    matCombo = ttk.Combobox(root, values=materiaux)
    matCombo.current(0)
    matCombo.pack()
    matCombo.bind("<<ComboboxSelected>>", changeMateriau)

    #Ajout de sources internes
    def rajoute_source():
        x0 = float(x0_s.get())
        y0 = float(y0_s.get())
        r = float(r_s.get())
        Pv = float(Pv_s.get())
        data["sources"].append([x0,y0,r,Pv])
        print(data["sources"])
        print("Ajout d'une source en", (x0,y0), "de rayon", r, "cm et puissance", Pv, "J")
    
    def supprime_source():
        data["sources"].pop()
        print("Source supprimée avec succès")
    
    labelx0 = tk.Label(root, text= "Abcisse")
    labelx0.pack()
    x0_s = tk.Entry(root, width = 10)
    x0_s.pack()
    labely0 = tk.Label(root, text= "Ordonnée")
    labely0.pack()
    y0_s = tk.Entry(root, width = 10)
    y0_s.pack()
    labelr = tk.Label(root, text= "Rayon")
    labelr.pack()
    labelx0.pack()
    r_s = tk.Entry(root, width = 10)
    r_s.pack()
    labelPv = tk.Label(root, text= "Puissance volumique")
    labelPv.pack()
    Pv_s = tk.Entry(root, width = 10)
    Pv_s.pack()
    ajtSrc = tk.Button(root, text = "Ajouter cette source", command = rajoute_source)
    ajtSrc.pack()
    PopSrc = tk.Button(root, text = "Supprimer la dernière source ajoutée", command = supprime_source)
    PopSrc.pack()
    
    #Bouton pour lancer l'animation
    launch_button = tk.Button(root, text = "Lancer", command = launch)
    launch_button.pack()

    # Fonction pour quitter l'interface
    def quit_interface():
        root.destroy()
    
    # Bouton pour quitter
    quit_button = tk.Button(root, text="Quitter", command=quit_interface)
    quit_button.pack()

    root.mainloop()
    

# Fonction pour ouvrir la fenêtre de configuration des paramètres
def open_config_window():
    config_window = tk.Toplevel()
    config_window.title(f"Configurer les paramètres - {interface_var.get()}")

    label_type = tk.Label(config_window, text=f"Configurer le type ({interface_var.get()}):")
    label_type.grid(row=0, column=0)
    entry_type = tk.Entry(config_window, textvariable=var_type)
    entry_type.grid(row=0, column=1)

    label_k = tk.Label(config_window, text=f"Configurer k ({interface_var.get()}):")
    label_k.grid(row=1, column=0)
    entry_k = tk.Entry(config_window, textvariable=var_k)
    entry_k.grid(row=1, column=1)

    label_T0 = tk.Label(config_window, text=f"Configurer T0 ({interface_var.get()}):")
    label_T0.grid(row=2, column=0)
    entry_T0 = tk.Entry(config_window, textvariable=var_T0)
    entry_T0.grid(row=2, column=1)

    label_T1 = tk.Label(config_window, text=f"Configurer T1 ({interface_var.get()}):")
    label_T1.grid(row=3, column=0)
    entry_T1 = tk.Entry(config_window, textvariable=var_T1)
    entry_T1.grid(row=3, column=1)

    label_Tmin = tk.Label(config_window, text=f"Configurer Tmin ({interface_var.get()}):")
    label_Tmin.grid(row=4, column=0)
    entry_Tmin = tk.Entry(config_window, textvariable=var_Tmin)
    entry_Tmin.grid(row=4, column=1)

    label_Tmax = tk.Label(config_window, text=f"Configurer Tmax ({interface_var.get()}):")
    label_Tmax.grid(row=5, column=0)
    entry_Tmax = tk.Entry(config_window, textvariable=var_Tmax)
    entry_Tmax.grid(row=5, column=1)

    # Bouton pour mettre à jour les paramètres
    update_button = tk.Button(config_window, text="Mettre à jour",
                              command=lambda: update_parameters(interface_var.get(), "g", var_type, var_k, var_T0, var_T1, var_Tmin, var_Tmax))
    update_button.grid(row=6, column=0, columnspan=2)

# Appel de la fonction pour créer l'interface principale
create_main_window()

