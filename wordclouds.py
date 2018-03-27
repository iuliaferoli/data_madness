# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 15:40:05 2018

@author: ami
"""

import read_file_in_one_block
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

path = read_file_in_one_block.path + '\\data\\'
# read data from file
subtitles_dict = read_file_in_one_block.read_file(path)
# put in dataframe with columns: season episode text
subtitles = read_file_in_one_block.convert_to_df(subtitles_dict)

mask = np.array(Image.open(path+"crown.jpg"))
stopwords = set(STOPWORDS)
extra = ["said","dont", "hes", "im", "ive", "will"]
stopwords |= set(extra)

# make wordclouds for each episode
for index, row in subtitles.iterrows():
    text = row["text"]

    wc = WordCloud(background_color="white", max_words=100, mask = mask)
    # generate word cloud
    wc.generate(text)
    
    # store to file
    wc.to_file(path + "S" + str(row["season"]) + "_Ep" +  str(row["episode"]) + ".png")
    
    # show
    plt.imshow(wc, interpolation='bilinear')
    plt.axis("off")
    plt.figure()
    
# make wordclouds for each season
subt = subtitles.groupby('season').apply(lambda x: x.sum()).drop(['episode', 'season'], axis = 1)

for index,row in subt.iterrows():
    text = row["text"]
    
    wc = WordCloud(background_color="white", max_words=100, mask = mask)
    # generate word cloud
    wc.generate(text)
    
    # store to file
    wc.to_file(path + "S" + str(index) + ".png")
    
    # show
    plt.imshow(wc, interpolation='bilinear')
    plt.axis("off")
    plt.figure()
