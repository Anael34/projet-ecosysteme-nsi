import random 
import time 

# --- 1. CLASSE SPECIES ---
class Species:
    def __init__(self, name, reproduction_rate, lifespan, diet=None, predation_rate=0.0):
        self.name = name
        self.reproduction_rate = reproduction_rate
        self.lifespan = lifespan
        self.diet = diet if diet is not None else []
        self.predation_rate = predation_rate

    def __str__(self):
        return f"{self.name}"

# --- 2. CLASSE INDIVIDUAL ---
class Individual:
    def __init__(self, species):
        self.species = species
        self.age = 0
        self.is_alive = True
        self.a_mange = False
        self.hunger=0

    def vieillir(self):
        self.age += 1
        if self.age >= self.species.lifespan:
            self.is_alive = False

    def reproduire(self):
        if self.is_alive:
            if random.random() < self.species.reproduction_rate:
                return Individual(self.species)
        return None
    
    def manger(self, available_prey):
        if not self.is_alive or not self.species.diet:
            return

        if random.random() < self.species.predation_rate:
            proies_possibles = []

            for ind in available_prey:
                if ind.is_alive and ind.species.name in self.species.diet:
                    proies_possibles.append(ind)
    
            if proies_possibles:
                victime = random.choice(proies_possibles)
                victime.is_alive = False
                self.a_mange = True
        
# --- 3. LE MOTEUR (Ecosystem) ---
class Ecosystem:
    def __init__(self):
        self.population = [] 

    def add_population(self, species, count):
        for _ in range(count):
            self.population.append(Individual(species))

    def run_day(self):
        
        time.sleep(1.5)

        new_babies = []
        
        random.shuffle(self.population)

        for individual in self.population:
            individual.a_mange = False

        # --- Phase 1 : Action (Vieillir, Manger, Reproduire) ---
        for individual in self.population:
            if not individual.is_alive:
                continue

            individual.vieillir()
            if not individual.is_alive: 
                continue # S'il meurt de vieillesse, il ne mange pas

            individual.manger(self.population)

            bebe = individual.reproduire()
            if bebe:
                compteur = 0

                for ind in self.population:
                    if ind.species.name == bebe.species.name and ind.is_alive:
                        compteur += 1

                if compteur < 200:
                    new_babies.append(bebe)

                    if individual.species.diet:   # seulement les animaux
                        if individual.a_mange:
                            individual.hunger = 0
                        else:
                            individual.hunger += 1
                            if individual.hunger >= 5:
                                individual.is_alive = False

        # --- Phase 2 : Nettoyage (VERSION "VIEILLE ÉCOLE") ---
        # C'est ici que j'ai changé le code pour le rendre plus lisible
        
        liste_des_survivants = [] 

        # On parcourt toute la population actuelle
        for ind in self.population:
            # Si "ind" (l'individu) est vivant, on le garde
            if ind.is_alive: 
                liste_des_survivants.append(ind)
        
        # On ajoute les bébés aux survivants
        # (On fusionne les deux listes)
        self.population = liste_des_survivants + new_babies

    def print_stats(self):
        stats = {}
        for ind in self.population:
            name = ind.species.name
            stats[name] = stats.get(name, 0) + 1
        print("Population:", stats)

# --- CONFIGURATION ET LANCEMENT ---

# Définition des espèces
plante = Species("Plante", 0.25, 50, [])
insecte = Species("Insecte", 0.18, 20, ["Plante"], 0.5)
souris = Species("Souris", 0.12, 30, ["Plante"], 0.4)
lapin = Species("Lapin", 0.10, 35, ["Plante"], 0.4)
grenouille = Species("Grenouille", 0.08, 35, ["Insecte"], 0.5)
serpent = Species("Serpent", 0.05, 60, ["Grenouille", "Souris"], 0.35)
loup = Species("Loup", 0.02, 90, ["Lapin"], 0.25)
aigle = Species("Aigle", 0.01, 120, ["Serpent", "Souris"], 0.2)

# Création du monde
monde = Ecosystem()
monde.add_population(plante, 120)
monde.add_population(insecte, 30)
monde.add_population(souris, 20)
monde.add_population(lapin, 15)
monde.add_population(grenouille, 10)
monde.add_population(serpent, 6)
monde.add_population(loup, 3)
monde.add_population(aigle, 2)

# Simulation
print("--- DÉBUT DE LA SIMULATION ---")
monde.print_stats()

for jour in range(1, 200):
    print(f"\n--- JOUR {jour} ---")
    monde.run_day()
    monde.print_stats()
