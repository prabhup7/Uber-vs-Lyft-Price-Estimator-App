import random
from itertools import groupby

#Gets edges for parent1, parent2
def find_edges(parent1, parent2):
  parent1_edges = calc_edges(parent1)
  parent2_edges = calc_edges(parent2)
  merged_edges = merge_edges(parent1_edges, parent2_edges)  

  return (parent1_edges, parent2_edges, merged_edges)

#calculates edges for an individual
def calc_edges(individual):
  edges = []
  
  for position in xrange(len(individual)):
    if position == 0:
      edges.append([individual[position], (individual[-1], individual[position+1])])
    elif position < len(individual)-1:
      edges.append([individual[position], (individual[position-1], individual[position+1])])
    else:
      edges.append([individual[position], (individual[position-1], individual[0])])
  
  return edges

#sort the edges    
def sort_edges(individual):
  individual.sort(lambda x, y: cmp(x[0],y[0]))

#perform an union on two parents
def merge_edges(parent1, parent2):
  sort_edges(parent1)
  sort_edges(parent2)

  edges = []
  for val in xrange(len(parent1)):
    edges.append([parent1[val][0], union(parent1[val][1], parent2[val][1])])
  
  return edges

#part of merge_edges - unions 2 individual
def union(individual1, individual2):
  edges = list(individual1)

  for val in individual2:
    if val not in edges:
      edges.append(val)
  return edges

#Edge recombination operator - http://en.wikipedia.org/wiki/Edge_recombination_operator
def crossover(parent1, parent2, edges):
  k = []
  previous = None
  current = random.choice([parent1[0], parent2[0]])

  while True:
    k.append(current)

    if(len(k) == len(parent1)):
      break
    
    previous = remove_node_from_neighbouring_list(current, edges)
    current_neighbour = get_current_neighbour(previous, edges)

    next_node = None
    if len(current_neighbour) > 0:
      next_node = get_best_neighbour(current_neighbour)
    else:
      next_node = get_next_random_neighbour(k, edges)
   
    current = next_node[0]
  return k
  
#returns the best possible neighbour
def get_best_neighbour(neighbour):
  if len(neighbour) is 1:
    return neighbour[0]
  else:
    group_neighbour = group_neighbours(neighbour)
    return random.choice(group_neighbour[0])[1]

#part of get_best_neighbour   
def group_neighbours(neighbours):
  sorted_neighbours = []

  #store length of each individual neighbour + neighbour in a list
  for neighbour in neighbours:
    sorted_neighbours.append((len(neighbour[1]), neighbour))
  
  #sort the new list
  sort_edges(sorted_neighbours)

  #group the neighbour by their size
  groups = []
  for k, g in groupby(sorted_neighbours, lambda x: x[0]):
    groups.append(list(g))

  return groups

#returns a random neighbour from remaining_edges that does not exist in current_path
def get_next_random_neighbour(current_path, remaining_edges):
  random_node = None

  while random_node is None:
    tmp_node = random.choice(remaining_edges)

    if tmp_node[0] not in current_path:
      random_node = tmp_node
  
  return random_node
    
# removes node from neighbouring list
def remove_node_from_neighbouring_list(node, neighbour_list):
  removed_node = None

  for n in neighbour_list:
    if n[0] == node:
      removed_node = n
      neighbour_list.remove(n)
    
    if node in n[1]:
      n[1].remove(node)
  
  return removed_node
    
#return neighbours for a give node(s)
def get_current_neighbour(nodes, neighbour_lists):
  neighbours = []

  if nodes is not None:
    for node in nodes[1]:
      for neighbour in neighbour_lists:
        if node == neighbour[0]:
          neighbours.append(neighbour)

  return neighbours