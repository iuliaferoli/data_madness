import read_file
from pandas import DataFrame as df

# use data frames season column, episode columnd, 1 1 sort of keys

subtitles = read_file.read_file(read_file.path + '\\data\\')

seasons = []
episodes = []
empty = []


for i,season in enumerate(subtitles):
	for j,episode in enumerate(subtitles[season]):
		seasons.append(season+1)
		episodes.append(j+1)
		empty.append("")



"""
test = "stark stark baratheon frey nope maybe tully i love frey"
print(count_house_occurances(test, house_names))
"""

data = {"season": seasons, "episode": episodes}
for i,name in enumerate(house_names):
	data[house_names[i]] = empty
houses = df(data=data)
print(houses)



