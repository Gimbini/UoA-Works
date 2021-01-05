##############################################
#	COMPSCI 220 S1    2019              #
#	Assignment 1                        #
#       Song List maker                     #
#	@author  	Bin Kim, bkim763    #
#	@version	24/04/19            #
#############################################


import sys

def songs():
    n = int(sys.stdin.readline().strip())
    sep =sys.stdin.readline().strip()
    song_list = [(None)]
    for line in sys.stdin:
        song_list.append(list(line.strip().split(sep)))
        song_list[-1][-1] = int(song_list[-1][-1])

    heapsort(song_list, n, sep)


def heapsort(a, n, seperator):
    k = len(a) - 1
    i = k // 2

    while i > 0:
        sink(a,i,k)
        i -= 1
    while k > 1:
        a[1], a[k] = a[k], a[1]
        k -= 1
        if k > 1:
            sink(a, 1, k)


    for num in range(n):
        print(*a.pop(), sep = seperator)

def sink(a,i,k):
    L = i * 2
    R = i * 2 + 1
    #right child check
    if R <= k:
        #get bigger out of L and R
        if a[L][-1] > a[R][-1]:
            bigger = L
        elif a[L][-1] < a[R][-1]:
            bigger = R
        elif a[L][-1] == a[R][-1]:
            if a[L][0] < a[R][0]:
                bigger = L
            elif a[L][0] > a[R][0]:
                bigger = R
            elif a[L][0] == a[R][0]:
                if len(a[L]) == 2 and len(a[R]) == 2:#L and R are same value, taking right child
                    bigger = R
                if len(a[L]) == 3 and len(a[R]) == 2:
                    bigger = L
                if len(a[L]) == 2 and len(a[R]) == 3:
                    bigger = R
                if len(a[L]) == 3 and len(a[R]) == 3:
                    if a[L][1] < a[R][1]:
                        bigger = L
                    else:
                        bigger = R #if L and R are same, also take right child.

        #compare i & bigger. swap & sink if needed.
        if a[i][-1] < a[bigger][-1]:
            a[i], a[bigger] = a[bigger], a[i]
            if (bigger * 2) <= k:
                sink(a, bigger, k)
        elif a[i][-1] == a[bigger][-1]:
            if a[i][0] > a[bigger][0]:
                a[i], a[bigger] = a[bigger], a[i]
                if (bigger * 2) <= k:
                    sink(a, bigger, k)
            elif a[i][0] == a[bigger][0]:
                if len(a[i]) == 2 and len(a[bigger]) >= 2:#they are same or bigger has composer
                    a[i], a[bigger] = a[bigger], a[i]
                    if (bigger * 2) <= k:
                        sink(a, bigger, k)
                if len(a[i]) == 3 and len(a[bigger]) == 3:
                    if a[i][1] >= a[bigger][1]:
                        a[i], a[bigger] = a[bigger], a[i]
                        if (bigger * 2) <= k:
                            sink(a, bigger, k)









    #no right child
    else:
        if a[i][-1] < a[L][-1]:
            a[i], a[L] = a[L], a[i]
            if (L * 2) <= k:
                sink(a, L, k)
        elif a[i][-1] == a[L][-1]:
            if a[i][0] > a[L][0]:
                a[i], a[L] = a[L], a[i]
                if (L * 2) <= k:
                    sink(a, L, k)
            elif a[i][0] == a[L][0]:
                if len(a[i]) == 2 and len(a[L]) >= 2:#they are same or bigger has composer
                    a[i], a[L] = a[L], a[i]
                    if (L * 2) <= k:
                        sink(a, L, k)
                if len(a[i]) == 3 and len(a[L]) == 3:
                    if a[i][1] >= a[L][1]:
                        a[i], a[L] = a[L], a[i]
                        if (L * 2) <= k:
                            sink(a, L, k)



songs()
