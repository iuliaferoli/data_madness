import math
from textblob import TextBlob as tb
import read_file_in_one_block as rd
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords


def tf(word, document):
    return document.split().count(word) / len(document.split())

def n_containing(word, corpus):
    return sum(1 for document in corpus if word in document.split())

def idf(word, corpus):
    return math.log(len(corpus) / (1 + n_containing(word, corpus)))

def tfidf(word, document, corpus):
    return tf(word, document) * idf(word, corpus)

subtitles = rd.read_file(rd.path + "//data//", False)
df = rd.convert_to_df(subtitles)
#print(df)


corpus = []
ps = PorterStemmer()


#combine episodes together to create 7 season
d={'episode': 'sum', 'text': 'sum'}
df_new = df.groupby("season", as_index=False).aggregate(d)
print(df_new)

for index, row in df_new.iterrows():
	filtered_words = str([ps.stem(word) for word in row["text"].split() if word not in stopwords.words('english')]).replace(",", "").replace("'", "")
	#print(filtered_words)
	corpus.append(tb(filtered_words))



for index, document in enumerate(corpus):
	print("Top words in episode ", index+1," :")
	for word in document.split():
		scores = {word: tfidf(word, document, corpus)}
	sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
	for word, score in sorted_words[:20]:
		print(word, ", ", score)
