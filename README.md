
# PyPlutchik
Python visualisation for Plutchik annotated corpora.

PyPlutchik is a module for visualizing the emotional fingerprint of corpora and text annotated with the [Plutchik's model of emotions](https://en.wikipedia.org/wiki/Robert_Plutchik).

If you use it, please cite
```
Semeraro A, Vilella S, Ruffo G (2021) 
PyPlutchik: Visualising and comparing emotion-annotated corpora 
PLOS ONE 16(9): e0256503.https://doi.org/10.1371/journal.pone.0256503
```


### Installation

Installation with pip:

```
pip3 install pyplutchik
```

Installation with conda:
```
conda install pyplutchik
```


### Usage
```python
from pyplutchik import plutchik

emotions = {'joy': 0.6,
            'trust': 0.4,
            'fear': 0.1,
            'surprise': 0.7,
            'sadness': 0.1,
            'disgust': 0.5,
            'anger': 0.4,
            'anticipation': 0.6}
            
plutchik(emotions)
```

### Features
PyPlutchik provides a plug-and-play tool for a quantitative representation of Plutchik's emotions in a text or corpus. It is respectful of original colors and spatial displacement of each petal in the Plutchik's wheel.
In Pyplutchik users can just pass a dictionary as only parameter, where dictionary's keys must be the 8 basic emotions. Each value must be ∈ [0, 1].

<img src="https://github.com/alfonsosemeraro/pyplutchik/blob/master/img/example01.png" alt="Example 1" width="650"/>



Users can represent also the three degrees of intensity for each emotion, just by providing a 3-dimensional iterable as value for each key in the dictionary. The sum of the components of each 3-dimensional val must be between 0 and 1.

<img src="https://github.com/alfonsosemeraro/pyplutchik/blob/master/img/example02.png" alt="Example 2" width="650"/>



PyPlutchik also represents primary dyads, secondary dyads, tertiary dyads and opposite emotions. It automatically understands what kind of dyad users want to display from the dictionary's keywords.

<img src="https://github.com/alfonsosemeraro/pyplutchik/blob/master/img/example03.png" alt="Example 3" width="650"/>




Integration with [matplotlib](https://matplotlib.org/) is easy, so PyPlutchik can be used for also for composed plots.

<img src="https://github.com/alfonsosemeraro/pyplutchik/blob/master/img/dyads_show.png" alt="Full spectrum of emotions" width="400"/>


### A couple of tricks

One can focus on a subset of emotions, ignoring the remaining ones, passing a list of emotions as value of the parameter `highlight_emotions`:

<img src="https://github.com/alfonsosemeraro/pyplutchik/blob/master/img/highlight_emotions.png" alt="Highlight some emotions" width="500"/>


Or can hide coordinates, ticks and labels, plotting only the petals of the flower, using the parameters `show_coordinates = False` and `show_ticklabels = False`:

<img src="https://github.com/alfonsosemeraro/pyplutchik/blob/master/img/imdb_full.png" alt="Small multiple" width="500"/>


## Full documentation

For a documentation of all parameters and a gallery of examples see [the documentation](https://github.com/alfonsosemeraro/pyplutchik/blob/master/Documentation.md).



🔥 PyPlutchik 2.0 is on its way! New features include extraction of emotions from texts and check against a non-topical Lexicon. Stay tuned... 🔥

