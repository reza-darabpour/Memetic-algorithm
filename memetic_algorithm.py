import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# parameters
population_size = 10
mutation_rate=0.7
generations = 120
MIN_points=[]

# Rastrigin function
def rastrigin(X):
    x, y = X
    return 10 * 2 +( x**2 - 10 * np.cos(2 * np.pi * x)) + (y**2 - 10 * np.cos(2 * np.pi * y))


# creating first population
def initialize_population(size):
    return np.random.uniform(-6, 6, (size, 2))

# fitness
def fitness(population):
    return np.array([(rastrigin(individual)) for individual in population])

#crossover
def crossover(parent1, parent2):
    if np.random.rand() < 0.7:
        return np.concatenate((parent1[:1], parent2[1:]))
    return parent1

#mutation

def mutate(child, rate=mutation_rate):
    if np.random.rand() < rate:
        idx = np.random.randint(len(child))
        child[idx] += np.random.uniform(-1, 1)
    return child

# Hill Climbing
  
def local_search(individual, step_size=0.01, max_iters=100):
    current = individual
    current_fitness = rastrigin(current)
    
    for i in range(max_iters):
        # creating neighbors points
        neighbors = [
            current + np.array([step_size, 0]),
            current + np.array([-step_size, 0]),
            current + np.array([0, step_size]),
            current + np.array([0, -step_size])
        ]
        
        #evaluate neighbors fitness
        neighbor_fitness = [rastrigin(neighbor) for neighbor in neighbors]
        
        #best  neighbor  
        min_fitness_index = np.argmin(neighbor_fitness)
        best_neighbor = neighbors[min_fitness_index]
        best_neighbor_fitness = neighbor_fitness[min_fitness_index]
        
        #if best neighbor is better of current move toward
        if best_neighbor_fitness < current_fitness:
            current = best_neighbor
            current_fitness = best_neighbor_fitness
        else:
            #if was not better neighbor break
            break
            
    return current, current_fitness

# finding min point in generation

def min_point(population, fitness_values):

    min_index = np.argmin(fitness_values)
    best_individual = population[min_index]
    
    return best_individual




# memtic algorithm
population = initialize_population(population_size)
print(f'first population : \n{population}')
print('-'*45)

for generation in range(generations):

    fitness_values = fitness(population)
    MIN_points.append(min_point(population, fitness_values))
    new_population = []

    for i in range(0, len(population), 2):
        #selecting
        parent1, parent2 = population[i], population[i+1]
        child1, child2 = crossover(parent1, parent2), crossover(parent2, parent1)
        child1, child2 = mutate(child1), mutate(child2)
        
        child1 = local_search(child1)[0]
        child2 = local_search(child2)[0]
        
        new_population.append(child1)
        new_population.append(child2)

    population = np.array(new_population)

f=fitness(MIN_points)
best_individual=(min_point(MIN_points,f))
best_value=rastrigin(best_individual)

print("Best individual:", best_individual)
print("Best value:", best_value)

# visualization
x = np.linspace(-5, 5, 400)
y = np.linspace(-5, 5, 400)
X, Y = np.meshgrid(x, y)
Z = rastrigin([X, Y])

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap="viridis", edgecolor='k', alpha=0.7)

#visualization global Minimum
ax.scatter(best_individual[0], best_individual[1], best_value, color='r', s=100, label="Global Minimum")

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Rastrigin(X, Y)")
ax.set_title("3D Visualization of Rastrigin Function with Memetic Algorithm Optimization")
ax.legend()

plt.show()

