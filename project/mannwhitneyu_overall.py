# -*- coding: utf-8 -*-
import numpy as np
import scipy
import scipy.stats
import pandas

def mann_whitney_plus_means(weather, target):

  #print("target: " + target)
  
  before = weather[target][(weather['yyyy'] < 1991)]
  after = weather[target][(weather['yyyy'] > 1990)] 

  #print before
  #print after

  before_mean = np.mean(before)
  after_mean = np.mean(after)
    
  #print "before n: " + str(len(before))
  #print "after n: " + str(len(after))    
    
  #print "mean before: " + str(np.mean(before))
  #print "mean after: " + str(np.mean(after))

  #print "median before: " + str(np.median(before))
  #print "median after: " + str(np.median(after))
                                
  U,p = scipy.stats.mannwhitneyu(before, after)    
    
  #print "U: " + str(U)
  #print "p: " + str(p)
  #print "p: " + str(p * 2)

  return p * 2
    
weather = pandas.read_csv('./data/oxforddata.txt', sep='\t')

#print mann_whitney_plus_means(weather)
#print('rain')
print(mann_whitney_plus_means(weather, 'rain'))
#print('tmax')
print(mann_whitney_plus_means(weather, 'tmax'))
#print('tmin')
print(mann_whitney_plus_means(weather, 'tmin'))
