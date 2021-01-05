#############################################
#	COMPSCI 220 S1    2019              #
#	Assignment 4   Question 2           #
#                                           #
#	@author  	Bin Kim, bkim763    #
#############################################
import sys
import math
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []
    
    def peek_index(self):
        return self.items[0]

    def getKey(self, item_index, dist):
        return dist[item_index]
    
    def insert_index(self, item_index, distance, dist):
        self.items.append(item_index)
        dist[item_index] = distance

    def decreaseKey(self, item_index, t2, dist):
        dist[item_index] = t2

    def delete(self):
        del self.items[0]
    
    def __str__(self):
        return ' '.join([str(i) for i in self.items])
    
    
def DijkstraPFS(adjacency_list, s_index):
    Q = Queue()
    colour = ['W' for town in range(len(adjacency_list))]
    dist = [-1 for town in range(len(adjacency_list))]
    colour[s_index] = 'G'
    Q.insert_index(s_index, 0, dist)
    while Q.isEmpty() == False:
        u_index = Q.peek_index()
        t1 = Q.getKey(u_index, dist)
        for adjacent_town in adjacency_list[u_index]:
            t2 = t1 + adjacent_town[1]
            if colour[adjacent_town[0]] == 'W':
                colour[adjacent_town[0]] = 'G'
                Q.insert_index(adjacent_town[0], t2, dist)
            elif colour[adjacent_town[0]] == 'G' and Q.getKey(adjacent_town[0], dist) > t2:
                Q.decreaseKey(adjacent_town[0], t2, dist)
        Q.delete()
        colour[u_index] = 'B'
        dist[u_index] = t1
    return dist
                

for line in sys.stdin:
    
    initial_list = line.strip().split(',')

    dimension = int(initial_list[0])
    town_list = []

    x = None
    y = None

    for num in initial_list[1:]:
        if x == None and y == None:
            x = float(num)
            
        elif x != None and y == None:
            y = float(num)
            town_list.append((x, y,))
            x = None
            y = None
            

    n_towns = len(town_list)
    adjacency_list = [[] for town in range(n_towns)]


    for town_index in range(n_towns - 1):#every node but last
        #calculate every distance between a town and others
        for other_town_index in range(town_index + 1, n_towns):
            distance = math.sqrt((town_list[other_town_index][0] - town_list[town_index][0])**2 \
                       + (town_list[other_town_index][1] - town_list[town_index][1])**2)
            print(distance)
            if distance <= 100:
                adjacency_list[town_index].append((other_town_index, distance))
                adjacency_list[other_town_index].append((town_index, distance))



    the_dist = DijkstraPFS(adjacency_list, 0)
    print(the_dist)
    final = the_dist[-1]
    if final == -1:
        print(final)
    else:
        print('{:.2f}'.format(final))
   

        
        
    
    

