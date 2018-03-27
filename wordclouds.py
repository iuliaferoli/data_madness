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
subtitles_dict = read_file_in_one_block.read_file(path)
subtitles = read_file_in_one_block.convert_to_df(subtitles_dict)

text = subtitles["text"].iloc[0]


# read the mask image
# taken from
# http://www.stencilry.org/stencils/movies/alice%20in%20wonderland/255fk.jpg
mask = np.array(Image.open(path+"crown.jpg"))

stopwords = set(STOPWORDS)
extra = ["said","dont", "hes", "im", "ive", "will"]
stopwords |= set(extra)

wc = WordCloud(background_color="white", max_words=100, mask = mask)
# generate word cloud
wc.generate(text)

# store to file
wc.to_file(path + "crown.png")

# show
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.figure()
