import os

path = os.getcwd()

def read_file(path, DEBUG = False):

    subtitles = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: []}

    delete = '"0123456789:.,!?\\-_'
    

    for i in subtitles:
        with open(path + "season" + str(i+1) + ".json") as infile:
            episode = []

            for line in infile:
                if line.find(" }") >= 0 :
                    subtitles[i].append(episode)
                    episode = []
                    next(infile)
                elif line.find("{") < 0:
                    line = ''.join( c for c in line if  c not in delete + "'" + r'\(\s\w*\s\)').strip().lower()
                    episode.append(line)
                    
    if DEBUG:   
       print (subtitles[2][5][3])
    #subtitles [season 1: [ [episode], [episode], [episode] ], season2 [[] [] [] ], season 3 [[] [] [] ]
    #count from 0 so print (subtitles[2][5][3]) season 3 episode 6 line 4

    return subtitles
