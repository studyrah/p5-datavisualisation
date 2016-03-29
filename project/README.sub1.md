# Comparison of Recent vs Historical Rainfall and Temperature - Oxford

### by Richard Haughton

## Summary

Having found this weather set for an area not so far from where I live, I
decided to test a couple of long held theories I had (totaly unscientific)
and illustrate my findings:

1. the weather had got generally hotter since the early 90's
2. the weather had got generally wetter since the early 90's
3. there had been a seasonal shift (as if the seasons had 'left shifted
by a couple of months')

The data itself contains monthly data points for every year since the
1850's showing (amongst other things):

* total rainfall (mm)
* average max temperature per day (degrees celcius)
* average min temperature per day (degrees celcius)

## Data preparation

see:

* ./README.data_cleansing - trivail data cleansing activities
* ./README.mann_whitney - pre-calculation of mann whitney u test scores

## Design

### Initial Considerations
I was very keen to provide a full context chart showing data points
for every single month/year. This was to enable the viewer to see for
themselves whether there appeared to be a trend or just curious outliers

I was also keen to show rain vs temperature on the same chart (naievely)
thinking that 'if my hypotheses held' then we send see a tendancy for
more recent data points to appear towards the top right.  As it turns out
not all my hypotheses appear to hold but the same visualisation technique
shows this.

Finaly, partly for fun and partly because I wanted to be able to consider
each month independently (which might help with the seasonal shift idea),
I wanted to animate the visualisation across months of the year

Armed with these aspirations I looked for a baseline chart to specialise,
selecting the following from the dimplejs examples:

http://dimplejs.org/advanced_examples_viewer.html?id=advanced_storyboard_control


### Approach

I took a crudely iterative approach taking feedback (in person) at key 
stages from family and friends (a software engineer, an electrical 
engineer, a nurse and a retired insurance salesman for context).

I gave them minimal context to understand the visualisation and asked for
both general feedback and a few direct questions:

* what stands out?
* what extra context do you need to understand the chart?
* what do you think of the layout, what could make it clearer?
* does the visualisation convey the intended message?

## Feedback

### Version 1 - ./version1.html

1. This was a crude attempt to get something up and running.  At this stage
there was a scatter plot of rain against max temperature (intention was
to later add a drop down select box to switch to min temperature).

2. Additionally there was an 'interactive legend - bar chart' highlighting 
the month by month animation.  I also used this to display monthly 
average rainfall as I didn't think the main scatter plot represented
this well.

### Version 1 Feedback

* what stands out?

1. Pleasingly people did notice a tendancy for my darker codifying of 
recent years data points as typically having higher temperature

2. By contrast there was no such observation for rainfall, values seemed
almost random (no obvious trend for recent years to be wetter). Which
as it turns out is true, that is to say my original hypothesis is
unfounded - the data never lies!!!!!

* what extra context do you need to understand the chart?

1. A more explanatory title.
2. Better axis titles.
3. Show recent vs historical figures in the rainfall bar chart.

* what do you think of the layout, what could make it clearer?

1. Show min temperature values alongside max temperature

* does the visualisation convey the intended message?

1. kind of shows a rise in max temperature
2. doesn't say anything about changing seasons

* general comments

1. not sure what the bar chart is supposed to mean
2. it's a bit slow (I think they were being kind)

### Version 2 - ./version2.html

1. I introduced the minimum temperature alongside maximum temperature
on the scatter plot.
2. I experimented with a super imposed line chart showing temperature
change over the years

### Version 2 Feedback
* what stands out?

1. awfull line chart - get rid

* what extra context do you need to understand the chart?

1. as before
2. a legend showing which years were which colour

* what do you think of the layout, what could make it clearer?

1. better now min temperature shown too
2. why are there different shades of colour (at this stage I was using
a colour scale to denote the year of each data point - i.e. it wasn't
just one colour for historical and one for recent)

* general comments

none

### Version 3 - ./version3.html

1. Introduced new bar charts for max and min temperature respectively.
2. Introduced side by side bars for historical vs recent data points
3. Removed line chart
4. Revised axis labels

### Version 3 Feedback

* what stands out?

1. Now clearer to see (because of bar charts) the increase in temperature
month on month
2. No obvious evidence of seasonal shift, cos recent and historical have
similar distribution (me para-phrasing). Again the data never lies!!!


* what extra context do you need to understand the chart?

1. Relate the colours in the bar chart to the series in the scatter plot
2. Still haven't improved the title
3. Would be better with month names rather than numbers on bar chart x-axis
4. Some 'stats' to prove there has/hasn't been change in temp/rainfall


* what do you think of the layout, what could make it clearer?

1. put the max temp bar chart above min chart to match the scatter plot
2. some debate as to whether the rain bar chart confused the picture and
whether to remove or move elsewhere (ultimately decided to leave)
3. labels difficult to read
4. show values on hover

### Version 4 (final) - ./index.html

1. increased label size
2. changed ordering and colour of bar charts to better match scatter plot
added Mann Whitney U Test values to give a more objective view of
3. whether there has been change
4. changed title
5. Changed colour scale to binary colour scheme for recent vs historical
encoding

### Version 3 Feedback

By this stage I think I'd probably exhausted 'my focus group', so
feedback was more limited!!!!

1. There was general acceptance that the visualisation was much better
2. Still very slow on transitions

## Outstanding Issues / didn't get time to .....

1. Couldn't get popups on hover to work, I think this would have helped
2. Couldn't change bar chart x-axis to month names over numbers and
still have the animation work properly
3. Didn't investigate performance issues, don't know whether this is 
just 'there are a lot of data points' or something I am doing wrong
4. Couldn't find out how to change shapes on the scatter plot. Wanted
to show min vs max temperature with a different shape
5. Code refactoring - far too much code in one file
6. Code refactoring - should have extracted styling from d3 to css
7. Ideally I would have been allow the user to choose their own
cutoff point (e.g. compare last 50 years to the rest or last 10 years...)

## Resources

* dimplejs.org - for api documentation
* d3.js - for api documentation
* http://dimplejs.org/advanced_examples_viewer.html?id=advanced_storyboard_control - template visualisation
* udacity training materials
* http://stackoverflow.com/questions/31892129/d3-js-rotate-text-to-vertical - rotate text labels in d3 
* http://www.w3schools.com/colors/colors_hex.asp - colour codes
* https://data.gov.uk/dataset/historic-monthly-meteorological-station-data - data set
