#############################################
#	COMPSCI 220 S1    2019              #
#	Assignment 3   Question 3           #
#                                           #
#	@author  	Bin Kim, bkim763    #
#	@version	17/05/18            #
#############################################
import sys


def adjacency_maker(n):
    adjacency_list = []

    for index in range(n):
        index_input = sys.stdin.readline().strip()
        adjacency_list.append([int(num) for num in index_input.split()])

    return adjacency_list



def recursiveDFSvisit(s):
    colour[s] = 'G'
    seen[s] = time[0]
    time[0] += 1
    for v in adjacency_list[s]:
        if colour[v] == 'W':
            pred[v] = s
            recursiveDFSvisit(v)
    colour[s] = 'B'
    done[s] = time[0]
    time[0] += 1
    
n = int(sys.stdin.readline().strip())


while n != 0:
    adjacency_list = adjacency_maker(n)

    colour = ['W'] * n
    seen = [None] * n
    done = [None] * n
    pred = [-1] * n
    time = [0]
    for node in range(len(adjacency_list)):
        if colour[node] == 'W':
            recursiveDFSvisit(node)

    tree_arc = 0
    back_arc = 0

    for v in range(len(adjacency_list)):
        for w in adjacency_list[v]:
            if seen[v] < seen[w] < done[w] < done[v]:
                if pred[w] == v:
                    tree_arc += 1
            if seen[w] < seen[v] < done[v] < done[w]:
                back_arc += 1

    print(str(tree_arc) + ',' + str(back_arc))
                    

    
    n = int(sys.stdin.readline().strip())
    
sys.exit()
