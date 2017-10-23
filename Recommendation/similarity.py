from rcommendations import critics
from Pearson import sim_distance


def topMatch(prefs,person,n=5,similarity=sim_distance):
    sims=[(similarity(prefs,person,other),other) for other in prefs.keys() if other!=person]

    sims.sort()
    sims.reverse()
    return sims[0:n]


print(topMatch(critics,'Toby',n=3))

def getRecommmendations(prefs,person,similarity=sim_distance):
    total={}
    simSums={}

    for other in prefs:
        if other == person : continue

        sim=similarity(prefs,person,other)

        if sim<0 : continue

        for item in prefs[other]:
            if item not in prefs[person] or prefs[person][item]==0:
                total.setdefault(item,0)
                total[item]+=prefs[other][item]*sim
                simSums.setdefault(item,0)
                simSums[item]+=sim

        ranking=[(total/simSums[item],item) for item,total in total.items()]

        ranking.sort()
        ranking.reverse()
        return ranking

print(getRecommmendations(critics,'Toby'))


