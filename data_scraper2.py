# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import re
from pandas import DataFrame as df
import read_file_in_one_block

path = read_file_in_one_block.path + '\\data\\'

''' get soup '''
def get_soup(url):
    content = requests.get(url).content
    return BeautifulSoup(content,'lxml') # choose lxml parser


''' main section '''
if __name__ == '__main__':

    rankings_df = df({'season':[],'episode':[],'rank':[]})
    
    for i in range(1,8):
        url2= 'http://www.imdb.com/title/tt0944947/episodes?season=' + str(i)
        soup = get_soup(url2)
        
        rankings=[]
        for span_tag in soup.find_all("span",  {'class' : 'ipl-rating-star__rating'}):
            link = span_tag.text
            if '.' in link :
                rankings.append(link)
            
        for div in soup.find_all("div", {'class': 'list detail eplist'}):
            text = div.text            
            season_episode = re.findall(r"S[0-9], Ep[0-9]*", div.text)
                
        ranking_dict = df({'season_episode': season_episode, 'rank': rankings})
        ranking_dict['season'], ranking_dict['episode'] = ranking_dict['season_episode'].str.split(',', 1).str
        ranking_dict = ranking_dict.drop('season_episode', axis = 1)
        ranking_dict['season'] = ranking_dict['season'].str.split('S').str.get(1)
        ranking_dict['episode'] = ranking_dict['episode'].str.split('p').str.get(1)
        
        rankings_df = rankings_df.append(ranking_dict)
        rankings_df
        print("done with season " + str(i))
        
    rankings_df.to_csv(path + 'info.csv')
    
    
    
    