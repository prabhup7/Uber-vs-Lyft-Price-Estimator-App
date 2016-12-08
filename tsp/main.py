import tsp, euclidean

print "Initialising"
ox = "OX"
edge_recombination = "EDGERECOMBINATION"

# #initialize class
# tsp = tsp.TSP()

# #Set file name
# tsp.file_name = "tspadata2.txt"

# #read file
# tsp.read_file()

# #set number of parents
# tsp.population_size = 1000

# #Create population
# tsp.create_population()

# #Calcuate the crossover points
# tsp.calc_crossover_point()

# #calculate fitness
# tsp.fitness()

# while tsp.generation < 1000:
#   tsp.evaluate_generation(edge_recombination)
#   print ("Generation %d") % (tsp.generation)

# soln = tsp.optimal_solution()
# print ("%d -> %d - > %s") % (tsp.generation, soln[0], soln[1])

#initialize class
euc = euclidean.Euclidean()

#set grid size
euc.grid_size = 50

#create euclidean space
euc.create_euclidean_space()

#set size of population
euc.population_size = 20

#create population
euc.create_population()

#calculate crossover points
euc.calc_crossover_points()

#calculate fitness
euc.fitness()

while euc.generation < 1000:
  euc.evaluate_generation(edge_recombination)
  print ("Generation %d") % (euc.generation)
  # soln = euc.optimal_solution()
  # print ("%d -> %d - > %s") % (euc.generation, soln[0], soln[1])

soln = euc.optimal_solution()
print ("%d -> %d - > %s") % (euc.generation, soln[0], soln[1])