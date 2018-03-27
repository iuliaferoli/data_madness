import re
import read_file_in_one_block

path = read_file_in_one_block.path + '\\data\\'
# read data from file
subtitles_dict = read_file_in_one_block.read_file(path)
# put in dataframe with columns: season episode text
subtitles = read_file_in_one_block.convert_to_df(subtitles_dict)

# make list of profane words
house_names = ["arryn", "baratheon","grejoy", "lannister","stark" ,"targaryen", "tyrell", "frey", "tully"]

# count profane words per episode 
for word in house_names:
    subtitles[word] = [subtitles["text"].iloc[index].count(word) for index,row in subtitles.iterrows()]
    
subtitles.to_csv(path + 'house_names.csv')
print("created house_names.csv at: " + path)
