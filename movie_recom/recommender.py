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



X,user_mapper,movie_mapper,user_inv_mapper,movie_inv_mapper=creat_x(ratings)


