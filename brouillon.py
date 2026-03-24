import random 
import time 

#1. CLASSE SPECIES
# Représente une espèce avec ses caractéristiques biologiques
class Species:
    def __init__(self, name, reproduction_rate, lifespan, diet=None, predation_rate=0.0):
        self.name = name  # Nom de l'espèce
        self.reproduction_rate = reproduction_rate  # Probabilité de reproduction par jour
        self.lifespan = lifespan  # Durée de vie maximale
        self.diet = diet if diet is not None else []  # Liste des espèces que cet animal peut manger
        self.predation_rate = predation_rate  # Probabilité de réussir une chasse

    def __str__(self):
        return f"{self.name}"


#2. CLASSE INDIVIDUAL
# Représente un individu appartenant à une espèce
class Individual:
    def __init__(self, species):
        self.species = species
        self.age = 0
        self.is_alive = True
        self.a_mange = False  # Indique si l'individu a mangé pendant la journée
        self.hunger = 0  # Compteur de faim

    # Vieillissement de l'individu
    def vieillir(self):
        self.age += 1
        # Mort naturelle si l'âge dépasse la durée de vie
        if self.age >= self.species.lifespan:
            self.is_alive = False

    # Tentative de reproduction
    def reproduire(self):
        if self.is_alive:
            # La reproduction dépend d'une probabilité
            if random.random() < self.species.reproduction_rate:
                return Individual(self.species)
        return None
    
    # Tentative de chasse
    def manger(self, available_prey):
        # Si l'individu est mort ou s'il n'a pas de régime alimentaire
        if not self.is_alive or not self.species.diet:
            return

        # Vérifie si l'animal tente de chasser aujourd'hui
        if random.random() < self.species.predation_rate:
            proies_possibles = []

            # Recherche des proies disponibles dans la population
            for ind in available_prey:
                if ind.is_alive and ind.species.name in self.species.diet:
                    proies_possibles.append(ind)
    
            # Si une proie est trouvée, elle est tuée
            if proies_possibles:
                victime = random.choice(proies_possibles)
                victime.is_alive = False
                self.a_mange = True
        

#3. LE MOTEUR (Ecosystem)
# Gère l'ensemble de la simulation et la population
class Ecosystem:
    def __init__(self):
        self.population = [] 

    # Ajoute plusieurs individus d'une espèce dans l'écosystème
    def add_population(self, species, count):
        for _ in range(count):
            self.population.append(Individual(species))

    # Simule une journée dans l'écosystème
    def run_day(self):
        
        time.sleep(1.5)  # Pause pour ralentir l'affichage

        new_babies = []  # Liste des nouveaux individus
        
        # Mélange la population pour éviter un ordre fixe d'action
        random.shuffle(self.population)

        # Réinitialisation du statut "a mangé"
        for individual in self.population:
            individual.a_mange = False

        #Phase 1 : Actions des individus
        for individual in self.population:

            if not individual.is_alive:
                continue

            # Vieillissement
            individual.vieillir()

            # S'il meurt de vieillesse, il ne peut plus agir
            if not individual.is_alive: 
                continue

            # Tentative de chasse
            individual.manger(self.population)

            # Tentative de reproduction
            bebe = individual.reproduire()

            if bebe:
                compteur = 0

                # Compte combien d'individus de cette espèce sont vivants
                for ind in self.population:
                    if ind.species.name == bebe.species.name and ind.is_alive:
                        compteur += 1

                # Limite de population pour éviter une explosion démographique
                if compteur < 200:
                    new_babies.append(bebe)

                    # Gestion de la faim (uniquement pour les prédateurs)
                    if individual.species.diet:
                        if individual.a_mange:
                            individual.hunger = 0
                        else:
                            individual.hunger += 1

                            # Mort si l'animal ne mange pas pendant trop longtemps
                            if individual.hunger >= 5:
                                individual.is_alive = False


        #Phase 2 : Nettoyage de la population

        liste_des_survivants = [] 

        # On conserve uniquement les individus encore vivants
        for ind in self.population:
            if ind.is_alive: 
                liste_des_survivants.append(ind)
        
        # On ajoute les nouveaux individus nés ce jour
        self.population = liste_des_survivants + new_babies


    # Affiche les statistiques de population par espèce
    def print_stats(self):
        stats = {}
        for ind in self.population:
            name = ind.species.name
            stats[name] = stats.get(name, 0) + 1
        print("Population:", stats)


#ONFIGURATION ET LANCEMENT

# Définition des espèces et de leurs caractéristiques
plante = Species("Plante", 0.25, 50, [])
insecte = Species("Insecte", 0.18, 20, ["Plante"], 0.5)
souris = Species("Souris", 0.12, 30, ["Plante"], 0.4)
lapin = Species("Lapin", 0.10, 35, ["Plante"], 0.4)
grenouille = Species("Grenouille", 0.08, 35, ["Insecte"], 0.5)
serpent = Species("Serpent", 0.05, 60, ["Grenouille", "Souris"], 0.35)
loup = Species("Loup", 0.02, 90, ["Lapin"], 0.25)
aigle = Species("Aigle", 0.01, 120, ["Serpent", "Souris"], 0.2)

# Création de l'écosystème
monde = Ecosystem()

# Population initiale
monde.add_population(plante, 120)
monde.add_population(insecte, 30)
monde.add_population(souris, 20)
monde.add_population(lapin, 15)
monde.add_population(grenouille, 10)
monde.add_population(serpent, 6)
monde.add_population(loup, 3)
monde.add_population(aigle, 2)

#Lancement de la simulation

print("DÉBUT DE LA SIMULATION")
monde.print_stats()

# Simulation sur plusieurs jours
for jour in range(1, 200):
    print(f"\nJOUR {jour} :")
    monde.run_day()
    monde.print_stats()