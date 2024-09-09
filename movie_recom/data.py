import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#from utils import movie_finder,creat_x, find_similar_movies

def get_data():
    ratings = pd.read_csv('https://s3-us-west-2.amazonaws.com/recommender-tutorial/ratings.csv')
    movies = pd.read_csv('https://s3-us-west-2.amazonaws.com/recommender-tutorial/movies.csv')
    movie_ratings = ratings.merge(movies, on='movieId')
    movie_index=dict(zip(movies['title'],list(movies.index)))

    index_2_movie=dict(zip(movies.index,movies['title']))
    
    return ratings,movies,movie_index,index_2_movie



