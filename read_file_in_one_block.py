# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 15:31:56 2018

@author: ami
"""

import os
import re
import pandas as pd

path = os.getcwd()

def read_file(path, DEBUG = False):

    subtitles = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: []}

    delete = '#"0123456789:.,!?\\-_'
    

    for i in subtitles:
        with open(path + "season" + str(i+1) + ".json") as infile:
            episode = ""
            lines = []
            for line in infile:
                if line.find(" }") >= 0 :
                    episode = "".join(lines)
                    subtitles[i].append(episode)
                    episode = ""
                    lines = []
                    next(infile)
                elif line.find("{") < 0:
                    line = ''.join( c for c in line if  c not in delete + "'").strip().lower()
                    line = re.sub(r'</?[i|b]>', "", line)
                    line = re.sub(r"\(.*\)", "", line)
                    line = re.sub(r"</?font(.*)>", "", line)
                    line = re.sub(r".* sync .* by .*", "", line)
                    line = re.sub(r".* original .* date .* ", "", line)
                    if line != "" :
                        lines.append(line + " ")

    if DEBUG:   
       print (subtitles[2][5][3])
    #subtitles [season 1: [ [episode], [episode], [episode] ], season2 [[] [] [] ], season 3 [[] [] [] ]
    #count from 0 so print (subtitles[2][5][3]) season 3 episode 6 line 4

    return subtitles


def convert_to_df(subtitles_dict):
    seasons=[]
    episodes=[]
    data=[]
    for i,season in enumerate(subtitles_dict):
    	for j,episode in enumerate(subtitles_dict[season]):
    		seasons.append(season+1)
    		episodes.append(j+1)
    		data.append(subtitles_dict[i][j])
    
    df = pd.DataFrame({'season':seasons, 'episode':episodes, 'text':data})
    
    return df
