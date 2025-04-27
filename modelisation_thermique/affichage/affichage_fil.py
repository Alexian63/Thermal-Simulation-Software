from tkinter import ttk
import tkinter as tk
from solvers.fil import *
from solvers.parametres import *
from solvers.features_fil import *
import matplotlib as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def affichage_fil(fig, anim):
    
   #création nouvelle fenêtre
    root=tk.Tk()
    root.title('fil électrique')

    #création des différentes parties de la fenêtre

    slider_frame = ttk.Frame(root, width=300, height=900)
    btn_frame = ttk.Frame(root, width=300, height=900)

    #création des sliders

    global Tinit_slider
    global Text_slider
    global Rho_fil_entry
    global conduct_entry_1
    global conduct_entry_2
    global conduct_entry_3
    global Mass_entry_1
    global Mass_entry_2
    global Mass_entry_3
    global Cp_entry_1
    global Cp_entry_2
    global Cp_entry_3
    global R1_slider
    global R2_slider
    global R3_slider
    global Intensity_slider


    #1er matériaux
    mat1 = ttk.Frame(slider_frame,width=300, height=200, relief='sunken', borderwidth=5 )
    titre_mat1 = ttk.Label(mat1, foreground='black', font = ("Arial black", 13 ), text= '1er matériaux')

    conduct_entry_1_text = ttk.Label(mat1, foreground='black', font = ("Arial black", 9 ), text= 'Conductivité thermique [W/m.K]' )
    conduct_entry_1 = ttk.Entry(mat1, width=15)
    conduct_entry_1.insert(0, str(data_fil['K1']))

    Cp_entry_1_text = ttk.Label(mat1, foreground='black', font = ("Arial black", 9 ), text= 'Chaleur massique [J/kg]' )
    Cp_entry_1 = ttk.Entry(mat1, width=15)
    Cp_entry_1.insert(0, str(data_fil['Cp1']))

    Rho_fil_entry_text = ttk.Label(mat1, foreground='black', font = ("Arial black", 9 ), text= 'Résistivité [Ohm.m]' )
    Rho_fil_entry = ttk.Entry(mat1, width=15)
    Rho_fil_entry.insert(0, str(data_fil['Rho_fil']))

    Mass_entry_1_text = ttk.Label(mat1, foreground='black', font = ("Arial black", 9 ), text= 'Masse volumique [kg/m3]' )
    Mass_entry_1 = ttk.Entry(mat1, width=15)
    Mass_entry_1.insert(0, str(data_fil['Mass_vol1']))

    R1_slider = tk.Scale(mat1, from_=0, to_=5, resolution=0.05,orient='horizontal', length=250, label='Rayon du fil [mm]')
    R1_slider.set(10*data_fil["Rayon_fil"])
    R1_slider.grid(row=1, column=0, columnspan=2)

    Intensity_slider = tk.Scale(mat1, from_=0, to_=200, resolution=2,orient='horizontal', length=250, label='Intensité [A]')
    Intensity_slider.set(data_fil["Intensité"])
    Intensity_slider.grid(row=1, column=2, columnspan=2)

    titre_mat1.grid(row=0, column=0, columnspan=2)
    conduct_entry_1_text.grid(row=2, column=0, pady=5)
    conduct_entry_1.grid(row=3, column=0)

    Cp_entry_1_text.grid(row=2, column=1, pady=5)
    Cp_entry_1.grid(row=3, column=1)

    Rho_fil_entry_text.grid(row=2, column=2, pady=5)
    Rho_fil_entry.grid(row=3, column=2)

    Mass_entry_1_text.grid(row=2, column=3, pady=5)
    Mass_entry_1.grid(row=3, column=3)

    #2eme matériaux
    mat2 = ttk.Frame(slider_frame,width=300, height=200, relief='sunken', borderwidth=5)
    titre_mat2 = ttk.Label(mat2, foreground='black', font = ("Arial black", 13 ), text= '2eme matériaux')

    conduct_entry_2_text = ttk.Label(mat2, foreground='black', font = ("Arial black", 9 ), text= 'Conductivité thermique [W/m.K]' )
    conduct_entry_2 = ttk.Entry(mat2, width=15)
    conduct_entry_2.insert(0, str(data_fil['K2']))

    Cp_entry_2_text = ttk.Label(mat2, foreground='black', font = ("Arial black", 9 ), text= 'Chaleur massique [J/kg]' )
    Cp_entry_2 = ttk.Entry(mat2, width=15)
    Cp_entry_2.insert(0, str(data_fil['Cp2']))

    Mass_entry_2_text = ttk.Label(mat2, foreground='black', font = ("Arial black", 9 ), text= 'Masse volumique [kg/m3]' )
    Mass_entry_2 = ttk.Entry(mat2, width=15)
    Mass_entry_2.insert(0, str(data_fil['Mass_vol2']))


    R2_slider = tk.Scale(mat2, from_=0, to_=5, resolution=0.05,orient='horizontal', length=250, label='épaisseur [mm]')
    R2_slider.set(10*data_fil["Rgaine"])
    R2_slider.grid(row=1, column=0, columnspan=2)

    titre_mat2.grid(row=0, column=0, columnspan=2)
    conduct_entry_2_text.grid(row=2, column=0, pady=5)
    conduct_entry_2.grid(row=3, column=0)
    Cp_entry_2_text.grid(row=2, column=1, pady=5)
    Cp_entry_2.grid(row=3, column=1)

    Mass_entry_2_text.grid(row=2, column=2, pady=5)
    Mass_entry_2.grid(row=3, column=2)


    #3eme matériaux
    mat3 = ttk.Frame(slider_frame,width=300, height=200, relief='sunken', borderwidth=5)
    titre_mat3 = ttk.Label(mat3, foreground='black', font = ("Arial black", 13 ), text= '3eme matériaux')

    conduct_entry_3_text = ttk.Label(mat3, foreground='black', font = ("Arial black", 9 ), text= 'Conductivité thermique [W/m.K]' )
    conduct_entry_3 = ttk.Entry(mat3, width=15)
    conduct_entry_3.insert(0, str(data_fil['K3']))

    Cp_entry_3_text = ttk.Label(mat3, foreground='black', font = ("Arial black", 9 ), text= 'Chaleur massique [J/kg]' )
    Cp_entry_3 = ttk.Entry(mat3, width=15)
    Cp_entry_3.insert(0, str(data_fil['Cp3']))

    Mass_entry_3_text = ttk.Label(mat3, foreground='black', font = ("Arial black", 9 ), text= 'Masse volumique [kg/m3]' )
    Mass_entry_3 = ttk.Entry(mat3, width=15)
    Mass_entry_3.insert(0, str(data_fil['Mass_vol3']))

    R3_slider = tk.Scale(mat3, from_=0, to_=5, resolution=0.05,orient='horizontal', length=250, label='épaisseur [mm]')
    R3_slider.set(10*data_fil["Delta"])
    R3_slider.grid(row=1, column=0, columnspan=2)
    titre_mat3.grid(row=0, column=0, columnspan=2)

    conduct_entry_3_text.grid(row=2, column=1, pady=5)
    conduct_entry_3.grid(row=3, column=1)
    
    Cp_entry_3_text.grid(row=2, column=2, pady=5)
    Cp_entry_3.grid(row=3, column=2)

    Mass_entry_3_text.grid(row=2, column=3, pady=5)
    Mass_entry_3.grid(row=3, column=3)

    
    
    Tinit_slider = tk.Scale(slider_frame, from_=0, to_=100, resolution=2,orient='horizontal', length=300, label='Température T0')
    Text_slider = tk.Scale(slider_frame, from_=0, to_=100, resolution=2,orient='horizontal', length=300, label='Température extérieure')
    
    Tinit_slider.set(data_fil['Tinit'])
    Text_slider.set(data_fil['Text'])

    #création des fonctions pour les boutons

    def return_menu():
        root.destroy()
        menu()

    def restart():
        anim.frame_seq = anim.new_frame_seq()

    def apply_new_parameter():
        data_fil['Tinit']=Tinit_slider.get()
        data_fil['Text']=Text_slider.get()
    
        data_fil['Rayon_fil']=R1_slider.get()/10
        data_fil['Rgaine']=R2_slider.get()/10
        data_fil['Delta']=R3_slider.get()/10

        data_fil['K1']=float(conduct_entry_1.get())
        data_fil['K2']=float(conduct_entry_2.get())
        data_fil['K3']=float(conduct_entry_3.get())

        data_fil['Cp1']=float(Cp_entry_1.get())
        data_fil['Cp2']=float(Cp_entry_2.get())
        data_fil['Cp3']=float(Cp_entry_2.get())

        data_fil["Mass_vol1"] = float(Mass_entry_1.get())
        data_fil["Mass_vol2"] = float(Mass_entry_2.get())
        data_fil["Mass_vol3"] = float(Mass_entry_3.get())

        data_fil["Intensité"] = Intensity_slider.get()

        root.destroy()
        fig, anim = visualise_fil()
        affichage_fil(fig, anim)


    #création des boutons
    menu_button = ttk.Button(btn_frame,
                            text = "menu",
                            command = return_menu
                            )

    restart_button = ttk.Button(btn_frame,
                            text = "Start",
                            command = restart
                            )
    pause_button = ttk.Button(btn_frame,
                            text = "Pause",
                            command = anim.pause
                            )
    resume_button = ttk.Button(btn_frame,
                            text = "Resume",
                            command = anim.resume
                            )
    quit_button = ttk.Button(btn_frame,
                            text = "Quit",
                            command = exit
                            )
    apply_button = ttk.Button(slider_frame,
                              text = "Apply",
                              command = apply_new_parameter)

    


    #affichage des sliders
    Tinit_slider.grid(row=0, column=0, pady=5)
    Text_slider.grid(row=0,column=1, pady=5)

    mat1.grid(row=1, column=0, pady=15, sticky='w', columnspan=2)
    mat2.grid(row=2, column=0, pady=15, sticky='w', columnspan=2)
    mat3.grid(row=3, column=0, pady=15, sticky='w', columnspan=2)

    apply_button.grid(column=0, row=4, pady=25)

    slider_frame.grid(column=1,row=0)
    
    #affichage des boutons
    menu_button.grid(column=0,row=0, pady=10, padx=30)
    restart_button.grid(column=1, row=0, pady=10, padx=10)
    pause_button.grid(column=2, row=0, pady=10, padx=10)
    resume_button.grid(column=3, row=0, pady=10, padx=10)
    quit_button.grid(column=4, row=0, pady=10, padx=30)
    

    btn_frame.grid(column=0, columnspan=2, row= 1)

    #affichage de l'animation

    
    canvas_animation = FigureCanvasTkAgg(fig, master=root)   # Incrustation de l'animation
    canvas_animation.get_tk_widget().grid(column=0, row=0)
    anim.pause()
    