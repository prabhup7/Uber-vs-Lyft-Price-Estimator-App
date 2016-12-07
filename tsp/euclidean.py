import random, math
import edge_recombination as ero

class Euclidean:
  
  # Initialize the value
  def __init__(self):
    self.euclidean_space = []
    self.population = []

    self.grid_size = 0
    self.generation = 0
    self.population_size = 0

    self.crossover_point = ()
    self.population_cost_matrix = []
    
    self.crossover_probability = 0.7
    self.mutate_probability = 0.05
  
  #create euclidean space
  def create_euclidean_space(self):
    for p in range(0, self.grid_size):
      for q in range (0, self.grid_size):
        self.euclidean_space.append((p,q))
  
  #create initial population
  def create_population(self):
    population = []
    while len(population) < self.population_size:
      population.append(random.sample(self.euclidean_space, len(self.euclidean_space)))
    self.population = population

  # Calculate crossover points - points at which the crossover will occur
  def calc_crossover_points(self):
    crossover_point1 = int(math.floor(self.grid_size/3))
    crossover_point2 = self.grid_size - crossover_point1
    self.crossover_point = (crossover_point1, crossover_point2)

  #calcuates the cost of the journey
  def fitness(self):
    self.population_cost_matrix = []
    for individual in self.population:
      index = 0
      fitness = 0
      while index < len(individual) - 1:
        fitness += float(self.evaluate_cost(individual[index], individual[index+1]))
        index += 1

      fitness += float(self.evaluate_cost(individual[len(individual)-1], individual[0]))
      self.population_cost_matrix.append((fitness, individual))

  def evaluate_cost(self, val1, val2):
    a = (val1[0] - val2[0]) * (val1[0] - val2[0])
    b = (val1[1] - val2[1]) * (val1[1] - val2[1])

    return (a + b) ** 0.5
  
  #Perform probabilistic crossover
  def ox_crossover(self, parent1, parent2):
    pC = random.random()

    if pC <= self.crossover_probability:
      child1 = self.create_child(parent1, parent2)
      child2 = self.create_child(parent2, parent1)
      return (child1, child2)
    else:
      return (parent1, parent2)

  #performs crossover
  def create_child(self, parent1, parent2):
    #get middle of parent
    parent1_chromosomes = parent1[self.crossover_point[0]:self.crossover_point[1]]

    #ordered chromosomes from parent2
    ordered_chromosomes = parent2[self.crossover_point[1]:]
    ordered_chromosomes.extend(parent2[:self.crossover_point[1]])
    
    #remove chromosome which exist in parent1
    parent2_chromosomes = filter(lambda chromosomes: chromosomes not in parent1_chromosomes, ordered_chromosomes)

    #add elements to end of parent
    parent1_chromosomes.extend(parent2_chromosomes[:self.crossover_point[0]-1])
    
    #add elements to front of parent
    elements = parent2_chromosomes[self.crossover_point[0]-1:len(parent2_chromosomes)]
    elements.extend(parent1_chromosomes)

    return elements

  #perform probabilistic mutation 
  def mutate(self, individual):
    pM = random.random()

    if pM <= self.mutate_probability:
      swap_position = random.sample(range(0,len(individual)), 2)
      individual[swap_position[0]], individual[swap_position[1]] = individual[swap_position[1]], individual[swap_position[0]]

  #sort individuals in order of decreasing fitness
  def sort_selection(self, individuals):
    individuals.sort(lambda x, y: cmp(x[0],y[0]))
  
  #create new population, and replace existing one
  def evaluate_generation(self, crossover):
    new_population = []
    self.generation += 1
    
    while len(new_population) < len(self.population):
      
      #tournament selection
      individuals = random.sample(self.population_cost_matrix, 10)
      self.sort_selection(individuals)
      lucky_individual1 , lucky_individual2 = individuals[0], individuals[1]

      #perform crossover
      if crossover is "OX":
        children = self.ox_crossover(lucky_individual1[1], lucky_individual2[1])
        
        #perform mutate
        for child in children:
          self.mutate(child)
          
          #add children to new population
          new_population.append(child)

      elif crossover is "EDGERECOMBINATION":
        #perform probabilistic crossover
        pC = random.random()

        if pC <= self.crossover_probability:
          matrix = ero.find_edges(lucky_individual1[1], lucky_individual2[1])
          child = ero.crossover(lucky_individual1[1], lucky_individual2[1], matrix[2])

          #perform mutate
          self.mutate(child)
        
          #add children to new population
          new_population.append(child)

        else:

          #mutate parent
          self.mutate(lucky_individual1[1])
          self.mutate(lucky_individual2[1])

          #add parent to new population
          new_population.append(lucky_individual1[1])
          new_population.append(lucky_individual2[1])


    #replace old population with new population
    self.population = new_population
    self.fitness()
  
  #returns the optimal solution
  def optimal_solution(self):
    self.sort_selection(self.population_cost_matrix)
    return self.population_cost_matrix[0]
