# Projet Coding Weeks Groupe 18

## Nom
**Diffusion thermique en régime transitoire.**

## Description
Notre projet aura pour but de visualiser, dans différents cas, l'évolution de la température dans un ou des matériaux soumis à un thermostat. On modélisera d'abord le cas unidimensionnel, puis le cas bidimensionnel. Une interface graphique permettra ensuite de choisir le cas que l'on souhaite, et de fixer les différents paramètres du problème.

## Le problème abordé
### Régime transitoire en 1D
+ Cartésien

> On ne développera pas la discrétisation et la résolution de ces problèmes car ils ne représentent pas la plus grande partie de notre travail, et une version plus générale (2D) est présentée ensuite.
### Régime transitoire en 2D
+ Cartésien :  

On s'intéresse à un plan, repéré en ordonnée par la coordonnée _y_ et en abcisse par la coordonnée _x_, traduit informatiquement par les indices i et j  
On rappelle l'équation de la chaleur dans le cas général 

<img src = "https://gitlab-cw3.centralesupelec.fr/alexian.helaine/project-coding-weeks-group-18/-/raw/main/Images/CodeCogsEqn.gif?ref_type=heads"/>  

avec:  
 <img src = "https://gitlab-cw3.centralesupelec.fr/alexian.helaine/project-coding-weeks-group-18/-/raw/main/Images/S.png?ref_type=heads">  
Dans le cas 2D, on obtient: 
<img src = "https://gitlab-cw3.centralesupelec.fr/alexian.helaine/project-coding-weeks-group-18/-/raw/main/Images/2dcartesien.png?ref_type=heads">

Après discrétisation, on a :
<img src = "https://gitlab-cw3.centralesupelec.fr/alexian.helaine/project-coding-weeks-group-18/-/raw/main/Images/discetisation.png?ref_type=heads">

Et on a besoin de préciser deux types de conditions, à savoir les conditions aux limites: 
<img src = "https://gitlab-cw3.centralesupelec.fr/alexian.helaine/project-coding-weeks-group-18/-/raw/main/Images/T(0,y,t).png?ref_type=heads">, <img src = "https://gitlab-cw3.centralesupelec.fr/alexian.helaine/project-coding-weeks-group-18/-/raw/main/Images/T(x,0,t).png?ref_type=heads">
ainsi que les conditions initiales en tous les autres points: <img src = "https://gitlab-cw3.centralesupelec.fr/alexian.helaine/project-coding-weeks-group-18/-/raw/main/Images/T(x,y,0).png?ref_type=heads">

Alors découle l'implémentation du fichier [modelisation2d.py](modelisation thermique/modelisation_2D.py)

<img src = "https://gitlab-cw3.centralesupelec.fr/alexian.helaine/project-coding-weeks-group-18/-/raw/main/Images/cart%C3%A9sien.png">

_Un exemple de profil spatial de température_

+ Cylindrique : analogue au cas cartésien, avec l'équation de la chaleur 2d associée (rayon et hauteur ou rayon et angle)

<img src = "https://gitlab-cw3.centralesupelec.fr/alexian.helaine/project-coding-weeks-group-18/-/raw/main/Images/Capture_d_%C3%A9cran_2023-11-24_083307.png">

_Un exemple de profil de température dans un cylindre avec une température dépendant de r et de z_

## Installation
> Notre code nécessite l'installation des librairies [matplotlib](https://matplotlib.org/), [numpy](https://numpy.org/), [scipy](https://www.scipy.org/) et TKinter

## Organisation du projet

### Objectif 1 (MVP) Création d'une interface graphique et diffusion thermique en 1D
Notre premier objectif était d'avoir une interface simple, ergonomique, nous permettant de visualiser la diffusion thermique s'effectuant dans un matériau, dans le cas simplificateur d'un objet unidimensionnel cylindrique ou cartésien. 
+ __Sprint 0 :__  

    + Analyse des objectifs et besoins

+ __Sprint 1 : Résolution numérique du problème__

    + Modélisation physique du problème
    + __Fonctionnalité 1 :__ implémentation et résolution de l’équation de la chaleur en régime transitoire en 1D
    + __Fonctionnalité 2 :__ visualisation au cours du temps
    + __Fonctionnalité 3 :__ Permettre d'avoir plusieurs matériaux sur la même simulation

+ __Sprint 2: Une interface graphique basique__
    + __Fonctionnalité 4 :__ Visualisation de l'animation et des matériaux sur l'interface graphique
    + __Fonctionnalité 5 :__ Permettre à l'utilisateur de changer les paramètres de la simulation

### Objectif 2 : Passage à la 2D 
On a donc réussi à avoir un code viable, pour des objets unidimensionnels. C'est un premier pas, mais peu de problèmes peuvent se résoudre avec ce type de modèles.
Ainsi, nous allons faire un premier pas vers une meilleure représentation de la réalité en passant à des objets bidimensionnels.

+ __Sprint 3 : Résolution numérique... en 2D__

    + Modélisation physique du problème
    + __Fonctionnalité 6 :__ implémentation et résolution de l’équation de la chaleur en régime transitoire en 2D
        + cartésien
        + cylindrique

+ __Sprint 4 : Visualisation d'un problème à 3 variables__
S'il était assez aisé de tracer la température en fonction d'une variable sur un plan avec matplotlib, on a désormais 2 variables spatiales, une variable de temps et on doit pouvoir visualiser la température pour chaque combinaison de chacune de ces variables.
Nous avons alors fait le choix de représenter les résultats sous forme d'une carte de chaleur à chaque instant.

    + __Fonctionnalité 7 :__ Une carte instantanée de la chaleur 
    + __Fonctionnalité 8 :__ Animation de la carte 

+ __Sprint 5 : Adaptation de l'interface graphique aux nouvelles fonctionnalités__
    + __Fonctionnalité 9 :__ Ajout de nouvelles fenêtres et interactions utilisateurs (conditions aux limites, source de chaleur interne)

### Objectif 3 : Un produit plus ergonomique et une gamme plus large d'utilisations
+ __Sprint 6 : Extension des possibilités pour l'utilisateur__

    + __Fonctionnalité 10 :__ Evolution de la température aux interfaces variable
    + __Fonctionnalité 11 :__ Ajout de plusieurs sources de chaleurs
    + __Fonctionnalité 12 :__ Possibilité de créer une source en cliquant sur le lieu de cette dernière
    + __Fonctionnalité 13 :__ Intégration de matériaux réels à choisir avec un menu déroulant

### Jalons  

_Jalon 1 :_ Résolution de l'équation de la chaleur 1D  
_Jalon 2 :_ Représentation de la température 1D  
_Jalon 2 :_ Prise en compte de plusieurs matériaux  
_Jalon 3 :_ Résolution de l'équation de la chaleur 2D en cylindrique  
_Jalon 4 :_ Résolution de l'équation de la chaleur 2D en cartésien  
_Jalon 5 :_ Possibilité de visualiser et interagir avec la simulation 2D   
_Jalon 6 :_ Ajout de fonctionnalités supplémentaires  


## Auteurs
+ Eddamiri Adam
+ Jean-Baptiste Senet
+ Louis Sender
+ Erwann Henon
+ Titouan Boutreux
+ Alexian Hélaine
