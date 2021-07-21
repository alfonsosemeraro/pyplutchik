#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 18:57:29 2021

@author: alfonso
"""

from glob import glob
import pandas as pd
import matplotlib.pyplot as plt
from pyplutchik import plutchik

""" 
    Dataset from SSEC.
    Details here http://www.romanklinger.de/ssec/
    
    Annotations are in a column with '\t' as separator; 6 annotators x 8 emotions = 48 values.
    By error, each 48-dim array is preceded by a label, 'pos', 'neg' or 'other', to be deleted.
    
    I guess 1 = emotion detected, 0 = emotion not detected, -1 = line not assigned to that annotator
"""





def unpack_annotation(annot, start_idx):
    
    annot = [int(x) for x in annot.split('\t')[1:]]
    tot = []
    
    # get each 8-th annotation starting from `start_idx`
    for i in range(start_idx, len(annot) + start_idx, 8):
        if annot[i] >= 0:
            tot += [annot[i]]
        
    # more than half of annotators said yes?
    if (sum(tot) / len(tot)) > .5:
        return 1
    
    return 0


def annotate_emotions(ect):
    
    # Order of emotion in dataset is
    # Anger Anticipation Disgust Fear Joy Sadness Surprise Trust
    # by docs
    ect['anger'] = [unpack_annotation(ect.iloc[x, 4], 0) for x in range(len(ect))]
    ect['anticipation'] = [unpack_annotation(ect.iloc[x, 4], 1) for x in range(len(ect))]
    ect['disgust'] = [unpack_annotation(ect.iloc[x, 4], 2) for x in range(len(ect))]
    ect['fear'] = [unpack_annotation(ect.iloc[x, 4], 3) for x in range(len(ect))]
    
    ect['joy'] = [unpack_annotation(ect.iloc[x, 4], 4) for x in range(len(ect))]
    ect['sadness'] = [unpack_annotation(ect.iloc[x, 4], 5) for x in range(len(ect))]
    ect['surprise'] = [unpack_annotation(ect.iloc[x, 4], 6) for x in range(len(ect))]
    ect['trust'] = [unpack_annotation(ect.iloc[x, 4], 7) for x in range(len(ect))]
    
    ect = ect[['target', 'stance', 'anger', 'anticipation', 'disgust', 'fear', 'joy', 'sadness', 'surprise', 'trust']]
    
    return ect


def annotate_dyads(df):
    
    # PRIMARY
        
    df['love'] = df.apply(lambda row: row.joy and row.trust, axis = 1)
    df['submission'] = df.apply(lambda row: row.trust and row.fear, axis = 1)
    df['alarm'] = df.apply(lambda row: row.fear and row.surprise, axis = 1)
    df['disappointment'] = df.apply(lambda row: row.surprise and row.sadness, axis = 1)
    df['remorse'] = df.apply(lambda row: row.sadness and row.disgust, axis = 1)
    df['contempt'] = df.apply(lambda row: row.disgust and row.anger, axis = 1)
    df['aggressiveness'] = df.apply(lambda row: row.anger and row.anticipation, axis = 1)
    df['optimism'] = df.apply(lambda row: row.anticipation and row.joy, axis = 1)
    
    
    # SECONDARY
    
    df['guilt'] = df.apply(lambda row: row.joy and row.fear, axis = 1)
    df['curiosity'] = df.apply(lambda row: row.trust and row.surprise, axis = 1)
    df['despair'] = df.apply(lambda row: row.fear and row.sadness, axis = 1)
    df['unbelief'] = df.apply(lambda row: row.surprise and row.disgust, axis = 1)
    df['envy'] = df.apply(lambda row: row.sadness and row.anger, axis = 1)
    df['cynism'] = df.apply(lambda row: row.disgust and row.anticipation, axis = 1)
    df['pride'] = df.apply(lambda row: row.anger and row.joy, axis = 1)
    df['hope'] = df.apply(lambda row: row.anticipation and row.trust, axis = 1)
    
    # TERTIARY
    
    df['delight'] = df.apply(lambda row: row.joy and row.surprise, axis = 1)
    df['sentimentality'] = df.apply(lambda row: row.trust and row.sadness, axis = 1)
    df['shame'] = df.apply(lambda row: row.fear and row.disgust, axis = 1)
    df['outrage'] = df.apply(lambda row: row.surprise and row.anger, axis = 1)
    df['pessimism'] = df.apply(lambda row: row.sadness and row.anticipation, axis = 1)
    df['morbidness'] = df.apply(lambda row: row.disgust and row.joy, axis = 1)
    df['dominance'] = df.apply(lambda row: row.anger and row.trust, axis = 1)
    df['anxiety'] = df.apply(lambda row: row.anticipation and row.fear, axis = 1)
    
    # OPPOSITE
    
    df['bittersweetness'] = df.apply(lambda row: row.joy and row.sadness, axis = 1)
    df['ambivalence'] = df.apply(lambda row: row.trust and row.disgust, axis = 1)
    df['frozenness'] = df.apply(lambda row: row.fear and row.anger, axis = 1)
    df['confusion'] = df.apply(lambda row: row.surprise and row.anticipation, axis = 1)
    
    return df


if __name__ == '__main__':
    
    # Read csv and get emotions
    ect = pd.read_csv('emotioncorpus-test.csv', header = None, error_bad_lines = False)
    ect.columns = ['text','target', 'stance', 'a', 'annot']
    ect = annotate_emotions(ect)
    
    # Possible targets and stances
    targets = ['Donald Trump', 'Hillary Clinton']
    stances = ['Supporting', 'Against']
    
    for stance in stances:
        
        
        fig, ax = plt.subplots(2, 5, figsize = (42, 16))
        legs = ['(i)', '(ii)', '(iii)', '(iv)', '(v)', '(vi)', '(vii)', '(viii)', '(ix)', '(x)'][::-1]
    
        for i, target in enumerate(targets):
        
            dfst = 'FAVOR' if stance == 'Supporting' else 'AGAINST'
    
            df = ect.copy()
            df = df.loc[df['target'] == target, ]
            df = df.loc[df['stance'] == dfst, ]
            
            # Get only rows with emotions
            df['s'] = df.apply(lambda row: row.joy + row.trust + row.fear + row.surprise + row.sadness + row.disgust + row.anger + row.anticipation, axis = 1)
            df = df.loc[df['s'] > 0,]
            del df['s']
            
            # Get dyads in the dataset
            df = annotate_dyads(df)
            
            
            # Pandas to dictionaries (mean scores of each emotion/dyad)
            
            emo1 = {col: [0, df[col].mean(), 0] for col in df.columns[2:10]}
            dyads = {}
            dyads['primary'] = {col: df[col].mean() for col in df.columns[10:18]}
            dyads['secondary'] = {col: df[col].mean() for col in df.columns[18:26]}
            dyads['tertiary'] = {col: df[col].mean() for col in df.columns[26:34]}
            dyads['opposites'] = {col: df[col].mean() for col in df.columns[34:]}
            
            
            # Scaling value
            scale = .4 if target == 'Donald Trump' else .3
            
            
            # Plots!
            title = '{} {} - Emotions'.format(stance, target)
            plutchik(emo1, ax = ax[i][0], normalize = .65, title_size = 15, title = title)
            ax[i][0].annotate(s = legs.pop(), xy = (1.5, 1.5), fontsize = 15)
            
            title = '{} {} - primary dyads'.format(stance, target)
            plutchik(dyads['primary'], ax = ax[i][1],  normalize = scale, title_size = 15, title = title)
            ax[i][1].annotate(s = legs.pop(), xy = (1.5, 1.5), fontsize = 15)
            
            title = '{} {} - secondary dyads'.format(stance, target)
            plutchik(dyads['secondary'], ax = ax[i][2], normalize = scale, title_size = 15, title = title)
            ax[i][2].annotate(s = legs.pop(), xy = (1.5, 1.5), fontsize = 15)
            
            title = '{} {} - tertiary dyads'.format(stance, target)
            plutchik(dyads['tertiary'], ax = ax[i][3], normalize = scale, title_size = 15, title = title)
            ax[i][3].annotate(s = legs.pop(), xy = (1.5, 1.5), fontsize = 15)
            
            title = '{} {} - opposite dyads'.format(stance, target)
            plutchik(dyads['opposites'], ax = ax[i][4], normalize = scale, title_size = 15, title = title)
            ax[i][4].annotate(s = legs.pop(), xy = (1.5, 1.5), fontsize = 15)
            
        plt.savefig('{}_5x2.png'.format(stance), bbox_inches = 'tight', dpi = 200)
