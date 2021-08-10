#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 17:17:35 2021

@author: alfonso
"""

import pandas as pd
from nrclex import NRCLex
import numpy as np
from pyplutchik import plutchik
import matplotlib.pyplot as plt
import itertools


""" 
    Dataset from Omar Hany's Kaggle repository
    https://www.kaggle.com/omarhanyy/imdb-top-1000
    
    The dataset is a 1000-row csv file.
    
    We only used the `Genre` column for filtering the genre of a movie
    and the `Description` column, that contains the synopsis of the movie.
    
    We annotated emotions in the movie synopsis by the means of the NRCLex library.
"""



def get_emotions(text, keys):

    # Gets emotions associated to words in the review's text
    emo = NRCLex(text).raw_emotion_scores
    
    # Counts emotions occurrences (default is 0)
    emo = {key: int(emo[key] > 0) if key in emo else 0 for key in keys}
    
    return emo
   

    
    
def get_top_genres(imdb_df, N):
    
    # Get a nested list of movie genres
    genres = [genre.split(', ') for genre in imdb_df['Genre']]
    
    # Flat the nested list
    genres = list(itertools.chain.from_iterable(genres))
    
    # Get the top N most represented genres
    genres = pd.Series(genres).value_counts().head(N)
    
    return list(genres.index)


    
def get_emotions_imdb(imdb_df, genres):
    
    # Emotions
    keys = ['anger', 'anticipation', 'disgust', 'fear', 'joy', 'sadness', 'surprise', 'trust']

    # we want a dict < genre: average scores of movies of such genre >
    scores = {}
    
    for genre in genres:
        
        # Get texts of movies of such genre
        tmp = list(imdb_df.loc[imdb_df['Genre'].str.contains(genre), 'Description'].values)
        
        # Get emotions scores associated with each text
        tmpscore = [get_emotions(t, keys) for t in tmp]
        
        # Average scores (by genre)
        scores[genre] = {key: np.mean([ts[key] for ts in tmpscore]) for key in keys}
        
    return scores
      
        
        
if __name__ == '__main__':
    
    # load data
    imdb_df = pd.read_csv('imdb/IMDB top 1000.csv')
    
    
    ## PLOT 1
    
    # get top 20 genres
    genres20 = get_top_genres(imdb_df, 20)
    
    # get emotions of top 20 genres
    imdb_scores_20 = get_emotions_imdb(imdb_df, genres20)
    
    # PLOT 1: top 20 genres, 4 x 5 
    fig, ax = plt.subplots(nrows = 4, ncols = 5, figsize = (8*5, 8*4))

    i = 0
    for row in range(4):
        for col in range(5):
            genre = list(imdb_scores_20.keys())[i]
            plutchik(imdb_scores_20[genre], ax = ax[row][col], show_coordinates = False)   
            ax[row][col].set_title(genre, size = 28)
            i += 1
            
    plt.subplots_adjust(wspace=0, hspace=0)
    plt.savefig('imdb_full.png')
    
    
    
    ## PLOT 2
    
    # selection of genres
    genres = ['Romance', 'Biography', 'Mystery', 'Animation']
    
    # get emotions of selected genres
    imdb_scores_slct = get_emotions_imdb(imdb_df, genres)
    
    # PLOT 2: A 2x2 comparison of 4 genres
    
    fig, ax = plt.subplots(nrows = 2, ncols = 2, figsize = (8*2, 8*2))
    
    i = 0
    for row in range(2):
        for col in range(2):
            genre = list(imdb_scores_slct.keys())[i]
            plutchik(imdb_scores_slct[genre], ax = ax[row][col], title = genre)   
            i += 1
            
        
    plt.savefig('imdb_small.png')
    
    
    