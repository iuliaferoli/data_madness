# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 20:40:53 2018

@author: ami
"""

import read_file_in_one_block
from pandas import DataFrame as df
import pandas as pd

path = read_file_in_one_block.path + '\\data\\'
# read data from file
subtitles_dict = read_file_in_one_block.read_file(path)
# put in dataframe with columns: season episode text
subtitles = read_file_in_one_block.convert_to_df(subtitles_dict)

subtitles['number of words'] = [len(subtitles["text"].iloc[index].split()) for index,row in subtitles.iterrows()]

# read IMDB ratings from file
ratings = df.from_csv(path+'info.csv')

# merge ratings and number of words per episode
df = pd.merge(ratings, subtitles, on = ['season', 'episode'])

df.to_csv(path + 'ratings_vs_wordcount.csv')
print("created ratings_vs_wordcount.csv at: " + path)
