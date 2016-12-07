from lyftfile1 import *

combo = list(itertools.permutations([0,1,3,4,5,6], 6))
#print combo

originallist = [0,1,3,4,5]
start = [originallist[0]]

end  = originallist[-1]

list1 = []

for i in range (1, len(originallist)-1):
 list1.append(originallist[i])


#print list(itertools.permutations(list1, 3))
"""for i in range(0,6):
 routei = list(itertools.permutations(list1, 3))[i]
 print routei"""

route1 = list(itertools.permutations(list1, 3))[0]
route2 = list(itertools.permutations(list1, 3))[1]
route3 = list(itertools.permutations(list1, 3))[2]
route4 = list(itertools.permutations(list1, 3))[3]
route5 = list(itertools.permutations(list1, 3))[4]
route6 = list(itertools.permutations(list1, 3))[5]

print route1

print route2

print route3

print route4

print route5

print route6


---------------------------------------------------------------------------1
routelist1 = []

routelist2 = []

routelist3 = []

routelist4 = []

routelist5 = []

routelist6 = []
#---------------------------------------------------------printing the possible routes
print"The possible routes are:-"

for i in range(0,3):
    routelist1.append(route1[i])
routelist1.insert(0,originallist[0])
routelist1.insert(len(routelist1),originallist[len(originallist)-1])
print routelist1


for i in range(0,3):
    routelist2.append(route2[i])
routelist2.insert(0,originallist[0])
routelist2.insert(len(routelist2),originallist[len(originallist)-1])
print routelist2

for i in range(0,3):
    routelist3.append(route3[i])
routelist3.insert(0,originallist[0])
routelist3.insert(len(routelist3),originallist[len(originallist)-1])
print routelist3

for i in range(0,3):
    routelist4.append(route4[i])
routelist4.insert(0,originallist[0])
routelist4.insert(len(routelist4),originallist[len(originallist)-1])
print routelist4

for i in range(0,3):
    routelist5.append(route5[i])
routelist5.insert(0,originallist[0])
routelist5.insert(len(routelist5),originallist[len(originallist)-1])
print routelist5

for i in range(0,3):
    routelist6.append(route6[i])
routelist6.insert(0,originallist[0])
routelist6.insert(len(routelist6),originallist[len(originallist)-1])
print routelist6


#--------------------------------------Taking into consideration all routes for estimated costs
print("Considering route1")
print routelist1
p1 =  estimate_cost[0]+estimate_cost[5]+estimate_cost[10]+estimate_cost[15]
print "The total estimated costs for this route is"
print p1

print("Considering route2")
print routelist2
p2 =  estimate_cost[0]+estimate_cost[6]+estimate_cost[14]+estimate_cost[11]
print "The total estimated costs for this route is"
print p2

print("Considering route3")
print routelist3
p3 =  estimate_cost[1]+estimate_cost[9]+estimate_cost[6]+estimate_cost[15]
print "The total estimated costs for this route is"
print p3

print("Considering route4")
print routelist4
p4 =  estimate_cost[1]+estimate_cost[10]+estimate_cost[13]+estimate_cost[19]
print "The total estimated costs for this route is"
print p4

print("Considering route5")
print routelist5
p5 =  estimate_cost[2]+estimate_cost[13]+estimate_cost[5]+estimate_cost[11]
print "The total estimated costs for this route is"
print p5

print("Considering route6")
print routelist6
p6 =  estimate_cost[2]+estimate_cost[14]+estimate_cost[9]+estimate_cost[7]
print "The total estimated costs for this route is"
print p6

mincost = min(p1,p2,p3,p4,p5,p6)
print ("The minimum cost is  " + repr(mincost))


print "As the total estimated costs for route " + repr(routelist3) + " is minimum so route 3 is the most preferred route for the entered list of places"











