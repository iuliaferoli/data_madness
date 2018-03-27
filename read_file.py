import os
from pandas import DataFrame as df
import re


path = os.getcwd() + "\data"
house_names = {"baratheon":0 ,"lannister":0 ,"stark":0 ,"targaryen":0, "tyrell":0}
subtitles = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: []}
delete = '"0123456789:.,!?\\-_'


def create_dataframe(house_names):
	data = ["season", "episode"] 
	for key,name in house_names.items():
		data.append(key)
	frame = df(columns=data)
	return frame

initial = create_dataframe(house_names)
print(initial)

def read_file(path, subtitles, delete, house_names, df, DEBUG = False):
	
    for i in subtitles:
        with open(path + "\season" + str(i+1) + ".json") as infile:
            count_episodes = 0
            episode = ""
            response = [0] * len(house_names)
            for line in infile:
                if line.find(" }") >= 0 :
                    subtitles[i].append(episode)
                    episode = ""
                    row = [i, count_episodes] + response
                    df.loc[len(df)]=row
                    response = [0] * len(house_names)
                    count_episodes += 1
                    next(infile)
                elif line.find("{") < 0:
                    line = ''.join( c for c in line if  c not in delete + "'").strip().lower()
                    line = re.sub(r'</?[i|b]>', "", line)
                    line = re.sub(r"\(.*\)", "", line)
                    line = re.sub(r"</?font(.*)>", "", line)
                    line = re.sub(r".* sync .* by .*", "", line)
                    line = re.sub(r".* original .* date .* ", "", line)
                    if line != "" :
                        episode += line + "\n"
                        print(line)
                        response = count_house_occurances(line, house_names, response)	
    if DEBUG:   
       print (subtitles[2][5][3])
    #subtitles [season 1: [ [episode], [episode], [episode] ], season2 [[] [] [] ], season 3 [[] [] [] ]
    #count from 0 so print (subtitles[2][5][3]) season 3 episode 6 line 4

    return subtitles

def count_house_occurances(line, house_names, response):
	for word in line.split():
		if word in house_names:
			house_names[word]+=1
	for i,house in enumerate(house_names):
		response[i] += house_names[house]
	return response



read_file(path, subtitles, delete, house_names, initial, False)
print(initial)
