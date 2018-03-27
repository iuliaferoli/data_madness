path = "C:/Users/ife/OneDrive - Mediaan abs b.v/UNI/block 4/Data analysis/data madness/"

subtitles = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: []}

for i in subtitles:
	with open(path + "season" + str(i+1) + ".json") as infile:
		episode = []

		for line in infile:
			if line.find(" }") > 0 :
				subtitles[i].append(episode)
				episode = []
				next(infile)
			elif line.find("{") < 0:
				episode.append(line)



print (subtitles[2][5][3])

#subtitles [season 1: [ [episode], [episode], [episode] ], season2 [[] [] [] ], season 3 [[] [] [] ]
#count from 0 so print (subtitles[2][5][3]) season 3 episode 6 line 4