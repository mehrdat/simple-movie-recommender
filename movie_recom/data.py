import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from utils import bayesian_avg,movie_finder,creat_x, find_similar_movies

ratings = pd.read_csv('https://s3-us-west-2.amazonaws.com/recommender-tutorial/ratings.csv')
movies = pd.read_csv('https://s3-us-west-2.amazonaws.com/recommender-tutorial/movies.csv')



movie_ratings = ratings.merge(movies, on='movieId')




C = movie_stats['count'].mean()
m = movie_stats['mean'].mean()

print(f"Average number of ratings for a given movie: {C:.2f}")
print(f"Average rating for a given movie: {m:.2f}")

def bayesian_avg(ratings):
    bayesian_avg = (C*m+ratings.sum())/(C+ratings.count())
    return round(bayesian_avg, 3)
movie_stats = movie_stats.merge(bayesian_avg_ratings, on='movieId')

