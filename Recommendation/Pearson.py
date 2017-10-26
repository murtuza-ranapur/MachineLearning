from rcommendations import critics
from math import sqrt


def sim_distance(pref, person1, person2):
    si = {}
    for items in pref[person1]:
        if items in pref[person2]:
            si[items] = 1

    n = len(si)
    if n == 0: return 0

    sum1 = sum([pref[person1][item] for item in si])
    sum2 = sum([pref[person2][item] for item in si])

    sum1sqr = sum([pow(pref[person1][item], 2) for item in si])
    sum2sqr = sum([pow(pref[person2][item], 2) for item in si])

    psum = sum([pref[person1][item] * pref[person2][item] for item in si])

    num = psum - (sum1 * sum2 / n)
    den = sqrt((sum1sqr - pow(sum1, 2) / n) * (sum2sqr - pow(sum2, 2) / n))

    if den == 0: return 0

    r = num / den

    return r


# print(sim_distance(critics, 'Lisa Rose', 'Jack Matthews'))
