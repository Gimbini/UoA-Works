#############################################
#	COMPSCI 220 S1    2019              #
#	Assignment 4   Question 1           #
#                                           #
#	@author  	Bin Kim, bkim763    #
#############################################
import sys
from functools import reduce

def adjacency_maker(pred_list, nodes_list):

    adjacency_list = [[] for i in range(len(nodes_list))]

    for index in range(len(nodes_list)):
        ancestor_index = int(pred_list[index])
        if ancestor_index != -1:
            adjacency_list[ancestor_index].append(index)

    return reverser(adjacency_list)
    
def reverser(adjacency_list):
    reverse_list = []
    n = len(adjacency_list)
    for i in range(n):
        reverse_list.append([])

    for node in range(n):
        for item in adjacency_list[node]:
            reverse_list[item].append(node)

    return reverse_list
    

def recursiveDFSvisit(s):
    colour[s] = 'G'
    seen[s] = time[0]
    time[0] += 1
    for v in reverse_list[s]:
        if colour[v] == 'W':
            pred[v] = s
            recursiveDFSvisit(v)
    colour[s] = 'B'
    done[s] = time[0]
    time[0] += 1


def calculate(done, nodes_list, reverse_list):
    values_list = [[] for i in range(len(reverse_list))]
    for i in range(len(reverse_list)): #processing topological ordering
        max_index = done.index(max(done))
        #if the value from nodes_list is number, then store in values_list
        if nodes_list[max_index] != '+' and nodes_list[max_index] != '*':
            for predecessor in reverse_list[max_index]:
                values_list[int(predecessor)].append(int(nodes_list[max_index]))
        else: #if the value is * or +
            if reverse_list[max_index] == []: #if this is the root
                if nodes_list[max_index] == '+':
                    final = sum(values_list[max_index])
                    print(final)
                elif nodes_list[max_index] == '*':
                    final = reduce(lambda x, y: x*y, values_list[max_index])
                    print(final)
            else: #if not root
                #calculate and parse on to reverse_list[max_index]
                if nodes_list[max_index] == '+':
                    parse = sum(values_list[max_index])
                    for predecessor in reverse_list[max_index]:
                        values_list[int(predecessor)].append(parse)
                elif nodes_list[max_index] == '*':
                    if values_list[max_index] == []:
                        parse = 0
                    else:
                        parse = reduce(lambda x, y: x*y, values_list[max_index])
                    for predecessor in reverse_list[max_index]:
                        values_list[int(predecessor)].append(parse)





        done[max_index] = 0


stop = False

while stop == False:
    pred_input = sys.stdin.readline()
    #EOF then end
    if not pred_input:
        break
    pred_list = pred_input.strip().split(',')

    
    nodes_list = sys.stdin.readline().strip().split(',')
    n = len(nodes_list)

    if nodes_list == ['']:
        print('0')
        
    elif n == 1:
        print(nodes_list[0])
        
    else:
        reverse_list = adjacency_maker(pred_list, nodes_list)
        
        colour = ['W'] * n
        seen = [None] * n
        done = [None] * n
        pred = [-1] * n
        time = [0]
        for node in range(len(reverse_list)):
            if colour[node] == 'W':
                recursiveDFSvisit(node)

        calculate(done, nodes_list, reverse_list)
