from rcommendations import critics


def sim_distance(pref, person1, person2):
    si = {}

    for items in pref[person1]:
        if items in pref[person2]:
            si[items] = 1

    if len(si) == 0: return 0

    inc=sum([min((pref[person1][item],pref[person2][item])) for item in pref[person1] if item in pref[person2]])
    deno=sum([max((pref[person1][item],pref[person2][item])) for item in pref[person1] if item in pref[person2]])

    return 1-(inc/deno)

# print(sim_distance(critics, 'Lisa Rose', 'Jack Matthews'))
