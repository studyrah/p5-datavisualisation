# Comparison of Recent vs Historical Rainfall and Temperature - Oxford
## Submission 2 Changes
### by Richard Haughton

## Summary

In response to review comments for my first submission which rightly 
pointed out that my visualisation was too exploratory (not explanatory
enough), I took the reviewers advise and replaced the scatter plot
with density charts for each measure (rainfall, max temp, min temp).

This way my conclusion that min and max temperature have increased
during the 'recent' vs historical timeframe and that rainfall hasn`t,
should me more obvious.

In actual fact I wanted to retain the scatter plot chart to enable the
viewer to drill down into the detail (e.g. look at specific data points,
investigate outliers etc.)

## Design

### Views

The chart now consists of two views.

1. Overview - A static view whose primary section shows rolled up density
charts with a 'historic' and 'recent' series for each measure 

2. Detail - An animated view whose primary section shows month by month
a scatter plot of temperature against rainfall containing both 'max' and
'min temp' series

There are also some enduring elements on each view.

1. Bar charts - Showing side by side values for 'historic' and 'recent'
for each measure by month

2. Mann Whitney - Statistical measure of difference between 'historical'
vs 'recent' for each measure

Navigation between the views is achieved via radio buttons

### Grid System

Fed up with littering the code with pixel values for placement, I 
implemented what can best be described as a 'poor mans Bootstrap grid
layout' to position and size elements using a 12 column by 3 row grid.

This helped to keep consistent alignment between views and make the
code more explanatory

### Refactoring

I refactored some of the code from the first version, specifically
encapsulating repeated chart definition in functions and 
extracting some styling to a separate css file.

I also cleaned up some visual features such as ensuring the color
of tooltips on the bar charts matched the appropriate bar.

## Issues

### Transitions

The primary (additional) issue is that it is really 2 
visualisations stitched together by url`s, which does not allow for 
seamless transition between the two (and results in repeated code).

To combine the two would be an obvious next step but a significant
undertaking and largely 'scaffolding' code (not directly relevant
to the course intent)

### Density plot scale

It is a little misleading to present temparature plots which go
from -5 to 30 inline with the rainfall plot which goes from
-50 to 200.  It has the effect of exaggerating the difference
in the temperature plots.

I didn`t think it was too misleading though, particularly given
the axes are clearly labelled with tick marks.

### Density plot smoothing

Unfortunately to get clean lines that reasonably represent the
difference between historical and recent for the rainfall measure, 
the parameters required for the density function yield negative
values (there can`t be < 0 rainfall!!!!)

I couldn`t find a solution to this and felt that the crucial
thing was the relative difference

## Further Resources

* density plot in d3 - http://bl.ocks.org/jensgrubert/7777399
