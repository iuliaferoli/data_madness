# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 19:23:59 2018

@author: ami
"""

import read_file_in_one_block

path = read_file_in_one_block.path + '\\data\\'
# read data from file
subtitles_dict = read_file_in_one_block.read_file(path)
# put in dataframe with columns: season episode text
subtitles = read_file_in_one_block.convert_to_df(subtitles_dict)

# make list of profane words
profane_words = ['dunghole', 'balls', 'prick', 'twat', 'bitch','whore', 
                 'bastard', 'slut',  'cunt', 'arse', 'tits', 'crap', 'cock', 
                 'fuck', 'piss', 'damn', 'hell', 'shit']

# count profane words per episode 
for word in profane_words:
    subtitles[word] = [subtitles["text"].iloc[index].count(word) for index,row in subtitles.iterrows()]
    

