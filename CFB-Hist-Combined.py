# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 14:51:55 2019

@author: NATE
This program creates a collection of subplot histograms of offensive and 
defensive ratings. The rating system was developed by me. The ratings histograms
represent a distribution of skill which a given team can play at These ratings 
are for power5/G5 conferences. Teams can be compared in different conferences
 or across the same conference
"""

from plotly import tools
import plotly
import plotly.graph_objs as go
from plotly import plotly as py
import plotly.figure_factory as ff
import pandas as pd
import numpy as np



defense_loc = r'C:\Users\NATE\.spyder-py3\CFBGames\DefenseDistribution2018.csv'
offense_loc = r'C:\Users\NATE\.spyder-py3\CFBGames\OffenseDistribution2018.csv'
team_file_loc = r'C:\Users\NATE\.spyder-py3\CFBGames\teamnames.csv'


SEC = [ 'Florida', 'Tennessee', 'South Carolina', 'Georgia', 'Kentucky', 'Missouri',  \
       'Vanderbilt', 'Texas A&M', 'Alabama', 'Mississippi' , 'Mississippi St',  \
       'Auburn', 'LSU', 'Arkansas']

ACC = ['Boston College', 'Clemson', 'Duke', 'Florida St', 'Georgia Tech', 'Louisville', \
       'Miami FL', 'NC State', 'North Carolina', 'Pittsburgh', 'Syracuse', \
       'Virginia', 'Virginia Tech', 'Wake Forest', 'Notre Dame']

AAC = ['Cincinnati', 'Connecticut', 'East Carolina' , 'Houston', 'Memphis', 'Navy', \
       'SMU', 'South Florida', 'Temple', 'Tulane', 'Tulsa', 'UCF']

Big_Ten = ['Illinois', 'Indiana', 'Iowa', 'Maryland', 'Michigan', 'Michigan St', \
           'Minnesota', 'Northwestern', 'Ohio St', 'Penn St', 'Rutgers' , \
           'Wisconsin', 'Purdue', 'Nebraska']

Pac_12 = ['Arizona', 'Arizona St', 'California', 'Colorado', 'Oregon', 'Oregon St', \
          'Stanford' , 'UCLA', 'USC', 'Utah', 'Washington', 'Washington St']

Big_12 = ['Baylor', 'Iowa St', 'Kansas', 'Kansas St', 'Oklahoma', \
          'Oklahoma St', 'TCU', 'Texas', 'Texas Tech', 'West Virginia']

CUSA = ['Charlotte', 'FL Atlantic', 'Florida Intl', 'Louisiana Tech', 'MTSU', \
        'Marshall', 'North Texas', 'Old Dominion', 'Rice', 'Southern Miss', \
        'UAB', 'UT San Antonio', 'UTEP', 'WKU']

MAC = ['Akron', 'Ball St', 'Bowling Green', 'Buffalo', 'C Michigan', 'E Michigan', \
       'Kent', 'Miami OH', 'N Illinois', 'Ohio', 'Toledo', 'W Michigan']

Mountain_West = ['Air Force', 'Boise St', 'Colorado St', 'Fresno St', 'Hawaii', \
                 'Nevada', 'New Mexico', 'San Diego St', 'San Jose St' , 'UNLV', \
                 'Utah St', 'Wyoming']

Sun_Belt = ['Appalachian St', 'Arkansas St', 'Coastal Car', 'Ga Southern', \
            'Georgia St', 'South Alabama', 'Texas St', 'Troy', 'Louisiana', 'ULM'] #'ULL',

Independent = ['Army', 'BYU', 'Liberty', 'Massachusetts', 'New Mexico St']


AP_Top_25 = [ 'Clemson', 'Florida',  'Georgia', 'Kentucky', 'Ohio St', 'Notre Dame', \
             'Oklahoma', 'LSU', 'Texas', 'Washington', 'Washington St', 'UCF' , \
             'Syracuse', 'Michigan', 'Texas A&M', 'Alabama', 'Penn St', 'Fresno St', \
             'Army', 'West Virginia', 'Northwestern', 'Utah St', 'Boise St', 'Iowa' ]


Power_5 ={'Big_Ten':Big_Ten, 'ACC':ACC, 'SEC':SEC, 'Big_12':Big_12, 'Pac_12':Pac_12}

G5={ 'AAC':AAC, 'CUSA':CUSA,'MAC':MAC, \
    'Mountain_West':Mountain_West, 'Sun_Belt':Sun_Belt,'Independent':Independent }

conferences = G5 #CHANGE

defenses = pd.read_csv(defense_loc)
offenses = pd.read_csv(offense_loc)
teams = pd.read_csv(team_file_loc)



#print(teams['FBS Teams'])
#print((np.concatenate(offenses[teams['FBS Teams'].iloc[3]+ ' Off'].to_frame().values)))
hist_off = {}
hist_def = {}
off_subplots = {}
def_subplots = {}

# Create distplot with custom bin_size

for (conf,c_list) in conferences.items():
    print(conf)
    hist_off[conf] = [np.concatenate(offenses[c_list[i] + ' Off'].to_frame().values) \
             for i in range(len(c_list))]
    hist_def[conf] = [np.concatenate(defenses[c_list[i] + ' Def'].to_frame().values) \
             for i in range(len(c_list))]
    off_labels = [c_list[i]+ ' Off' for i in range(len(c_list))]
    def_labels = [c_list[i]+ ' Def' for i in range(len(c_list))]
    
    off_subplots[conf] = ff.create_distplot(hist_off[conf], off_labels, bin_size=.03)
    def_subplots[conf] = ff.create_distplot(hist_def[conf], def_labels, bin_size=.03)
    


    off_subplots[conf]['layout'].update(xaxis =dict(title ='Rating'), yaxis = dict(title ='Rating Likelihood'), \
                title = conf + ' Offensive Skill 2018')
    def_subplots[conf]['layout'].update(xaxis =dict(title ='Rating'), yaxis = dict(title ='Rating Likelihood'), \
                title = conf + ' Defensive Skill 2018')
    
    off_subplots[conf] = off_subplots[conf]['data']
    def_subplots[conf] = def_subplots[conf]['data']
    



layout = go.Layout(barmode = 'overlay') #make the bar graphs wide


fig = tools.make_subplots(rows = len(conferences) , cols = 1, vertical_spacing = 0.11, \
                          subplot_titles = ('AAC Def', \
                                            'CUSA Def', \
                                            'MAC Def', \
                                            'Mountain West Def', \
                                            'Sun Belt Def ', \
                                            'Independent Def ')) #CHANGE

i=1
for (conf,c_list) in conferences.items():
    for j in range(len(c_list)):
        temp_hist = go.Histogram(def_subplots[conf][j], opacity = 0.6) #CHANGE
        fig.append_trace(temp_hist,i,1)  #draw histogram
        fig.layout.update(barmode = 'overlay')
        fig.append_trace(def_subplots[conf][len(c_list)+j],i,1) #draw distribution CHANGE
    i += 1

i=1
for conf in conferences: #add axis labeling
    fig['layout']['xaxis'+str(i)].update(title='Rating', range=[-.05,0.9])
    fig['layout']['yaxis'+str(i)].update(title='Likelihood', range=[0,12])
    fig['layout']['xaxis'+str(i)].title.font.size = 12
    i+=1
    
    
    

fig['layout'].update(title='Group of Five Defensive Skill 2018') #CHANGE
# Plot!
py.iplot(fig, filename='Group of Five Defensive Skill 2018.html') #CHANGE
