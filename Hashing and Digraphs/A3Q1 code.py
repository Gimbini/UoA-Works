#############################################
#	COMPSCI 220 S1    2019              #
#	Assignment 3     Quesion 1          #
#                                           #
#	@author  	Bin Kim, bkim763    #
#	@version	17/05/18            #
#############################################
import sys
import math

def Hash():
    for input_line in sys.stdin:
        input_index = 0
        input_list = input_line.split(',')
        for i in range(len(input_list)):
            input_list[i] = int(input_list[i])
        n = len(input_list) - 2
        m = input_list[0]
        p = input_list[1]
        out_of_place = 0
        hash_table = [None] * m

        #hashing until last item
        for index in range(2, len(input_list) - 1):
            x = input_list[index]
            primary_hash = x % m
            probe_index = primary_hash
            if hash_table[probe_index] == None:
                hash_table[probe_index] = x

            else:
                out_of_place += 1
                hashed = False
                secondary_hash = x % p + 1
                while hashed == False:
                    probe_index -= secondary_hash
                    if probe_index < 0:
                        probe_index = probe_index % m
                    if hash_table[probe_index] == None:
                        hash_table[probe_index] = x
                        hashed = True

        #hashing last item + probe count
        probe = 0
        x = input_list[-1]#final item
        primary_hash = x % m
        probe_index = primary_hash
        probe += 1
        if hash_table[probe_index] == None:
            hash_table[probe_index] = x

        else:
            out_of_place += 1
            hashed = False
            secondary_hash = x % p + 1
            while hashed == False:
                probe_index -= secondary_hash
                probe += 1
                probe_index = probe_index % m
                if hash_table[probe_index] == None:
                    hash_table[probe_index] = x
                    hashed = True
        


        probes_expected = 1 / (n/m) * math.log(1 / (1 - (n/m)))
        print(str(out_of_place) + ',' + str(probe) + ',' + '{0:.3f}'.format(probes_expected))


        
    
Hash()
