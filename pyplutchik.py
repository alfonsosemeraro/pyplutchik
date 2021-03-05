
"""
**********
Plutchik
**********

This package contains a data visualization tool for corpora annotated with emotions.
Given a JSON representation of the emotions in a text or in a group of texts, it draws the corresponding
Plutchik's flower.

--------
repository available at https://www.github.com/alfonsosemeraro/pyplutchik
@author: Alfonso Semeraro <alfonso.semeraro@gmail.com>

"""

import shapely.geometry as sg
import matplotlib.pyplot as plt
import descartes
from math import sqrt, cos, sin, radians
import numpy as np
import matplotlib.font_manager as fm
from matplotlib import colors


__author__ = """Alfonso Semeraro (alfonso.semeraro@gmail.com)"""
__all__ = ['emo_params',
           '_rotate_point',
           '_polar_coordinates',
           '_neutral_central_circle',
           '_petal_shape',
           '_petal_spine',
           '_petal_circle',
           '_draw_petal',
           'plutchik']




def emo_params(emotion):
    """
    Gets color and angle for drawing a petal.
    Color and angle depend on the emotion name.

    Required arguments:
    ----------
    *emotion*:
        Emotion's name. Possible values: 
        ['joy', 'trust', 'fear', 'surprise', 'sadness', 'disgust', 'anger', 'anticipation']
    
    
    Returns:
    ----------
    *color*:
        Matplotlib color for the petal. See: https://matplotlib.org/3.1.0/gallery/color/named_colors.html
        
    *angle*:
        Each subsequent petal is rotated 45° around the origin.    
        
        
    Notes:
    -----
    This function allows also 8 principal emotions, one for each Plutchik's flower petal.
    No high or low intensity emotions are allowed (no 'ecstasy' or 'serenity', for instance).
    """
    
    if emotion == 'joy':
        color = 'gold'
        angle = 0
    elif emotion == 'trust':
        color = 'olivedrab'
        angle = -45
    elif emotion == 'fear':
        color = 'forestgreen'
        angle = -90
    elif emotion == 'surprise':
        color = 'skyblue'
        angle = -135
    elif emotion == 'sadness':
        color = 'dodgerblue'
        angle = 180
    elif emotion == 'disgust':
        color = 'slateblue'
        angle = 135
    elif emotion == 'anger':
        color = 'orangered'
        angle = 90
    elif emotion == 'anticipation':
        color = 'darkorange'
        angle = 45
    else:
        raise Exception("""Bad input: {} is not an accepted emotion.
                        Must be one of 'joy', 'trust', 'fear', 'surprise', 'sadness', 'disgust', 'anger', 'anticipation'""".format(emotion))
    return color, angle


def _rotate_point(point, angle):
    """
    Rotate a point counterclockwise by a given angle around a given origin.

    Required arguments:
    ----------
    *point*:
        A two-values tuple, (x, y), of the point to rotate
        
    *angle*:
        The angle the point is rotated. The angle should be given in radians.
    
    Returns:
    ----------
    *(qx, qy)*:
        A two-values tuple, the new coordinates of the rotated point.     
        
    """
    ox, oy = 0, 0
    px, py = point
    angle = radians(angle)
    qx = ox + cos(angle) * (px - ox) - sin(angle) * (py - oy)
    qy = oy + sin(angle) * (px - ox) + cos(angle) * (py - oy)
    return (qx, qy)


def _polar_coordinates(ax, font, fontweight, fontsize, show_ticklabels, ticklabels_angle, ticklabels_size, offset = .15):
    """
    Draws polar coordinates as a background.

    Required arguments:
    ----------
    *ax*:
        Axes to draw the coordinates.
        
    *font*:
        Font of text. Default is Montserrat.
        
    *fontweight*:
        Font weight of text. Default is light.
        
    *fontsize*:
        Font size of text. Default is 15.
        
    *show_ticklabels*:
        Boolean, wether to show tick labels under Joy petal. Default is False.
        
    *ticklabels_angle*:
        How much to rotate tick labels from y=0. Value should be given in radians. Default is 0.
        
    *ticklabels_size*:
        Size of tick labels. Default is 11.
        
    *offset*:
        Central neutral circle has radius = .15, and coordinates must start from there.
    
    Returns:
    ----------
    *ax*:
        The input Axes modified.     
        
    """
    
    # Lines
    for i in range(0, 110, 20):
        c = plt.Circle((0, 0), offset + i/100, color = 'grey', alpha = .3, fill = False, zorder = -20)
        ax.add_artist(c)

        
    # Tick labels
    if show_ticklabels:
        for x in np.arange(0.2, 1.2, .2):
            a = round(x, 1)
            x, y = _rotate_point((0, a + offset), ticklabels_angle) #-.12
            ax.annotate(s = str(a), xy = (x, y),  fontfamily = font, size = ticklabels_size, fontweight = fontweight, zorder = 8, rotation = ticklabels_angle)
    return ax


def _neutral_central_circle(ax, r = .15):
    """
    Draws central neutral circle (in grey).

    Required arguments:
    ----------
    *ax*:
        Axes to draw the coordinates.
        
    *r*:
        Radius of the circle. Default is .15.
        
    Returns:
    ----------
    *ax*:
        The input Axes modified.     
        
    """
    c = sg.Point(0, 0).buffer(r)
    ax.add_patch(descartes.PolygonPatch(c, fc='white', ec=(.5, .5, .5, .3), alpha=1, zorder = 15))
    
    return ax
    

def _outer_border(ax, emotion_score, color, angle, highlight, offset = .15, height_width_ratio = 1):
    """
    Draw a the outer border of a petal.
    
    Required arguments:
    ----------
    *ax*:
        Axes to draw the coordinates.
        
    *emotion_score*:
        Score of the emotion. Values range from 0 to 1.
       
    *color*:
        Color of the petal. See emo_params().       
        
    *angle*:
        Rotation angle of the petal. See emo_params().
        
    *highlight*:
        String. 'opaque' if the petal must be shadowed, 'regular' is default.
        
    *offset*:
        Central neutral circle has radius = .15, and petals must start from there.
    
    *height_width_ratio*:
        Ratio between height and width of the petal. Lower the ratio, thicker the petal. Default is 1.
        
    """
    
    # Computing proportions. 
    h = 1*emotion_score + offset
    x = height_width_ratio*emotion_score
    y = h/2 
    r = sqrt(x**2 + y**2)
    
    # Computing rotated centers
    x_right, y_right = _rotate_point((x, y), angle)
    x_left, y_left = _rotate_point((-x, y), angle)
    
    # Circles and intersection
    right = sg.Point(x_right, y_right).buffer(r)
    left = sg.Point(x_left, y_left).buffer(r)
    petal = right.intersection(left)
    
    alpha = 1 if highlight == 'regular' else .8
    ecol = (colors.to_rgba(color)[0], colors.to_rgba(color)[1], colors.to_rgba(color)[2], alpha)

    ax.add_patch(descartes.PolygonPatch(petal, fc=(0, 0, 0, 0), ec = ecol, lw= 1))
    
    
    
def _petal_shape(ax, emotion_score, color, angle, font, fontweight, fontsize, highlight, will_circle, offset = .15, height_width_ratio = 1):
    """
    Draw a petal.
    A petal is the intersection area between two circles.
    The height of the petal depends on the radius and the center of the circles.
    Full details at http://www.github.com/alfonsosemeraro/plutchik/tutorial.ipynb
    
    Required arguments:
    ----------
    *ax*:
        Axes to draw the coordinates.
        
    *emotion_score*:
        Score of the emotion. Values range from 0 to 1.
       
    *color*:
        Color of the petal. See emo_params().
        
    *angle*:
        Rotation angle of the petal. See emo_params().
        
    *font*:
        Font of text. Default is Montserrat.
        
    *fontweight*:
        Font weight of text. Default is light.
        
    *fontsize*:
        Font size of text. Default is 15.
        
    *highlight*:
        String. 'opaque' if the petal must be shadowed, 'regular' is default.
        
    *will_circle*:
        Boolean. If three intensities will be plotted, then the lower petal must be pale.
        
    *offset*:
        Central neutral circle has radius = .15, and petals must start from there.
    
    *height_width_ratio*:
        Ratio between height and width of the petal. Lower the ratio, thicker the petal. Default is 1.
        
    Returns:
    ----------
    *petal*:
        The petal, a shapely shape.     
        
    """

    
    # Computing proportions. 
    h = 1*emotion_score + offset
    x = height_width_ratio*emotion_score
    y = h/2 
    r = sqrt(x**2 + y**2)
    
    # Computing rotated centers
    x_right, y_right = _rotate_point((x, y), angle)
    x_left, y_left = _rotate_point((-x, y), angle)
    
    # Circles and intersection
    right = sg.Point(x_right, y_right).buffer(r)
    left = sg.Point(x_left, y_left).buffer(r)
    petal = right.intersection(left)
    
    if highlight == 'regular':
        if will_circle:
            alpha = .3
        else:
            alpha = .5
            
    elif will_circle:
        alpha = .0
        
    else:
        alpha = .0
    
    ax.add_patch(descartes.PolygonPatch(petal, fc='white', lw = 0, alpha=1, zorder = 0))
    ax.add_patch(descartes.PolygonPatch(petal, fc=color, lw= 0, alpha=alpha, zorder = 10))
    
    return petal


def _petal_spine(ax, emotion, emotion_score, color, angle, font, fontweight, fontsize, highlight = 'all', offset = .15):
    """
    Draw the spine beneath a petal, and the annotation of emotion and emotion's value.
    The spine is a straight line from the center, of length 1.03.
    Full details at http://www.github.com/alfonsosemeraro/plutchik/tutorial.ipynb
    
    Required arguments:
    ----------
    *ax*:
        Axes to draw the coordinates.
        
    *emotion*:
        Emotion's name.
        
    *emotion_score*:
        Score of the emotion. Values range from 0 to 1. if list, it must contain 3 values that sum up to 1.
       
    *color*:
        Color of the petal. See emo_params().
        
    *angle*:
        Rotation angle of the petal. See emo_params().
        
    *font*:
        Font of text. Default is Montserrat.
        
    *fontweight*:
        Font weight of text. Default is light.
        
    *fontsize*:
        Font size of text. Default is 15.
        
    *highlight*:
        String. 'opaque' if the petal must be shadowed, 'regular' is default.
        
    *offset*:
        Central neutral circle has radius = .15, and petals must start from there.
        
    """
    
    # Diagonal lines and ticks
    step = .03
    p1 = (0, 0) # 0, 0 + offset
    p2 = _rotate_point((0, 1 + step + offset), angle) # draw line until 0, 1 + step + offset
    p3 = _rotate_point((-step, 1 + step + offset), angle) # draw tick
    ax.plot([p1[0], p2[0]], [p1[1], p2[1]], zorder = 5, color = 'black', alpha = .3, linewidth = .75)
    ax.plot([p2[0], p3[0]], [p2[1], p3[1]], zorder = 5, color = 'black', alpha = .3, linewidth = .75)
    
    if highlight == 'opaque':
        alpha = .8
        color = 'lightgrey'
    else:
        alpha = 1
    
    try:
        _ = emotion_score[0]
        iterable = True
    except:
        iterable = False
        
    if iterable:
        # Annotation
        angle2 = angle + 180 if abs(angle) > 120 else angle
        p4 = _rotate_point((0, 1.4 + step + offset), angle)
        ax.annotate(s = emotion, xy = p4, rotation = angle2, ha='center', va = 'center',
                    fontfamily = font, size = fontsize, fontweight = fontweight)
        p5 = _rotate_point((0, 1.1 + step + offset), angle)
        p6 = _rotate_point((0, 1.2 + step + offset), angle)
        p7 = _rotate_point((0, 1.3 + step + offset), angle)
        ax.annotate(s = "{0:.2f}".format(round(emotion_score[0],2)), xy = p5, rotation = angle2, ha='center', va = 'center',
                    color = color, fontfamily = font, size = fontsize, fontweight = 'regular', alpha = alpha)
        ax.annotate(s = "{0:.2f}".format(round(emotion_score[1],2)), xy = p6, rotation = angle2, ha='center', va = 'center',
                    color = color, fontfamily = font, size = fontsize, fontweight = 'demibold', alpha = alpha)
        ax.annotate(s = "{0:.2f}".format(round(emotion_score[2],2)), xy = p7, rotation = angle2, ha='center', va = 'center',
                    color = color, fontfamily = font, size = fontsize, fontweight = 'regular', alpha = alpha)        
        
    else:  
        # Annotation
        angle2 = angle + 180 if abs(angle) > 120 else angle
        p4 = _rotate_point((0, 1.2 + step + offset), angle)
        ax.annotate(s = emotion, xy = p4, rotation = angle2, ha='center', va = 'center',
                    fontfamily = font, size = fontsize, fontweight = fontweight)
        p5 = _rotate_point((0, 1.1 + step + offset), angle)
        ax.annotate(s = "{0:.2f}".format(round(emotion_score,2)), xy = p5, rotation = angle2, ha='center', va = 'center',
                    color = color, fontfamily = font, size = fontsize, fontweight = 'demibold', alpha = alpha)
    
    
def _petal_circle(ax, petal, radius, color, inner = False, highlight = 'none', offset = .15):
    """
    Each petal has 3 emotions, 3 degrees of intensity.
    Each of the three sections of a petal is the interception between
    the petal and up to two concentric circles from the origin.
    This function draws one section.
    Full details at http://www.github.com/alfonsosemeraro/plutchik/tutorial.ipynb
    
    Required arguments:
    ----------
    *ax*:
        Axes to draw the coordinates.
        
    *petal*:
        The petal shape. See petal().
        
    *radius*:
        Radius of the section.
       
    *color*:
        Color of the section. See emo_params().
        
    *inner*:
        Boolean. If True, a second patch is drawn with alpha = 0.3, making the inner circle darker.
        
    *highlight*:
        String. 'opaque' if the petal must be shadowed, 'regular' is default.
        
    *offset*:
        Central neutral circle has radius = .15, and petals must start from there.
    
    """
    if radius:
        c = sg.Point(0, 0).buffer(radius + offset)
        area = petal.intersection(c)
        
        alpha0 = 1 if highlight == 'regular' else .2
        
        ecol = (colors.to_rgba(color)[0], colors.to_rgba(color)[1], colors.to_rgba(color)[2], alpha0)
        
        alpha1 = .5 if highlight == 'regular' else .0
        alpha2 = .3 if highlight == 'regular' else .0
        
        ax.add_patch(descartes.PolygonPatch(area, fc=color, ec = 'black', lw = 0, alpha=alpha1))
        ax.add_patch(descartes.PolygonPatch(area, fc=(0, 0, 0, 0), ec = ecol, lw = 1.3))
        
        if inner:
            ax.add_patch(descartes.PolygonPatch(area, fc=color, ec = 'w', lw = 0, alpha=alpha2))
            ax.add_patch(descartes.PolygonPatch(area, fc=(0, 0, 0, 0), ec = ecol, lw = 1.5))
    

def _draw_petal(ax, emotion, emotion_score, highlight_emotions, show_intensity_labels, font, fontweight, fontsize, show_coordinates, height_width_ratio):
    """
    Draw the petal and its possible sections.
    Full details at http://www.github.com/alfonsosemeraro/plutchik/tutorial.ipynb
    
    Required arguments:
    ----------
    *ax*:
        Axes to draw the coordinates.
        
    *emotion*:
        Emotion's name.
        
    *emotion_score*:
        Score of the emotion. Values range from 0 to 1.
    
    *highlight_emotions*:
        A list of main emotions to highlight. Other emotions will be shadowed.
        
    *show_intensity_labels*:
        A string or a list of main emotions. It shows all three intensity scores for each emotion in the list, and for the others cumulative scores. Default is 'none'.
         
    *font*:
        Font of text. Default is Montserrat.
        
    *fontweight*:
        Font weight of text. Default is light.
        
    *fontsize*:
        Font size of text. Default is 15.
        
    *offset*:
        Central neutral circle has radius = .15, and petals must start from there.
       
    *show_coordinates*:
        A boolean, wether to show polar coordinates or not.   
    """
    color, angle = emo_params(emotion)
    
    try:
        _ = emotion_score[0]
        iterable = True
    except:
        iterable = False
    
        
    if highlight_emotions != 'all':
        if emotion in highlight_emotions:
            highlight = 'regular'
        else:
            highlight = 'opaque'
    else:
        highlight = 'regular'
        

    if not iterable:
        if show_coordinates:
            _petal_spine(ax = ax, emotion = emotion, emotion_score = emotion_score, 
                        color = color, angle = angle, 
                        font = font, fontweight = fontweight, fontsize = fontsize, 
                        highlight = highlight)
        _petal_shape(ax, emotion_score, color, angle, font, fontweight, fontsize, height_width_ratio = height_width_ratio, highlight = highlight, will_circle = False)
        _outer_border(ax, emotion_score, color, angle, height_width_ratio = height_width_ratio, highlight = highlight)
        
    else:
        a, b, c = emotion_score
        length = a + b + c
        label = emotion_score if ((show_intensity_labels == 'all') or (emotion in show_intensity_labels)) else length
        
        if show_coordinates:
            _petal_spine(ax = ax, emotion = emotion, emotion_score = label, 
                        color = color, angle = angle, 
                        font = font, fontweight = fontweight, fontsize = fontsize,
                        highlight = highlight)
        petal_shape = _petal_shape(ax, length, color, angle, font, fontweight, fontsize, height_width_ratio = height_width_ratio, highlight = highlight, will_circle = True)
        _petal_circle(ax, petal_shape, a + b, color, False, highlight)
        _petal_circle(ax, petal_shape, a, color, True, highlight)        
        _outer_border(ax, length, color, angle, height_width_ratio = height_width_ratio, highlight = highlight)


def plutchik(emotions, ax = None, font = None, fontweight = 'light', fontsize = 15, show_coordinates = True, show_ticklabels = False, highlight_emotions = 'all', show_intensity_labels = 'none', ticklabels_angle = 0, ticklabels_size = 11, height_width_ratio = 1, title = None, title_size = 15):
    """
    Draw the petal and its possible sections.
    Full details at http://www.github.com/alfonsosemeraro/plutchik/tutorial.ipynb
    
    Required arguments:
    ----------
          
    *emotions*:
        Emotion's JSON. For each emotion, values accepted are a 3-values iterable or a scalar value between 0 and 1.
        The sum of the 3-values iterable values must not exceed 1, and no value should be negative.
        See emo_params() for accepted emotions.
        
    *ax*:
        Axes to draw the coordinates.
        
    *font*:
        Font of text. Default is Montserrat.
        
    *fontweight*:
        Font weight of text. Default is light.
        
    *fontsize*:
        Font size of text. Default is 15.
        
    *offset*:
        Central neutral circle has radius = .15, and petals must start from there.
       
    *show_coordinates*:
        A boolean, wether to show polar coordinates or not.
        
    *show_ticklabels*:
        Boolean, wether to show tick labels under Joy petal. Default is False.
        
    *highlight_emotions*:
        A string or a list of main emotions to highlight. If a list of emotions is given, other emotions will be shadowed. Default is 'all'.
        
    *show_intensity_labels*:
        A string or a list of main emotions. It shows all three intensity scores for each emotion in the list, and for the others cumulative scores. Default is 'none'.
        
    *ticklabels_angle*:
        How much to rotate tick labels from y=0. Value should be given in radians. Default is 0.
        
    *ticklabels_size*:
        Size of tick labels. Default is 11.
        
    *height_width_ratio*:
        Ratio between height and width of the petal. Lower the ratio, thicker the petal. Default is 1.
        
    *title*:
        Title for the plot.
        
    *title_size*:
        Size of the title. Default is 15.
        
    Returns:
    ----------
    *ax*:
        The input Axes modified.     
        
    """

    if not ax:
        fig, ax = plt.subplots(figsize = (8, 8))
    
    if not font:
        font = 'Montserrat'
        fm.fontManager.addfont('res/Montserrat-Regular.ttf')
        fm.fontManager.addfont('res/Montserrat-SemiBold.ttf')
        fm.fontManager.addfont('res/Montserrat-ExtraLight.ttf')
    
    emotions = {key.lower(): val for key, val in emotions.items()}
    
    if show_coordinates:
        _polar_coordinates(ax, font, fontweight, fontsize, show_ticklabels, ticklabels_angle, ticklabels_size)
        
    _neutral_central_circle(ax)
    for emo in emotions:
        if hasattr(emotions[emo], '__iter__'): 
            if sum(emotions[emo]) > 1 or any([e < 0 for e in emotions[emo]]):
                raise Exception("Bad input for `{}`. Emotion scores array should be between 0 and 1.".format(emo))
        else:
            if emotions[emo] > 1 or emotions[emo] < 0:
                raise Exception("Bad input for `{}`. Emotion scores array should be between 0 and 1.".format(emo))
                
        _draw_petal(ax, emotion_score = emotions[emo], emotion = emo, 
                    font = font, fontweight = fontweight, fontsize = fontsize,
                    highlight_emotions = highlight_emotions, show_intensity_labels = show_intensity_labels,
                    show_coordinates = show_coordinates, height_width_ratio = height_width_ratio)
     
        
    try:
        _ = emotions['joy'][0]
        iterable = True
    except:
        iterable = False
        
    if show_coordinates:
        if show_intensity_labels != 'none' and iterable:
            ax.set_xlim(-1.6, 1.6)
            ax.set_ylim(-1.6, 1.6)
        else:
            ax.set_xlim(-1.6, 1.6)
            ax.set_ylim(-1.6, 1.6)
    else:
        ax.set_xlim(-1.2, 1.2)
        ax.set_ylim(-1.2, 1.2)
        
    ax.axis('off')
    
    if not title_size:
        title_size = fontsize
    
    if title:
        ax.set_title(title, fontfamily = 'Montserrat SemiBold', fontsize = title_size, fontweight = 'bold')
        
    return ax
