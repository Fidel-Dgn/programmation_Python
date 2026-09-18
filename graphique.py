# -*- coding: utf-8 -*-
from tkinter import *
import webbrowser

def open_free_services():
    webbrowser.open_new("http://pharmacie-free-service.com")
#creer une premiere fenetre 
Root= Tk()
#personaliser la fenetre

Root.title("Pharmacie")#donner un title for the windows

Root.geometry("850x500")#permet de personnaliser la taille de la fenetre
Root.minsize(480,360)#taille minimale

Root.iconbitmap("D:/PROJET/OIP.ico")#icone de ma fenetre

Root.config(background="#41B77F") #pour configurer la couleur du back de notre fenetre

#creer la frame
frame= Frame(Root,bg='#41B77F',bd=1,relief=SUNKEN)#Frame nous permet de creer un conteneur..... bd c'est la bordure

#ajouter un premier texte
label_title = Label(frame, text="Bienvenue cher client!!! Votre phamartie toujours a votre disposition.", font=("Courrier",20), bg='#41B77F', fg='white') #declaration et creation du variable qui contient le text a afficher 

label_title.pack()#permet d'afficher et de positionner le texte avection la fonctionnalite side ou expand

#ajouter un second text

label_subtitle = Label(frame, text="Pour tout renseignement aller a l'acceuille", font=("Courrier",12), bg='#41B77F', fg='white') #declaration et creation du variable qui contient le text a afficher 

label_subtitle.pack()

#ajouter un bouton
fisrt_btn = Button(frame, text="Free services",font=("Courrier",15), bg='white', fg='#41B77F',command=open_free_services)

fisrt_btn.pack(pady=25, fill=X)
#ajouter
frame.pack(expand=YES)

#afficher : on le fait avec la fonction mainloop

Root.mainloop()