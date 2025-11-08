#Task 3 

import random
import string

target = "HELLOGA123"
pop_size = 50
generations = 20
chromosome_length = len(target)
mutation_rate = 0.05
crossover_rate = 0.8
tournament_size = 3
charset = string.ascii_uppercase + string.digits

def random_string():
    return ''.join(random.choice(charset) for _ in range(chromosome_length))

def fitness(chromo):
    match_count = 0
    for i in range(chromosome_length):
        if chromo[i] == target[i]:
            match_count += 1
    return match_count

def tournament_selection(pop):
    selected = []
    for _ in range(2):
        contestants = random.sample(pop, tournament_size)
        best = max(contestants, key=fitness)
        selected.append(best)
    return selected

def crossover(parent1, parent2):
    if random.random() < crossover_rate:
        point1 = random.randint(1, chromosome_length - 2)
        point2 = random.randint(point1 + 1, chromosome_length - 1)
        child1 = parent1[:point1] + parent2[point1:point2] + parent1[point2:]
        child2 = parent2[:point1] + parent1[point1:point2] + parent2[point2:]
        return child1, child2
    else:
        return parent1, parent2

def mutate(chromo):
    mutated = ""
    for ch in chromo:
        if random.random() < mutation_rate:
            mutated += random.choice(charset)
        else:
            mutated += ch
    return mutated

def genetic_algorithm():
    population = [random_string() for _ in range(pop_size)]

    for gen in range(1, generations + 1):
        new_population = []
        fitness_scores = [fitness(ind) for ind in population]

        max_fit = max(fitness_scores)
        avg_fit = sum(fitness_scores) / pop_size

        print(f"Generation {gen}: Max Fitness = {max_fit}, Average Fitness = {avg_fit:.2f}")

        while len(new_population) < pop_size:
            parent1, parent2 = tournament_selection(population)
            child1, child2 = crossover(parent1, parent2)
            child1 = mutate(child1)
            child2 = mutate(child2)
            new_population.extend([child1, child2])

        population = new_population[:pop_size]

    best_individual = max(population, key=fitness)
    print(f"\nBest match after {generations} generations: {best_individual}")
    print(f"Fitness: {fitness(best_individual)}")

genetic_algorithm()