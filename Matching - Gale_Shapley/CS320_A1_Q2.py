import sys

def gale_shapley(males_po, females_po, unmatched_males, unmatched_females):
    matches_male = {}
    matches_female = {}

    while unmatched_males:
        male = unmatched_males[0]
        preferred_female = males_po[male].pop(0)
        if preferred_female in unmatched_females:
            matches_male[male] = preferred_female
            matches_female[preferred_female] = male

            unmatched_males.remove(male)
            unmatched_females.remove(preferred_female)

        else:
            proposer_rank = females_po[preferred_female].index(male)
            fiance = matches_female[preferred_female]
            fiance_rank = females_po[preferred_female].index(fiance)

            if proposer_rank < fiance_rank:
                matches_male[male] = preferred_female
                matches_female[preferred_female] = male

                unmatched_males.remove(male)
                unmatched_males.append(fiance)
                del matches_male[fiance]

    return matches_male


off = False
instance = 0

while off == False:
    instance += 1

    males_po = {}
    females_po = {}
    unmatched_males = []
    unmatched_females = []


    size_half = int(sys.stdin.readline().strip())

    if size_half == 0:
        off = True
        sys.exit()

    for male in range(1, size_half+1):
        po = [int(x) for x in sys.stdin.readline().strip().split(" ")]
        males_po[male] = po
        unmatched_males.append(male)

    for female in range(1, size_half+1):
        po = [int(x) for x in sys.stdin.readline().strip().split(" ")]
        females_po[female] = po
        unmatched_females.append(female)

    male_matches = gale_shapley(males_po, females_po, unmatched_males, unmatched_females)

    print("Instance {}:".format(instance))

    for i in range(1, size_half+1):
        print("Blue node {0} matched with pink node {1}".format(i, male_matches[i]))
