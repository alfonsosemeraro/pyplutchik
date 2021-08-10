#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 16:57:57 2021

@author: alfonso
"""

import json
from nrclex import NRCLex
import numpy as np
from pyplutchik import plutchik
import matplotlib.pyplot as plt



    
""" 
    Dataset from https://jmcauley.ucsd.edu/data/amazon/
    
    We downloaded the Office Products reviews.
    
    The dataset is a list of dicts.
    
    We only used the `overall` entry for filtering the star rating of a review
    and the `reviewText` entry, that contains the text of the review.
    
    We annotated emotions in the review texts by the means of the NRCLex library.
"""


def get_emotions_text(text, keys):
    
    # Gets emotions associated to words in the review's text
    emo = NRCLex(text).raw_emotion_scores
    
    # Counts emotions occurrences (default is 0)
    emo = {key: int(emo[key] > 0) if key in emo else 0 for key in keys}
    
    return emo





def get_amazon_emotions(amz):
           
    # emotions
    keys = ['anger', 'anticipation', 'disgust', 'fear', 'joy', 'sadness', 'surprise', 'trust']
    
    # we want a dict < N_stars: scores of products rated N_stars >
    emo_scores = {}
    
    for i in range(1, 5, 1):
        
        # Get texts of reviews of products rated i-star
        tmp = [a['reviewText'] for a in amz if a['overall'] == i]
        
        # Get scores for each text among the i-star reviews
        scores = [get_emotions_text(t, keys) for t in tmp]
        
        # Average the scores
        emo_scores[str(i)] = {key: np.mean([s[key] for s in scores]) for key in keys}
        
        print("Got", i+1)
        
    
    return emo_scores
    


        
if __name__ == '__main__':
    
    # get dataset
    with open('amazon_office/Office_Products_5.json', 'r') as fr:
        amz = json.load(fr)
        
    # get emotions for each entry in amz
    amz_emo = get_amazon_emotions(amz)
    
    
    
    
    # PLOT 1 : reviews of 1 to 5 star products
    
    fig, ax = plt.subplots(nrows = 1, ncols = 5, figsize = (8*6, 8))
    
    for i in range(5):
        plutchik(amz_emo[str(i + 1)], ax = ax[i], title = '★'*(i+1), title_size = 35)   
        
    plt.savefig('amazon.png', bbox_inches = 'tight', dpi = 200)
    
    
    
    
    # PLOT 2 : comparison between 1-star and 5-star products, highlight on anger, disgust and fear
    
    fig, ax = plt.subplots(nrows = 2, ncols = 2, figsize = (17, 16))
    
    
    plutchik(amz_emo['1'], ax = ax[0][0], title = '★', title_size = 35)
    plutchik(amz_emo['5'], ax = ax[0][1], title = '★★★★★', title_size = 35)
    
    plutchik(amz_emo['1'], ax = ax[1][0], title = '★', title_size = 35, highlight_emotions = ['anger', 'disgust', 'fear'], show_intensity_labels = ['anger', 'disgust', 'fear'])
    plutchik(amz_emo['5'], ax = ax[1][1], title = '★★★★★', title_size = 35, highlight_emotions = ['anger', 'disgust', 'fear'], show_intensity_labels = ['anger', 'disgust', 'fear'])
    
    
    plt.savefig('amazon_comparison.png', bbox_inches = 'tight', dpi = 200)
    