
# PyPlutchik
Python visualisation for Plutchik annotated corpora.

PyPlutchik is a module for visualizing the emotional fingerprint of corpora and text annotated with the [Plutchik's model of emotions](https://en.wikipedia.org/wiki/Robert_Plutchik).

PyPlutchik provides a plug-and-play tool for a quantitative representation of Plutchik's emotions in a text or corpus. It is respectful of original colors and spatial displacement of each petal in the Plutchik's wheel.
In Pyplutchik users can just pass a dictionary as only parameter, where dictionary's keys must be the 8 basic emotions. Each value must be $\in{[0, 1]}$.

![Example1](https://github.com/alfonsosemeraro/pyplutchik/blob/master/img/example01.png)


Users can represent also the three degrees of intensity for each emotion, just by providing a 3-dimensional iterable as value for each key in the dictionary. Each 3-dimensional value must sum somewhere between 0 and 1.

![Example2](https://github.com/alfonsosemeraro/pyplutchik/blob/master/img/example02.png)

PyPlutchik also represents primary dyads, secondary dyads, tertiary dyads and opposite emotions. It automatically understand what kind of dyad users want to display from the dictionary's keywords.

![Example3](https://github.com/alfonsosemeraro/pyplutchik/blob/master/img/example03.png)


Integration with _matplotlib_ is easy, so PyPlutchik can be used for also for composed plots.

![Full spectrum of emotions](https://github.com/alfonsosemeraro/pyplutchik/blob/master/img/dyads_show.png =300x30)


### A couple tricks

One can focus on a subset of emotions, ignoring the remaining ones...

<img src="https://github.com/alfonsosemeraro/pyplutchik/blob/master/img/highlight_emotions.png" alt="Highlight some emotions" style="width:500px;"/>

... or can hide coordinates, ticks and labels, plotting only the petals of the flower
<img src="https://github.com/alfonsosemeraro/pyplutchik/blob/master/img/imdb_full.png" alt="Small multiple" style="width:500px;"/>


