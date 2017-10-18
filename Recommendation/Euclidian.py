from rcommendations import critics


def sim_distance(pref, person1, person2):
    si = {}
    for items in pref[person1]:
        if items in pref[person2]:
            si[items] = 1

    if len(si) == 0: return 0

    sum_of_squr = sum([pow(pref[person1][item] - pref[person2][item], 2) for item in pref[person1]
                       if item in pref[person2]])

    return 1 / (1 + sum_of_squr)


print(sim_distance(critics, 'Lisa Rose', 'Jack Matthews'))
