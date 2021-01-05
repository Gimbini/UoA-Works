#############################################
#	COMPSCI 220 S1    2019              #
#	Assignment 3   Question 2           #
#                                           #
#	@author  	Bin Kim, bkim763    #
#	@version	17/05/18            #
#############################################
import sys


def reverse(n):

    adjacency_list = []
    reverse_list = []
    for i in range (n):
        reverse_list.append([])

    for index in range(n):
        index_input = sys.stdin.readline().strip()
        adjacency_list.append([int(num) for num in index_input.split()])

    for node in range(n):
        for item in adjacency_list[node]:
            reverse_list[item].append(node)
            
    print(n)
    for node in range(n):
        print(*reverse_list[node], ' ')
        


n = int(sys.stdin.readline().strip())

while n != 0:
    reverse(n)
    n = int(sys.stdin.readline().strip())
    
print(0)

sys.exit()

