# -*- coding: utf-8 -*-
import numpy as np
import scipy
import scipy.stats
import pandas

def mann_whitney_plus_means(weather, target):


  for i in range(12):
    i = i + 1
    print("target: " + target + " month: " + str(i))
    before = weather[target][(weather['yyyy'] < 1991) & (weather['mm'] == i)]
    after = weather[target][(weather['yyyy'] > 1990) & (weather['mm'] == i)] 

    print before
    print after

    
    before_mean = np.mean(before)
    after_mean = np.mean(after)
    
    print "before n: " + str(len(before))
    print "after n: " + str(len(after))    
    
    print "mean before: " + str(np.mean(before))
    print "mean after: " + str(np.mean(after))

    print "median before: " + str(np.median(before))
    print "median after: " + str(np.median(after))
    
    
                                
    U,p = scipy.stats.mannwhitneyu(before, after)    
    
    #print "U: " + str(U)
    #print "p: " + str(p)
    print "p: " + str(p * 2)    
    

weather = pandas.read_csv('./data/oxforddata.txt', sep='\t')

#print mann_whitney_plus_means(weather)
print('rain')
mann_whitney_plus_means(weather, 'rain')
print('tmax')
mann_whitney_plus_means(weather, 'tmax')
print('tmin')
mann_whitney_plus_means(weather, 'tmin')

#  Ans = (1105.4463767458733, 1090.278780151855, 1924409167.0, 0.024999912793489721)
#
#  So our P value is 0.02, so assuming a p critical of 0.05 we can reasonably
# reject the null hypothesis and thus deduce that there is a difference
# between the mean of the 2 samples
#
# The 'with rain' sample has a higher mean so we can further expect
# that traffic through the turnstile is higher when there is rain
#
# Q. what is the significance of the size of U value 1924409167.0?
