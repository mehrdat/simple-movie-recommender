import streamlit as st
from fuzzywuzzy import process
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics.pairwise import cosine_similarity
from fuzzywuzzy import process
from sklearn.neighbors import NearestNeighbors
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors
from data import get_data

# def bayesian_avg(ratings):
#     bayesian_avg = (C*m+ratings.sum())/(C+ratings.count())
#     return round(bayesian_avg, 3)
ratings,movies,movie_index,index_2_movie=get_data()

genres=set(g for G in movies['genres'] for g in G)
for g in genres:
    movies[g]=movies.genres.transform(lambda x: int(g in x))

movie_genre=movies.drop(['movieId','title','genres'],axis=1)

cosine_sim=cosine_similarity(movie_genre,movie_genre)
#movie_index=dict(zip(movies['title'],range(len(movies))))


def movie_finder(title):
    all_titles=movies['title'].tolist()
    closest_match=process.extractOne(title,all_titles)
    return closest_match[0]

def creat_x(df):
    M=df['userId'].nunique()
    N=df['movieId'].nunique()

    user_mapper=dict(zip(np.unique(df['userId']),list(range(M))))
    movie_mapper=dict(zip(np.unique(df['movieId']),list(range(N))))

    user_inv_mapper=dict(zip(list(range(M)),np.unique(df['userId'])))
    movie_inv_mapper=dict(zip(list(range(N)),np.unique(df['movieId'])))

    user_index=[user_mapper[i] for i in df['userId']]
    movie_index=[movie_mapper[i] for i in df['movieId']]

    X=csr_matrix((df['rating'],(user_index,movie_index)),shape=(M,N))
    return X,user_mapper,movie_mapper,user_inv_mapper,movie_inv_mapper



def find_similar_movies(movie_id,X,movie_mapper,movie_inv_mapper,k, metric='cosine'):
    X=X.T
    neighbour_ids=[]
    movie_index=movie_mapper[movie_id]
    movie_vec=X[movie_index]

    if isinstance(movie_vec, (np.ndarray)):
        movie_vec=movie_vec.reshape(1,-1)

    KNN=NearestNeighbors(n_neighbors=k+1,algorithm='brute',metric=metric)
    KNN.fit(X)

    neighbour=KNN.kneighbors(movie_vec,return_distance=False)
    for i in range(0,k):
        n=neighbour.item(i)
        neighbour_ids.append(movie_inv_mapper[n])
    neighbour_ids.pop(0)
    return neighbour_ids


def get_content_based_recommedation(title,n_recommendations=10):
    title=movie_finder(title)
    idx=movie_index[title]
    sim_scores=list(enumerate(cosine_sim[idx]))
    sim_scores=sorted(sim_scores,key=lambda x : x[1],reverse=True)
    sim_scores=sim_scores[1:(n_recommendations+1)]
    similar_movies=[i[0] for i in sim_scores]
    return movies['title'].iloc[similar_movies].reset_index()