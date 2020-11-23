'''
Author: Bin Kim
UPI: bkim763
Purpose: Finding closest pair of points given latitude & longitude

Method: First convert the lat,long points to x,y,z, then use divide and conquer
algorithm.
'''
import sys
import math

off = False

def closest_pair(cities):
    P_x = sorted(cities, key = lambda x : x[1])
    P_y = sorted(cities, key = lambda x : x[2])

    pair_one, pair_two = closest_pair_rec(P_x,P_y)

    return sorted((pair_one, pair_two), key = lambda x : x[0])


def closest_pair_rec(P_x, P_y):
    list_len = len(P_x)
    if list_len <= 3:
        min_dist = float('inf')
        for i in range(list_len-1):
            point_one = P_x[i]
            for j in range(i+1,list_len):
                point_two = P_x[j]
                distance = math.sqrt((point_one[1]-point_two[1])**2 +  \
                            (point_one[2]-point_two[2])**2 + \
                            (point_one[3]-point_two[3])**2)
                if distance < min_dist:
                    min_dist = distance
                    pair_one = point_one
                    pair_two = point_two
        return pair_one, pair_two

    list_half = math.ceil(list_len/2)

    Q_x, R_x = P_x[0:list_half], P_x[list_half:]
    Q_y, R_y = P_y[0:list_half], P_y[list_half:]

    q_0, q_1 = closest_pair_rec(Q_x, Q_y)
    r_0, r_1 = closest_pair_rec(R_x, R_y)
    dist_q = math.sqrt((q_0[1]-q_1[1])**2 + (q_0[2]-q_1[2])**2 + (q_0[3]-q_1[3])**2)
    dist_r = math.sqrt((r_0[1]-r_1[1])**2 + (r_0[2]-r_1[2])**2 + (r_0[3]-r_1[3])**2)
    delta = min(dist_q, dist_r)

    L = P_x[list_half][1] # half line
    S_x = []
    S_len = 0
    for city in P_x:
        if (city[1] >= L-delta) and (city[1] <= L + delta):
            S_x.append(city)
            S_len += 1

    if S_len != 0:
        S_y = sorted(S_x, key = lambda x: x[2])

        S_min_dist = float('inf')
        # S_y check
        for i in range(S_len-1):
            point_one = S_y[i]
            for j in range(i+1, min(S_len, 7)):
                point_two = S_y[j]
                distance = math.sqrt((point_one[1]-point_two[1])**2 +  \
                            (point_one[2]-point_two[2])**2 + \
                            (point_one[3]-point_two[3])**2)

                if distance < S_min_dist:
                    S_min_dist = distance
                    S_pair_one, S_pair_two = point_one, point_two


    if S_min_dist < delta:
        return S_pair_one, S_pair_two
    elif dist_q <= dist_r:
        return q_0, q_1
    else:
        return r_0, r_1


scenario = 0

while off == False:
    scenario += 1
    n_lines = int(sys.stdin.readline().strip())
    if n_lines == 0:
        off = True
        sys.exit()

    cities = []
    radius = 1000
    for i in range(n_lines):
        line = sys.stdin.readline().strip()
        point = line.split()
        point_long = float(point.pop())
        point_lat = float(point.pop())
        city_name = ' '.join(point)

        # get x,y,z co-ordinate for each city
        lat_radians = math.radians(point_lat)
        long_radians = math.radians(point_long)

        # x = R * cos(lat) * cos(lon)
        # y = R * cos(lat) * sin(lon)
        # z = R *sin(lat)

        x = radius * math.cos(lat_radians) * math.cos(long_radians)
        y = radius * math.cos(lat_radians) * math.sin(long_radians)
        z = radius * math.sin(lat_radians)

        cities.append((city_name, x, y, z, point_lat, point_long))


    # Closest points
    the_pair_list = closest_pair(cities)

    # Calculate dist
    city_one = the_pair_list[0]
    city_two = the_pair_list[1]

    city_one_lat, city_one_long = math.radians(city_one[4]), math.radians(city_one[5])
    city_two_lat, city_two_long = math.radians(city_two[4]), math.radians(city_two[5])


    # Haversine
    a = math.sin((city_one_lat-city_two_lat) / 2)**2 + math.cos(city_one_lat) \
        * math.cos(city_two_lat) * math.sin((city_one_long-city_two_long)/ 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = 6371 * c
    closest_distance = '{:.1f}'.format(d)

    print("Scenario " + str(scenario) + ":")
    print("Closest pair: " + the_pair_list[0][0] + " " + the_pair_list[1][0])
    print("Distance: " + closest_distance)
