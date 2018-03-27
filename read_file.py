path = "C:/Users/ife/OneDrive - Mediaan abs b.v/UNI/block 4/Data analysis/data madness/"

subtitles = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: []}

for i in subtitles:
	with open(path + "season" + str(i) + ".json") as infile:
		episode_number = 1
		episode = {episode_number : []}

		for line in infile:
			if line.find(" }") > 0 :
				subtitles[i].append(episode)
				episode_number = episode_number + 1
				episode = {episode_number : []}
				next(infile)
			elif line.find("{") < 0:
				episode[episode_number].append(line)

for line in subtitles[2][4]:
	print (line + "\n")


# season 1: [ {episode 1:[lines]}, {2:[]}, {3:[]} ]