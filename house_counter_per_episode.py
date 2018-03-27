import read_file
from pandas import DataFrame as df

# use data frames season column, episode columnd, 1 1 sort of keys

subtitles = read_file.read_file(read_file.path)

seasons = []
episodes = []
empty = []
house_names = ["arryn" ,"baratheon" ,"frey" ,"greyjoy" ,"lannister" ,"martell" ,"stark" ,"targaryen" ,"tully" ,"tyrell" ]

for i,season in enumerate(subtitles):
	for j,episode in enumerate(subtitles[season]):
		seasons.append(season+1)
		episodes.append(j+1)
		empty.append("")

data = {"season": seasons, "episode": episodes}
for i,name in enumerate(house_names):
	data[house_names[i]] = empty
houses = df(data=data)
print(houses)

