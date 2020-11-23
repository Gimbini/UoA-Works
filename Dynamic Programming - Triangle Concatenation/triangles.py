
import sys
import copy

n_lines = int(sys.stdin.readline().strip())

# Initialising triangle list
t_set = []

for i in range(n_lines):

    line = sys.stdin.readline().strip().split()
    sides = []
    i = 0
    for item in line:
        if i <= 2:
            sides.append(int(item))
        else:
            g_scale = float(item)
        i += 1
    t_set.append([sides,g_scale])

# Sort by greyscale
A = sorted(t_set, key = lambda x: x[1])


M = []
i_prev = 0
global_max = 1

for t in A:
    for side in range(3):
        t_marked = copy.deepcopy(t)
        t_marked_side = t_marked[0][side]
        t_marked[0][side] = str(t_marked[0][side])

        max = -1
        for i in range(i_prev):
            m = M[i]
            if m[1] < t_marked[1]: # g-value check
                for m_side in m[0]: # compare
                    if type(m_side) != str:
                        if m_side == t_marked_side:
                            if m[2] >= max:
                                max = m[2]


            #no_match = False
        if max == -1:
            t_marked.append(1)
            M.append(t_marked)
        else:
            t_marked.append(max+1)
            M.append(t_marked)
            if max+1 > global_max:
                global_max = max+1
    i_prev += 3

print(global_max)

sys.exit()
