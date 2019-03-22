# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 22:36:29 2019

@author: NATE
This program creates a collection of histograms of offensive and 
defensive ratings. The rating system was developed by me. The ratings histograms
 represent a distribution of skill which a given team can play at. 
These ratings are for power5/G5 conferences. Team offensive and defensive skill
 can be compared across the same conference.
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
       'Virginia', 'Virginia Tech', 'Wake Forest']

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

Independent = ['Army', 'BYU', 'Liberty', 'Massachusetts', 'New Mexico St', 'Notre Dame']


AP_Top_25 = [ 'Clemson', 'Florida',  'Georgia', 'Kentucky', 'Ohio St', 'Notre Dame', \
             'Oklahoma', 'LSU', 'Texas', 'Washington', 'Washington St', 'UCF' , \
             'Syracuse', 'Michigan', 'Texas A&M', 'Alabama', 'Penn St', 'Fresno St', \
             'Army', 'West Virginia', 'Northwestern', 'Utah St', 'Boise St', 'Iowa' ]


Power_5 ={'Big_Ten':Big_Ten, 'ACC':ACC, 'SEC':SEC, 'Big_12':Big_12, 'Pac_12':Pac_12}

G5={ 'AAC':AAC, 'CUSA':CUSA,'MAC':MAC, \
    'Mountain_West':Mountain_West, 'Sun_Belt':Sun_Belt,'Independent':Independent }

conferences =G5 #CHANGE

defenses = pd.read_csv(defense_loc)
offenses = pd.read_csv(offense_loc)
teams = pd.read_csv(team_file_loc)



    
#cycle through conferences and create histograms for each one and upload it
for (conf,c_list) in conferences.items():
    print(conf)
    hist_data = [np.concatenate(defenses[c_list[i] + ' Def'].to_frame().values) \
             for i in range(len(c_list))] #CHANGE
    group_labels = [c_list[i]+ ' Def' for i in range(len(c_list))] #CHANGE
    # Create distplot with custom bin_size
    fig = ff.create_distplot(hist_data, group_labels, bin_size=.03, show_rug=False)
    fig['layout']['xaxis'].update(title='Rating')
    fig['layout']['yaxis'].update(title='Likelihood')
    fig['layout'].update(title=conf + ' Defense') #CHANGE
    # Plot!
    py.iplot(fig, filename=conf + ' Defensive Skill Distributions 2018') #CHANGE





