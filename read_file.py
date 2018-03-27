import os
from pandas import DataFrame as df


path = os.getcwd() + "\data"
house_names = {"arryn":[] ,"baratheon":[] ,"frey":[] ,"greyjoy":[] ,"lannister":[] ,"martell":[] ,"stark":[] ,"targaryen":[] ,"tully":[],"tyrell":[] }
subtitles = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: []}
delete = '"0123456789:.,!?\\-_'


def create_dataframe(house_names):
	data = ["season", "episode"] 
	for key,name in house_names.items():
		data.append(key)
	houses = df(columns=data)
	return houses
	#print(houses)

house = create_dataframe(house_names)
print(house)

def read_file(path, subtitles, delete, house_names, house, DEBUG = False):
	
    for i in subtitles:
        with open(path + "\season" + str(i+1) + ".json") as infile:
            count_episodes = 0
            episode = []
            response = [0] * len(house_names)
            for line in infile:
                if line.find(" }") >= 0 :
                    subtitles[i].append(episode)
                    episode = []
                    count_episodes += 1
                    next(infile)
                    house.oc[len(house)]=[i, count_episodes].extend(response)
                    response = [0] * len(house_names)

                elif line.find("{") < 0:
                    line = ''.join( c for c in line if  c not in delete + "'" + r'\(\s\w*\s\)').strip().lower()
                    response += count_house_occurances(line, house_names, response)
                    episode.append(line)
                    
    if DEBUG:   
       print (subtitles[2][5][3])
    #subtitles [season 1: [ [episode], [episode], [episode] ], season2 [[] [] [] ], season 3 [[] [] [] ]
    #count from 0 so print (subtitles[2][5][3]) season 3 episode 6 line 4

    return subtitles

def count_house_occurances(line, house_names, response):
	for i,name in enumerate(house_names):
		count = 0
		for word in line.split():	
			#print (word)
			if word.find(name) >= 0:
				count += 1
		response[i] += count
	return response


read_file(path, subtitles, delete, house_names, house, False)

print (house)