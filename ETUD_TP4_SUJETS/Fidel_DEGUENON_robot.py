# Biblothèques nécessaires au TP

import turtle as tl
import random as rd

##################################################################
# SOUS-PROGRAMMES DE GESTION DES OUVERTURES ######################
#                                           ######################
# ajouter_ouverture, supprimer_ouvertures   ######################
##################################################################

def ajouter_ouverture(ouverture,piece,mode_trace):
    if mode_trace:
        #verification id parametre formelle
        print("ID parametre formelle :",id(ouverture))
        print(f"Identifiant paramètre formel: piece = {piece} : {id(piece)} ")

    #verification du type des parametres en entré 
    c=False #verifier la conformité des coin de mur d'ouverture avec les coins de la piece
    if ((not isinstance(piece,dict))or(not isinstance(ouverture,dict))):
        print("Erreur: le paramètre n'est pas un dictionnaire représentant une pièce...")
        return
    else:
        for ouv in piece["liste_ouvertures"]:
            if(ouverture==ouv):
                print("L'ouverture existe deja dans la liste des ouverture...")
                return
            
        for coin in piece["coins_piece"]:
            if(ouverture["coins_mur_ouverture"]==coin):
                c=True
                
        if not c:
            print("Erreur: le coin d'ouverture n'est pas un coin de la pièce...")
            return
        else:

            if ((ouverture["largeur"]!=None and ouverture["largeur"]>0) and (ouverture["dist_coins_mur"]!=None and ouverture["dist_coins_mur"]>0) and (ouverture["couleur"]!=None) and (ouverture["largeur_trait"]!=None and ouverture["largeur_trait"]>0)):
                print("Parametre valides")
                piece["liste_ouvertures"].append(ouverture)
                print("ouverture ajoutée avec succès à la pièce")
                
                

def supprimer_ouvertures(piece,mode_trace):
    if mode_trace:
        #verification id parametre formelle
        print("ID parametre formelle :",id(piece))
        print(f"Identifiant paramètre formel: piece = {piece} : {id(piece)} ")

    #verification du type des parametres en entré 
    if (not isinstance(piece,dict)):
        print("Erreur: le paramètre n'est pas un dictionnaire représentant une pièce...")
        return
    else:
        for ouv in piece["liste_ouvertures"]:
            piece["liste_ouvertures"].remove(ouv)
        
        print("toutes les ouvertures ont été supprimées de la pièce avec succès")
            
            
            
##################################################################
# SOUS-PROGRAMMES DE GESTION DES OBSTACLES  ######################
#                                           ######################
# ajouter_obstacle, supprimer_obstacles     ######################
##################################################################


def ajouter_obstacle(obs,piece,mode_trace):
    if mode_trace:
        #print("ID parametre formelle :",id(obs))
        #print(f"Identifiant paramètre formel: piece : {id(piece)} ")
        print("ID parametre formelle :",id(obs))
        print(f"Identifiant paramètre formel: piece : {id(piece)} ")
    if (not isinstance(obs,dict))or(not isinstance(piece,dict)):
        print("Erreur: le paramètre n'est pas un dictionnaire représentant un obstacle...")
        return
    else:
        for obs_exist in piece["liste_obstacles"]:
            if(obs==obs_exist):
                print("L'obstacle existe deja dans la liste des obstacles...")
                return
        if((obs["type"]=="cercle")):
            if((obs["position"]!=None and (abs(obs["position"][0])<=abs(piece["position_coin_HD"][0]-obs["rayon"]-5 )and abs(obs["position"][1])<=abs(piece["position_coin_HD"][1]-obs["rayon"]-5))) and (obs["rayon"]!=None and obs["rayon"]>0) and (obs["couleur"]!=None) and (obs["largeur_trait"]!=None and obs["largeur_trait"]>0))and (piece["dimensions"][0]!=None and piece["dimensions"][0]>0)and(piece["dimensions"][1]!=None and piece["dimensions"][1]>0)and (piece["dimensions"][0]==2*piece["position_coin_HD"][0])and(piece["dimensions"][1]==2*piece["position_coin_HD"][1]):
                print("Parametre valides")
                
                piece["liste_obstacles"].append(obs)
                print("obstacle ajouté à la liste des obstacles de la pièce")
            else:
                print("Erreur: les informations de l'obstacle ne sont pas correctes...")
        elif (obs["type"]=="rectangle"):
            if((obs["position"]!=None and (abs(obs["position"][0])<=abs(piece["position_coin_HD"][0]-obs["largeur"]/2-5 ))and (abs(obs["position"][1])<=abs(piece["position_coin_HD"][1]-obs["longueur"]/2-5))) and (obs["largeur"]!=None and obs["largeur"]>0)  and (obs["longueur"]!=None and obs["longueur"]>0) and (obs["couleur"]!=None) and (obs["largeur_trait"]!=None and obs["largeur_trait"]>0))and (piece["dimensions"][0]!=None and piece["dimensions"][0]>0)and(piece["dimensions"][1]!=None and piece["dimensions"][1]>0)and (piece["dimensions"][0]==2*piece["position_coin_HD"][0])and(piece["dimensions"][1]==2*piece["position_coin_HD"][1]):
                print("Parametre valides")
                
                piece["liste_obstacles"].append(obs)
                print("obstacle ajouté à la liste des obstacles de la pièce")
            else:
                print("Erreur: les informations de l'obstacle ne sont pas correctes...")
        else:
            print("Erreur: le type d'obstacle n'est pas reconnu... Veuillez revérifier le parametre en entrée.")
            return

#Ce  sous-programme est une procédure            
def supprimer_obstacle(piece,mode_trace):
    if mode_trace:
        #verification id parametre formelle
        print("ID parametre formelle :",id(piece))
        print(f"Identifiant paramètre formel: piece : {id(piece)} ")

    #print(f"Identifiant paramètre formel: piece : {id(piece)} ")
    if (not isinstance(piece,dict)):
        print("Erreur: le paramètre n'est pas un dictionnaire représentant un obstacle...")
        return
    else:
        for obs in piece["liste_obstacles"]:
            piece["liste_obstacles"].remove(obs)
        print("tous les obstacles ont été supprimés de la liste des obstacles de la pièce")                  



####################################################################################
# SOUS-PROGRAMMES DE TRACAGE DES ELEMENTS DE L'ENVIRONNEMENT  ######################
#                                                             ######################
# tracer_piece, tracer_ouvertures_piece                       ######################
# tracer_obstacles_piece, tracer_environnement                ######################
####################################################################################

#tracer_piece
def tracer_piece(piece,mode_trace):
    
    #print(f"Identifiant paramètre formel: piece = {piece} : {id(piece)} ")
    if mode_trace:
        print("ID parametre formelle :",id(piece))
        print(f"Identifiant paramètre formel: piece = {piece} : {id(piece)} ")
    if not isinstance(piece,dict):
        print("Erreur: le paramètre n'est pas un dictionnaire représentant une pièce...")
        return
    else:
        
        if ((piece["dimensions"][0]!=None and piece["dimensions"][0]>0)and(piece["dimensions"][1]!=None and piece["dimensions"][1]>0))and (piece["dimensions"][0]==2*piece["position_coin_HD"][0])and(piece["dimensions"][1]==2*piece["position_coin_HD"][1]):
            print("coins_HD/Longueur/Largeur valides")

            # néttoyage de la table traçante
            tl.clearscreen()

            # Stylet en position haute - pas de traçage
            tl.up()

            # position du coin Haut Droit
            coin_HD = piece["position_coin_HD"]
            x_HD, y_HD = coin_HD
            print('TRACE coordonnées coinHD =', x_HD, y_HD)

            # déplacement au coin Haut Droit 
            tl.goto(coin_HD)

            # direction à prendre pou le traçage du premier côté
            tl.right(90)

            # Dimensions de la pièce carrée
            longueur = piece["dimensions"][0]
            largeur = piece["dimensions"][1]
            angle = 90

            # Données pour le traçage
            tl.width(5)                  # largeur du trait
            tl.color('red')             # couleur du trait
            tl.down()                    # stylet en position basse pour le traçage

            # tracer les contours de la pièce
            for i in range(2):
                tl.forward(longueur)
                tl.right(angle)
                tl.forward(largeur)
                tl.right(angle)
            
            tl.up()                      # retour en position haute
            print("tracage de la piece effectué avec succès...")
        else:
            print("Erreur: les dimensions ou la position de la piece ne sont pac corrects...")
            
#tracer_ouvertures_piece

def tracer_ouvertures_piece(piece,mode_trace):
    if mode_trace:
        print("ID parametre formelle :",id(piece))
        print(f"Identifiant paramètre formel: piece = {piece} : {id(piece)} ")
    #print(f"Identifiant paramètre formel: piece = {piece} : {id(piece)} ")
    if (not isinstance(piece,dict)):
        print("Erreur: les paramètres ne sont pas des dictionnaires représentant une ouverture...")
        return
    else:
        
        if(piece["dimensions"][0]!=None and piece["dimensions"][0]>0)and(piece["dimensions"][1]!=None and piece["dimensions"][1]>0)and (piece["dimensions"][0]==2*piece["position_coin_HD"][0])and(piece["dimensions"][1]==2*piece["position_coin_HD"][1]):
            
            for ouverture in piece["liste_ouvertures"]:
                
                # Traçage de la porte 1
                tl.up()                         # stylet en position haute
                tl.width(ouverture["largeur_trait"])                    # largeur du trait des ouvertures
                 
                tl.goto(ouverture["coins_mur_ouverture"])
                

                
                
                if (ouverture["coins_mur_ouverture"]==piece["coins_piece"][0]):
                    tl.setheading(270)  # orientation vers le bas
                   
                    ouverture["position"] = (piece["coins_piece"][0][0],ouverture["coins_mur_ouverture"][1] - ouverture["dist_coins_mur"]-ouverture["largeur"]) 
                elif (ouverture["coins_mur_ouverture"]==piece["coins_piece"][1]):
                    tl.setheading(180)  # orientation vers la gauche
                    ouverture["position"] = (piece["coins_piece"][1][0] - ouverture["dist_coins_mur"]-ouverture["largeur"],piece["coins_piece"][1][1])
                elif (ouverture["coins_mur_ouverture"]==piece["coins_piece"][2]):
                    tl.setheading(90)  # orientation vers le haut
                    ouverture["position"] = (piece["coins_piece"][2][0],piece["coins_piece"][2][1] + ouverture["dist_coins_mur"]+ouverture["largeur"])
                elif (ouverture["coins_mur_ouverture"]==piece["coins_piece"][3]):
                    tl.setheading(0)  # orientation vers la droite
                    ouverture["position"] = (piece["coins_piece"][3][0] + ouverture["dist_coins_mur"]+ouverture["largeur"],piece["coins_piece"][3][1])
                else:
                    print("Erreur: le coin d'ouverture n'est pas un coin de la pièce...")
                tl.forward(ouverture["dist_coins_mur"])  # déplacement jusqu'à la position de la porte
                tl.down()                       # stylet en position basse
                tl.width(ouverture["largeur_trait"])  
                tl.color(ouverture["couleur"])
                tl.forward(ouverture["largeur"])      # traçage de la porte
                tl.up()  # stylet en position haute
                                                
                print("tracage de des ouvertures effectuées avec succès...",ouverture["nom"])
        else:
            print("Erreur: les informations de l'ouverture ne sont pas correctes...")
 
 
 
           
#tracer_obstacles_piece

def tracer_obstacles_piece(piece,mode_trace):
    if mode_trace:
        print("ID parametre formelle :",id(piece))
        print(f"Identifiant paramètre formel: piece = {piece} : {id(piece)} ")

    #print(f"Identifiant paramètre formel: piece : {id(piece)} ")
    if (not isinstance(piece,dict)):
        print("Erreur: le paramètre n'est pas un dictionnaire représentant un obstacle...")
        return
    else:
        for obstacle in piece["liste_obstacles"]:
            
            if(piece["dimensions"][0]!=None and piece["dimensions"][0]>0)and(piece["dimensions"][1]!=None and piece["dimensions"][1]>0)and (piece["dimensions"][0]==2*piece["position_coin_HD"][0])and(piece["dimensions"][1]==2*piece["position_coin_HD"][1]):
                print("Parametre valides")
                tl.width(obstacle["largeur_trait"])                    # largeur du trait des ouvertures
                tl.up()                                              # stylet en position haute  
                tl.goto(obstacle["position"])                               # déplacement jusqu'au la position de l'obstacle 1


                tl.width(obstacle["largeur_trait"])      
                tl.color(obstacle["couleur"])
                if obstacle["type"] == 'cercle' : 
                    tl.forward(obstacle["rayon"])
                    tl.down()                           # stylet en position basse
                    tl.begin_fill()
                    tl.circle(obstacle["rayon"])
                    tl.end_fill ()
                if obstacle["type"] == 'rectangle' : 
                    tl.down()                           # stylet en position basse
                    tl.begin_fill()
                    tl.forward(obstacle["longueur"])
                    tl.right(90)
                    tl.forward(obstacle["largeur"])
                    tl.right(90)
                    tl.forward(obstacle["longueur"])
                    tl.right(90)
                    tl.forward(obstacle["largeur"])
                    tl.right(90)
                    tl.end_fill ()
            
                tl.up()                         # retour en position haute
                ajouter_obstacle(obstacle,piece,mode_trace)
                print("tracage de l'obstacle effectué avec succès...")
                
            else:
                print("Erreur: les informations de l'obstacle ne sont pas correctes...")


#tracer_environnement

def tracer_environnement(piece,mode_trace):
    
    #print(f"Identifiant paramètre formel: piece = {piece} : {id(piece)} ")
    if not isinstance(piece,dict):
        print("Erreur: le paramètre n'est pas un dictionnaire représentant une pièce...")
        return
    else:
        if mode_trace:
            print("ID parametre formelle :",id(piece))
            print(f"Identifiant paramètre formel: piece = {piece} : {id(piece)} ")

        if ((piece["dimensions"][0]!=None and piece["dimensions"][0]>0)and(piece["dimensions"][1]!=None and piece["dimensions"][1]>0))and (piece["dimensions"][0]==2*piece["position_coin_HD"][0])and(piece["dimensions"][1]==2*piece["position_coin_HD"][1]):
            print("coins_HD/Longueur/Largeur valides")

            # néttoyage de la table traçante
            tl.clearscreen()

            # Stylet en position haute - pas de traçage
            tl.up()

            # position du coin Haut Droit
            coin_HD = piece["position_coin_HD"]
            x_HD, y_HD = coin_HD
            print('TRACE coordonnées coinHD =', x_HD, y_HD)

            # déplacement au coin Haut Droit 
            tl.goto(coin_HD)

            # direction à prendre pou le traçage du premier côté
            tl.right(90)

            # Dimensions de la pièce carrée
            longueur = piece["dimensions"][0]
            largeur = piece["dimensions"][1]
            angle = 90

            # Données pour le traçage
            tl.width(5)                  # largeur du trait
            tl.color('red')             # couleur du trait
            tl.down()                    # stylet en position basse pour le traçage

            # tracer les contours de la pièce
            for i in range(2):
                tl.forward(longueur)
                tl.right(angle)
                tl.forward(largeur)
                tl.right(angle)
            
            tl.up()                      # retour en position haute
            print("tracage de la piece effectué avec succès...")
            
            tracer_ouvertures_piece(piece,mode_trace)
            tracer_obstacles_piece(piece,mode_trace)
        else:
            print("Erreur: les dimensions ou la position de la piece ne sont pac corrects...")
                
                
####################################################################################
# INITIALISATION ET AFFICHAGE DE L'ENVIRONNEMENT              ######################
#                                                             ######################
# initialiser_environnement, afficher_info_environnement      ######################
####################################################################################
# ces deux sous-programmes seront à utiliser à la place de la création faite dans  #
# le TP3 -- Cela peut simuler la lecture des informations dans un fichier          #
####################################################################################


def initialiser_environnement(mode_trace):

    piece = {"nom": "entrepot", "dimensions": (400, 400), "position_coin_HD": (200, 200),
             "coins_piece": [], "liste_ouvertures": [], "liste_obstacles": []}

    piece["coins_piece"] = [
        (piece["position_coin_HD"][0], piece["position_coin_HD"][1]),
        (piece["position_coin_HD"][0], piece["position_coin_HD"][1] - piece["dimensions"][1]),
        (piece["position_coin_HD"][0] - piece["dimensions"][0], piece["position_coin_HD"][1] - piece["dimensions"][1]),
        (piece["position_coin_HD"][0] - piece["dimensions"][0], piece["position_coin_HD"][1])
    ]

    ouverture = {"nom": "porte1", "largeur": 60, "coins_mur_ouverture": piece["coins_piece"][0],
                 "dist_coins_mur": 100, "position": None, "couleur": "orange", "largeur_trait": 10}

    obstacle = {"nom": "obstacle1", "type": "cercle", "rayon": 20, "position": (50, 50),
                "couleur": "green", "largeur_trait": 10}

    ajouter_ouverture(ouverture, piece,mode_trace)
    ajouter_obstacle(obstacle, piece,mode_trace)

    return piece

########

def afficher_info_environnement(piece,mode_trace):
    if mode_trace:
        print("ID parametre formelle :",id(piece))
        print(f"Identifiant paramètre formel: piece = {piece} : {id(piece)} ")

    print("PIECE -----------------------")
    for cle in piece.keys():
        if cle not in ["liste_ouvertures", "liste_obstacles"]:
            print("\t", cle, " = ", piece[cle])

    nb_ouvertures = len(piece["liste_ouvertures"])
    nb_obstacles = len(piece["liste_obstacles"])
    for ouv in range(nb_ouvertures):
        print("OUVERTURE ", ouv + 1, " = ", piece["liste_ouvertures"][ouv])
    for obs in range(nb_obstacles):
        print("OBSTACLE ", obs + 1, " = ", piece["liste_obstacles"][obs])

    return None

########



####################################################################################
# SOUS-PROGRAMMES DE GESTION DES DEPLACEMENT DU ROBOT.        ######################
#                                                             ######################
# ajouter_trajectoire, supprimer_trajectoire                  ######################
####################################################################################

def ajouter_trajectoire(robot,trajectoire,mode_trace):
    if mode_trace:
        print("ID parametre formelle :",id(trajectoire))
        print(f"Identifiant paramètre formel: robot : {id(robot)} ")
    if (not isinstance(trajectoire,list))or(not isinstance(robot,dict)):
        print("Erreur: le paramètre n'est pas un dictionnaire représentant un robot...")
        return
    else:
        for traj in robot["liste_parcours"]:
            if(trajectoire==traj):
                print("La trajectoire existe deja dans la liste des trajectoires du robot...")
                return
        
        robot["liste_parcours"].append(trajectoire)
        print("trajectoire ajoutée à la liste des trajectoires du robot")
        
        
def supprimer_trajectoire(robot,mode_trace):
    if mode_trace:
        print(f"Identifiant paramètre formel: robot : {id(robot)} ")
    if (not isinstance(robot,dict)):
        print("Erreur: le paramètre n'est pas un dictionnaire représentant un robot...")
        return
    else:
        for traj in robot["liste_parcours"]:
            robot["liste_parcours"].remove(traj)
        print("tous les trajectoires ont été supprimés de la liste des trajectoires du robot")
        
        
        
        
####################################################################################
# SOUS-PROGRAMMES DE GESTION DE LA MISSION DU ROBOT             ####################
#                                                               ####################
# definir_mission_robot donnée ci-après pour définir le robot   ####################
# et la trajectoire à effectuer lors de la mission              ####################
#                                                               ####################
# valider_position pour lisser les petites différences < delta  ####################
# entre la position courante et la positions attendue           ####################
####################################################################################



def definir_mission_robot(piece,mode_trace):

    # Caractéristiques du robot à utiliser
    robot = {"nom": "r2d2", "couleur": "red", "largeur_trait": 3, "orientation": 0,
             "position": None, "liste_parcours": []}

    # Définition de la trajectoire
    trajectoire = [{"depart": (207,62), "direction": 2, "distance": 100, "arrivee": None},
                   {"depart": (107,62), "direction": 1, "distance": 50, "arrivee": None},
                   {"depart": (107,112), "direction": 2, "distance": 207, "arrivee": None},
                   {"depart": (-100,112), "direction": 3, "distance": 100, "arrivee": None},
                   {"depart": (-100,12), "direction": 0, "distance": 100, "arrivee": None}]

    ajouter_trajectoire(robot, trajectoire, mode_trace)

    nb_ouvertures = len(piece["liste_ouvertures"])
    if nb_ouvertures != 0:
        ouverture_entree = piece["liste_ouvertures"][0]
        X_robot_depart = ouverture_entree["position"][0]
        Y_robot_depart = ouverture_entree["position"][1]
        X_robot_depart = X_robot_depart + 50
        Y_robot_depart = Y_robot_depart + ouverture_entree["largeur"] / 2

        robot["position"] = (X_robot_depart, Y_robot_depart)
        print("\n Position robot :",robot["position"])

        robot["orientation"] = 2
    return robot




def valider_position(ref_position_courante, ref_debut_segment, delta):
    x1, y1 = ref_position_courante
    print("TRACE x1 y1 = ", x1, y1)
    x2, y2 = ref_debut_segment["depart"]
    print("TRACE x2, y2 = ", x2, y2)

    validite_OK = abs(x1 - x2) <= delta and abs(y1 - y2) <= delta
    return validite_OK

####################################################################################
# à compléter avec                                              ####################
# modifier_orientation, positionner_robot, exécuter_trajectoire ####################

def modifier_orientation(robot, nouvelle_orientation):
    
    if (not isinstance(robot,dict)):
        print("Erreur: le paramètre n'est pas un dictionnaire représentant un robot...")
        return
    else:
        if (nouvelle_orientation in [0, 1, 2, 3]):
            if(tl.heading()!= float(nouvelle_orientation*90)):
                tl.setheading(nouvelle_orientation*90)
                robot["orientation"] = nouvelle_orientation
                print("Orientation du robot modifiée avec succès...")
            else:
                print("L'orientation du robot est déjà la même que la nouvelle orientation...")
            
        else:
            print("Erreur: la nouvelle orientation n'est pas valide...")
            
def positionner_robot(robot,piece):
    if (not isinstance(robot,dict)):
        print("Erreur: le paramètre n'est pas un dictionnaire représentant un robot...")
        return
    else:
        tl.up()
        tl.goto(robot["position"])

        # Orientation absolue
        tl.setheading(robot["orientation"] * 90)

        tl.down()
        
def executer_trajectoire(robot, piece,mode_trace):
    if mode_trace:
        print("ID parametre formelle robot :",id(robot))
        print(f"Identifiant paramètre formel: piece = {piece} : {id(piece)} ")
    
    if not isinstance(robot, dict) or not isinstance(piece, dict):
        print("Erreur : robot ou pièce invalide.")
        return
    
    c = False
    marge = 5
    distance_max = 10
    #positionner au niveau de la première ouverture de la pièce
    robot["position"] = (piece["liste_ouvertures"][0]["position"][0]+10, piece["liste_ouvertures"][0]["position"][1]+20)
    for ouverture in piece["liste_ouvertures"]:
        x_robot, y_robot = robot["position"]
        x_ouv, y_ouv = ouverture["position"]
        largeur = ouverture["largeur"]
        coin = ouverture["coins_mur_ouverture"]

        if coin in (piece["coins_piece"][0], piece["coins_piece"][2]):
            y_min = min(y_ouv, y_ouv - largeur)
            y_max = max(y_ouv, y_ouv - largeur)

            if not (
                y_min + marge <= y_robot <= y_max - marge
                and abs(x_robot - x_ouv) <= distance_max
            ):
                c = True
                break
        else:
            x_min = min(x_ouv, x_ouv - largeur)
            x_max = max(x_ouv, x_ouv - largeur)

            if not (
                x_min + marge <= x_robot <= x_max - marge
                and abs(y_robot - y_ouv) <= distance_max
            ):
                c = True
                break

    if not c:
        print("Erreur : le robot n'est pas devant une ouverture.")
        return

    for trajectoire in robot["liste_parcours"]:
        for segment in trajectoire:

            # Lire la position réelle de la tortue
            positionner_robot(robot,piece)
            position_actuelle = tuple(tl.pos())

            if not valider_position(position_actuelle, segment, marge):
                print("Position non valide")
                return

            depart = segment["depart"]
            direction = segment["direction"]
            distance = segment["distance"]

            # Positionner le robot au départ validé
            tl.up()
            tl.color(robot["couleur"])
            tl.goto(depart)
            robot["position"] = depart

            # Définir l'orientation
            modifier_orientation(robot, direction)
            tl.down()
            # Exécuter le déplacement
            tl.forward(distance)

            # Enregistrer la position réelle d'arrivée
            position_arrivee = tuple(tl.pos())
            robot["position"] = position_arrivee
            segment["arrivee"] = position_arrivee

            print("Arrivée du segment :", position_arrivee)
        

########################################################################
# PROGRAMME PRNCIPAL A EXECUTER                     ####################
########################################################################

mode_trace = True             # permet d'activer ou désactiver le mode trace
                              # modifier vos codes en conséquence pour que 
                              # les messages de trace s'affichent ou pas suivant le cas

environnement = initialiser_environnement(mode_trace)

if mode_trace :
        print('TRACE =', environnement)  # S'affiche uniquement si le mode trace est actif

afficher_info_environnement(environnement, mode_trace)

tracer_environnement(environnement, mode_trace)

robot = definir_mission_robot(environnement,mode_trace)

executer_trajectoire(robot, environnement, mode_trace)




#END