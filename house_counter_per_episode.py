import read_file
from pandas import DataFrame as df

subtitles = read_file.read_file(read_file.path)

seasons = []
episodes = []
empty = []
house_names = {"arryn":[] ,"baratheon":[] ,"frey":[] ,"greyjoy":[] ,"lannister":[] ,"martell":[] ,"stark":[] ,"targaryen":[] ,"tully":[],"tyrell":[] }

for i,season in enumerate(subtitles):
	for j,episode in enumerate(subtitles[season]):
		seasons.append(season+1)
		episodes.append(j+1)
		empty.append("")

def count_house_occurances(line, house_names):
	response = []
	for name in house_names:
		count = 0
		for word in line.split():	
			print (word)
			if word.find(name) >= 0:
				count += 1
		response.append(count)
	return response

"""
test = "stark stark baratheon frey nope maybe tully i love frey"
print(count_house_occurances(test, house_names))
"""

data = {"season": seasons, "episode": episodes}
for i,name in enumerate(house_names):
	data[house_names[i]] = empty
houses = df(data=data)
print(houses)



