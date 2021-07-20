Help on module pyplutchik:

NAME
    pyplutchik

DESCRIPTION
    **********
    Plutchik
    **********
    
    This package contains a data visualization tool for corpora annotated with emotions.
    Given a JSON representation of the Plutchik's emotions (or dyads) in a text or in a group of texts, 
    it draws the corresponding Plutchik's flower.
    
    See Plutchik, Robert. "A general psychoevolutionary theory of emotion." Theories of emotion. Academic press, 1980. 3-33.
    
    --------
    repository available at https://www.github.com/alfonsosemeraro/pyplutchik
    @author: Alfonso Semeraro <alfonso.semeraro@gmail.com>

FUNCTIONS
    _check_scores_kind(tags)
        Checks if the inputed scores are all of the same kind 
        (emotions or primary dyads or secondary dyads or tertiary dyads or opposites).
        
        No mixed kinds are allowed.
        
        Required arguments:
        ----------
              
        *tags*:
            List of the tags provided as 'scores'.
            
            
        Returns:
        ----------
        
        A boolean, True if `scores` contains emotions, False if it contains dyads.
    
    _draw_dyad_petal(ax, dyad, dyad_score, font, fontweight, fontsize, show_coordinates, height_width_ratio, offset=0.15, normalize=False)
        Draw the petal and its possible sections.
        Full details at http://www.github.com/alfonsosemeraro/plutchik/tutorial.ipynb
        
        Required arguments:
        ----------
        *ax*:
            Axes to draw the coordinates.
            
        *dyad*:
            Dyad's name.
            
        *dyad_score*:
            Score of the dyad. Values range from 0 to 1.
        
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
            
        *normalize*:
            Either False or the highest value among the dyads. If not False, normalize petal length.
    
    _draw_emotion_petal(ax, emotion, emotion_score, highlight_emotions, show_intensity_labels, font, fontweight, fontsize, show_coordinates, height_width_ratio, normalize=False)
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
            
        *normalize*:
            Either False or the highest value among emotions. If not False, normalize petal length.
    
    _neutral_central_circle(ax, r=0.15)
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
    
    _petal_circle(ax, petal, radius, color, inner=False, highlight='none', offset=0.15, normalize=False)
        Each petal may have 3 degrees of intensity.
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
            
        *normalize*:
            Either False or the highest value among emotions. If not False, must normalize all petal lengths.
    
    _petal_shape_dyad(ax, emotion_score, colorA, colorB, angle, font, fontweight, fontsize, highlight, will_circle, offset=0.15, height_width_ratio=1, normalize=False)
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
           
        *colorA*:
            First color of the petal. See dyad_params().
           
        *colorB*:
            Second color of the petal. See dyad_params().
            
        *angle*:
            Rotation angle of the petal. See dyad_params().
            
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
            
        *normalize*:
            Either False or the highest value among emotions. If not False, must normalize all petal lengths.
            
        Returns:
        ----------
        *petal*:
            The petal, a shapely shape.
    
    _petal_shape_emotion(ax, emotion_score, color, angle, font, fontweight, fontsize, highlight, will_circle, offset=0.15, height_width_ratio=1, normalize=False)
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
            
        *normalize*:
            Either False or the highest value among emotions. If not False, must normalize all petal lengths.
            
        Returns:
        ----------
        *petal*:
            The petal, a shapely shape.
    
    _petal_spine_dyad(ax, dyad, dyad_score, color, emotion_names, angle, font, fontweight, fontsize, highlight='all', offset=0.15)
        Draw the spine beneath a petal, and the annotation of dyad and dyad's value.
        The spine is a straight line from the center, of length 1.03.
        Full details at http://www.github.com/alfonsosemeraro/plutchik/tutorial.ipynb
        
        Required arguments:
        ----------
        *ax*:
            Axes to draw the coordinates.
            
        *dyad*:
            Dyad's name.
            
        *dyad_score*:
            Score of the dyad. Values range from 0 to 1. if list, it must contain 3 values that sum up to 1.
           
        *color*:
            Color of the two emotions of the dyad. See dyad_params().
            
        *emotion_names*:
            Name of the emotions the dyad is made of. See dyad_params().
            
        *angle*:
            Rotation angle of the petal. See dyad_params().
            
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
    
    _petal_spine_emotion(ax, emotion, emotion_score, color, angle, font, fontweight, fontsize, highlight='all', offset=0.15)
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
    
    _polar_coordinates(ax, font, fontweight, fontsize, show_ticklabels, ticklabels_angle, ticklabels_size, offset=0.15)
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
    
    _rotate_point(point, angle)
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
    
    dyad_params(dyad)
        Gets colormap and angle for drawing a dyad.
        Colormap and angle depend on the dyad name.
        
        Required arguments:
        ----------
        *dyad*:
            Dyad's name. Possible values: 
             
            {"primary": ['love', 'submission', 'alarm', 'disappointment', 'remorse', 'contempt', 'aggression', 'optimism'],
             "secondary": ['guilt', 'curiosity', 'despair', '', 'envy', 'cynism', 'pride', 'fatalism'],
             "tertiary": ['delight', 'sentimentality', 'shame', 'outrage', 'pessimism', 'morbidness', 'dominance', 'anxiety']}
        
        Returns:
        ----------
        *colormap*:
            Matplotlib colormap for the dyad. See: https://matplotlib.org/3.1.0/gallery/color/named_colors.html
            
        *angle*:
            Each subsequent dyad is rotated 45° around the origin.
    
    emo_params(emotion)
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
    
    plutchik(scores, ax=None, font=None, fontweight='light', fontsize=15, show_coordinates=True, show_ticklabels=False, highlight_emotions='all', show_intensity_labels='none', ticklabels_angle=0, ticklabels_size=11, height_width_ratio=1, title=None, title_size=None, normalize=False)
        Draw the petal and its possible sections.
        Full details at http://www.github.com/alfonsosemeraro/plutchik/tutorial.ipynb
        
        Required arguments:
        ----------
              
        *scores*:
            A dictionary with emotions or dyads. 
            For each entry, values accepted are a 3-values iterable (for emotions only) or a scalar value between 0 and 1.
            The sum of the 3-values iterable values must not exceed 1, and no value should be negative.
            See emo_params() and dyad_params() for accepted keys.
                    
            Emotions and dyads are mutually exclusive. Different kinds of dyads are mutually exclusive.
        
        *ax*:
            Axes to draw the coordinates.
            
        *font*:
            Font of text. Default is sans-serif.
            
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
            Size of the title. Default is font_size.
            
        Returns:
        ----------
        *ax*:
            The input Axes modified.

DATA
    __all__ = ['emo_params', 'dyad_params', '_rotate_point', '_polar_coord...
    __warningregistry__ = {'version': 12}

AUTHOR
    Alfonso Semeraro (alfonso.semeraro@gmail.com)

FILE
    /home/alfonso/pyplutchik/pyplutchik.py

