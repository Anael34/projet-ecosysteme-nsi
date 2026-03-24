# Simulation d'Écosystème

## Description

Ce projet est une **simulation d'écosystème en Python** qui modélise
l'évolution de différentes espèces au fil du temps.

Chaque individu peut : - vieillir - se reproduire - chasser (s'il est
prédateur) - mourir (de vieillesse ou de faim)

La simulation évolue **jour après jour** et affiche l'état des
populations dans la console.

------------------------------------------------------------------------

# Installation

## Prérequis

Vous devez avoir **Python 3** installé.

Vérifier l'installation :

``` bash
python --version
```

ou

``` bash
python3 --version
```

------------------------------------------------------------------------

# Protocole d'utilisation

## 1. Lancer le programme

Dans le terminal, se placer dans le dossier du projet puis exécuter :

``` bash
python index.py
```

ou

``` bash
python3 index.py
```

------------------------------------------------------------------------

## 2. Démarrage de la simulation

Au lancement, le programme :

1.  crée un **écosystème**
2.  initialise une **population de départ**
3.  démarre la simulation

Exemple :

    DÉBUT DE LA SIMULATION
    Population: {'Plante': 120, 'Insecte': 30, 'Souris': 20}

------------------------------------------------------------------------

## 3. Déroulement d'une journée

Chaque jour simulé :

1.  les individus **vieillissent**
2.  les prédateurs **chassent**
3.  les individus **tentent de se reproduire**
4.  les animaux qui ne mangent pas peuvent **mourir de faim**
5.  les individus morts sont **retirés**
6.  les nouveaux individus **naissent**

------------------------------------------------------------------------

## 4. Lecture des résultats

Après chaque jour, le programme affiche le nombre d'individus par
espèce.

Exemple :

    JOUR 10 :
    Population: {'Plante': 140, 'Insecte': 25, 'Souris': 18, 'Lapin': 12}

------------------------------------------------------------------------

# Limite de population

Afin d'éviter une explosion démographique, chaque espèce est limitée à
**200 individus maximum**.

------------------------------------------------------------------------

# Arrêter la simulation

La simulation s'arrête automatiquement après **un jours**.

Vous pouvez aussi arrêter le programme avec :

    CTRL + C

dans le terminal.
