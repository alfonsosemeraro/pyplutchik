#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 20:16:33 2020

@author: alfonso
"""
import matplotlib.pyplot as plt
from pyplutchik import plutchik



emo1 = {
    'joy': [.30, .2, 0.5],
    'trust': [.5, 0.1, 0],
    'fear': [.1, .4,.2],
    'surprise': [.15, .5, .35],
    'sadness': [0, .5, .5],
    'disgust': [.4, .33, .22],
    'anger': [.43, .12, .09],
    'anticipation': [.3, .5, .2]
}


emo2 = {
    'joy': 1,
    'trust': [1, 0, 0],
    'fear': 1,
    'surprise': [0, 1, 0],
    'sadness': 1,
    'disgust': 1,
    'anger': 1,
    'anticipation': [1, 0, 0]
}

emo3 = {
    'joy': 0,
    'trust': [0, 0, 0],
    'fear': 0,
    'surprise': [0, 0, 0],
    'sadness': 0,
    'disgust': 0,
    'anger': 0,
    'anticipation': 0
}

#emo1 = {key: sum(val) for key, val in emo1.items()}
#
#plutchik(emo1, show_coordinates = False);
selected_emotions = ['anticipation', 'joy', 'sadness']
plutchik(emo1, highlight_emotions = selected_emotions, show_intensity_labels = selected_emotions)
plt.savefig('img/provaalf.png', bbox_inches = 'tight', dpi = 300)
#plutchik(emo2);
#plutchik(emo3);



#fig, ax = plt.subplots(figsize = (15, 15))
#plutchik(emo1, ax, fontsize = 20, fontweight = 'bold');

#
#import random
#fig, axs = plt.subplots(5, 5, figsize = (25, 25))
#
#for i in range(25):
#    emoj = {e: [random.uniform(0, .33),random.uniform(0, .33),random.uniform(0, .33)] for e in emo1.keys()}
#    plt.subplot(5, 5, i+1)
#    plutchik(ax = plt.gca(), emotions = emoj, show_coordinates = False)
#    
#plt.savefig('img/example2.png', dpi = 300)