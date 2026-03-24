# Présentation du projet : Simulation d'un écosystème en Python

## Objectif du projet

Ce projet consiste à créer une **simulation d'écosystème** en Python.
L'objectif est de modéliser les interactions entre différentes espèces
vivantes au sein d'un environnement : reproduction, prédation,
vieillissement et mortalité.

La simulation évolue **jour après jour**, en mettant à jour la
population de chaque espèce selon des règles biologiques simplifiées.

------------------------------------------------------------------------

## Principe général

L'écosystème est composé de plusieurs espèces animales et végétales.
Chaque individu possède des caractéristiques biologiques et agit chaque
jour selon différentes règles :

-   Vieillir
-   Se reproduire
-   Manger (prédation)
-   Mourir (vieillesse ou faim)

La simulation permet d'observer **l'évolution des populations dans le
temps**.

------------------------------------------------------------------------

## Structure du programme

Le programme repose sur **trois classes principales**.

### 1. Classe `Species`

Cette classe représente une **espèce biologique**.

Chaque espèce possède plusieurs caractéristiques :

-   `name` : nom de l'espèce
-   `reproduction_rate` : probabilité de reproduction par jour
-   `lifespan` : durée de vie maximale
-   `diet` : liste des espèces pouvant être consommées
-   `predation_rate` : probabilité de réussite d'une chasse

Cette classe sert de **modèle biologique** pour tous les individus
appartenant à l'espèce.

------------------------------------------------------------------------

### 2. Classe `Individual`

Cette classe représente **un individu vivant** dans l'écosystème.

Chaque individu possède :

-   une **espèce**
-   un **âge**
-   un **état de vie (vivant ou mort)**
-   un **niveau de faim**

Un individu peut :

-   **vieillir**
-   **se reproduire**
-   **chasser et manger**

La reproduction crée **un nouvel individu de la même espèce**. La chasse
permet à un prédateur de **tuer une proie appartenant à son régime
alimentaire**.

Un prédateur qui ne mange pas pendant **plusieurs jours consécutifs
meurt de faim**.

------------------------------------------------------------------------

### 3. Classe `Ecosystem`

Cette classe représente **le moteur de la simulation**.

Elle gère :

-   la **population totale**
-   le **déroulement des journées**
-   les **naissances**
-   la **suppression des individus morts**

Chaque journée se déroule en plusieurs étapes :

1.  Mélange de la population
2.  Vieillissement des individus
3.  Tentatives de chasse
4.  Tentatives de reproduction
5.  Gestion de la faim
6.  Nettoyage des individus morts
7.  Ajout des nouveaux individus

------------------------------------------------------------------------

## Espèces présentes dans la simulation

L'écosystème contient plusieurs niveaux de la **chaîne alimentaire** :

  Espèce       Rôle
  ------------ ------------------------------------
  Plante       Producteur
  Insecte      Consommateur primaire
  Souris       Herbivore
  Lapin        Herbivore
  Grenouille   Prédateur d'insectes
  Serpent      Prédateur de grenouilles et souris
  Loup         Prédateur de lapins
  Aigle        Superprédateur

Chaque espèce possède :

-   un **taux de reproduction**
-   une **durée de vie**
-   un **régime alimentaire**

------------------------------------------------------------------------

## Déroulement de la simulation

Au lancement :

1.  Un **écosystème est créé**
2.  Une **population initiale** est ajoutée
3.  La simulation s'exécute pendant **un certain nombre de jour**

À chaque jour :

-   les actions des individus sont simulées
-   les populations sont mises à jour
-   les statistiques de population sont affichées

Exemple d'affichage :

    JOUR 5 :
    Population: {'Plante': 130, 'Insecte': 28, 'Souris': 19, 'Lapin': 14}

------------------------------------------------------------------------

## Limites de population

Afin d'éviter une **explosion démographique**, une limite de **200
individus maximum par espèce** est appliquée lors des reproductions.

------------------------------------------------------------------------

## Technologies utilisées

-   **Python**
-   Modules standards :
    -   `random` pour les probabilités
    -   `time` pour ralentir l'affichage

------------------------------------------------------------------------

## Intérêt du projet

Ce projet permet de :

-   comprendre les **interactions écologiques**
-   pratiquer la **programmation orientée objet (POO)**
-   manipuler des **simulations probabilistes**
-   observer des **dynamiques de population**

------------------------------------------------------------------------

## Améliorations possibles

Plusieurs améliorations pourraient être ajoutées :

-   ajout d'un **environnement (saisons, climat)**
-   gestion de **ressources limitées**
-   **visualisation graphique** des populations
-   simulation sur une **grille spatiale**
-   interface utilisateur avec choix du nombre de départ d'individus par espèce

------------------------------------------------------------------------

## Conclusion

Ce projet propose une **modélisation simplifiée d'un écosystème**
permettant d'observer l'évolution de différentes espèces au fil du
temps.

Il met en pratique les concepts de **programmation orientée objet**, de
**probabilité** et de **simulation dynamique**, tout en illustrant les
mécanismes fondamentaux de la **chaîne alimentaire**.
