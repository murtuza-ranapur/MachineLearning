import pandas as pd


def getMovieLensData():
    movie={}
    data=pd.read_csv("../ml-latest-small/movies.csv")
    for row in data.itertuples():
        movie[row.movieId]=row.title

    prefs={}
    data2=pd.read_csv("../ml-latest-small/ratings.csv")
    for row in data2.itertuples():
        prefs.setdefault(row.userId,{})
        prefs[row.userId][movie[row.movieId]]=float(row.rating)

    return prefs