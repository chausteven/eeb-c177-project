#!/usr/bin/env python
# coding: utf-8

# In[164]:
import pandas as pd
import matplotlib.pyplot as plt

filename = str(input('What .csv file would you like to use?'))
stat = str(input('What statistic do you want to find from the data? (i.e. Max, Min, Avg, Std) '))
key = str(input('What do you want to find the {} of? (i.e Slow approach, Vigilance, Foraging)'.format(stat)))
data = pd.read_csv(filename)
catdata = data.loc[data['TREATMENT'] == 'Cat']
controldata = data.loc[data['TREATMENT'] == 'Control']
if stat.upper() == 'MAX':
    print('This is the maximum behavior score for bettongs exposed to cats:',round(catdata[key].max(), 3))
    print('This is the maximum behavior score for bettongs not exposed to cats:',round(controldata[key].max(), 3))
    plt.scatter(range(len(catdata)),catdata[key], label='Cat Exposed')
    plt.scatter(range(len(controldata)),controldata[key], label='Control')
    plt.legend(loc='upper right')
    plt.ylabel('Behavior Score')
    plt.xlabel('Subject #')
elif stat.upper() == 'MIN':
    print('This is the minimum behavior score for bettongs exposed to cats:',round(catdata[key].min(), 3))
    print('This is the minimum behavior score for bettongs not exposed to cats:',round(controldata[key].min(), 3))
    plt.scatter(range(len(catdata)),catdata[key], label='Cat Exposed')
    plt.scatter(range(len(controldata)),controldata[key], label='Control')
    plt.legend(loc='upper right')
    plt.ylabel('Behavior Score')
    plt.xlabel('Subject #')
elif stat.upper() == 'AVG':
    print('This is the average behavior score for bettongs exposed to cats:',round(catdata[key].mean(), 3))
    print('This is the average behavior score for bettongs not exposed to cats:',round(controldata[key].mean(), 3))
    plt.scatter(range(len(catdata)),catdata[key], label='Cat Exposed')
    plt.scatter(range(len(controldata)),controldata[key], label='Control')
    plt.legend(loc='upper right')
    plt.ylabel('Behavior Score')
    plt.xlabel('Subject #')
elif stat.upper() == 'STD':
    print('This is the standard deviation for behavior score for bettongs exposed to cats:', round(catdata[key].std(), 3))
    print('This is the standard deviation for behavior scores for bettongs not exposed to cats:',round(controldata[key].std(), 3))
    plt.scatter(range(len(catdata)),catdata[key], label='Cat Exposed')
    plt.scatter(range(len(controldata)),controldata[key], label='Control')
    plt.legend(loc='upper right')
    plt.ylabel('Behavior Score')
    plt.xlabel('Subject #')
