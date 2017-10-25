from rcommendations import critics
from Pearson import sim_distance
from parseMovieLens import getMovieLensData


def topMatch(prefs,person,n=5,similarity=sim_distance):
    sims=[(similarity(prefs,person,other),other) for other in prefs.keys() if other!=person]

    sims.sort()
    sims.reverse()
    return sims[0:n]


# print(topMatch(critics,'Toby',n=3))

def getRecommmendations(prefs,person,similarity=sim_distance):
    total={}
    simSums={}

    for other in prefs:
        if other == person : continue

        sim=similarity(prefs,person,other)

        if sim<=0 : continue

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

def transformPrefs(prefs):
    result={}
    for pearson in prefs:
        for items in prefs[pearson]:
            result.setdefault(items,{})
            result[items][pearson]=prefs[pearson][items]
    return result

# print(getRecommmendations(critics,'Toby'))
prefTrans=transformPrefs(critics)

# print(topMatch(prefTrans,'Superman Returns'))

"""
Till now we did user based collaborative filtering now we will do item based collaborative filtering
"""

def calculate_similar_items(prefs,n=10):
    result={}
    itemprefs=transformPrefs(prefs)
    c=0
    for item in itemprefs:
        c+=1
        if c%100==0: print("%d / %d"%(c,len(itemprefs)))
        scores=topMatch(itemprefs,item,n=n)
        result[item]=scores
    return result

# print(calculate_similar_items(critics))

def getRecommendedItems(prefs,itemmatch,user):
    userRating=prefs[user]
    scores={}
    totalSim={}

    for item,rating in userRating.items():
        for similarity,item2 in itemmatch[item]:
            if item2 in userRating: continue

            scores.setdefault(item2,0)
            scores[item2]+=similarity*rating

            totalSim.setdefault(item2,0)
            totalSim[item2]+=similarity

    ranking=[(score/totalSim[item],item) for item,score in scores.items()]

    ranking.sort()
    ranking.reverse()
    return ranking


# sim_items=calculate_similar_items(critics)

# print(getRecommendedItems(critics,sim_items,'Toby'))


print(getRecommmendations(getMovieLensData(),87)[0:30])