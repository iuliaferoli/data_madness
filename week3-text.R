#Change path to where you work and save your files
setwd("~/Dropbox/MST_COURSES/KEN3450/week3/")
library("plyr")
library("ggplot2")
library("wordcloud")
library("RColorBrewer")
library("tm")
library("SnowballC")

###Get the data
# from: http://www.wvgazettemail.com/
data <- readLines("https://www.r-bloggers.com/wp-content/uploads/2016/01/vent.txt")
df <- data.frame(data)
textdata <- df[df$data, ]

### Next, we remove nonessential characters such as punctuation, numbers, web addresses,
### etc from the text, before we begin processing

#regular expressions
textdata = gsub("[[:punct:]]", "", textdata)
textdata = gsub("[[:digit:]]", "", textdata)
textdata = gsub("http\\w+", "", textdata)
textdata = gsub("[ \t]{2,}", "", textdata)
textdata = gsub("^\\s+|\\s+$", "", textdata)

#word clouds: using "tm" package and "wordcloud" package.
#convert our data frame to a "Corpus" object to be handled by tm package
corpus = Corpus(VectorSource(textdata))
#inspect some of the data in the corpus
inspect(corpus)
corpus[[1]]$content

#tm package offers all the necessary pre-processing tools
#Removing punctuation (it's already removed by the regular expressions applied before)
corpus <- tm_map(corpus, removePunctuation)   

#You can also check here for any "hand-picked" regular expressions
for(j in seq(corpus))   
{   
  corpus[[j]] <- gsub("/", " ", corpus[[j]])   
  corpus[[j]] <- gsub("@", " ", corpus[[j]])   
  corpus[[j]] <- gsub("\\|", " ", corpus[[j]])   
}   

#Removing numbers:
corpus <- tm_map(corpus, removeNumbers)   

#Converting to lowercase:
corpus <- tm_map(corpus, tolower)   

#Removing stop-words
#see the list below (also it's available for other languages, or you can define your own file)
length(stopwords("english"))   
#stopwords("english")   
corpus <- tm_map(corpus, removeWords, stopwords("english"))   

#Removing (any other) particular words:
corpus <- tm_map(corpus, removeWords, c("department", "email")) 

#Snowball package offers stemming possibilities
corpus <- tm_map(corpus, stemDocument)   

#usually pre-processing with the above steps, leaves too much whitespace
#luckily, it can be removed

corpus <- tm_map(corpus, stripWhitespace)   
# inspect(docs[3]) # Check to see if it worked.   

#end the pre-processing by telling R that you processed everything as Plain Text
corpus_plain <- tm_map(corpus, PlainTextDocument)
alltexts=corpus_plain[[1]]$content
#or this might also be useful for individual records
corpus_plain_other <- strwrap(corpus[[1]])

#create a term document matrix (notice that this should be on the corpus object)
tdm = TermDocumentMatrix(corpus)
#converting tdm object to a normal matrix to be handled by us
tdm = as.matrix(tdm)
#check the structure and the dimensions of tdm now

#sort array by the most frequent terms
v <- sort(rowSums(tdm),decreasing=TRUE)
#create a list with names of terms and their frequency
d <- data.frame(word = names(v),freq=v)

wordcloud(d$word,d$freq)

#A bigger cloud with a minimum frequency of 2
wordcloud(d$word,d$freq,c(8,.3),2)

#Now lets try it with frequent words plotted first
wordcloud(d$word,d$freq,c(8,0.5),2,,FALSE,0.1)
#If at any point you want to convert the corpus back to a point:
X=data.frame(text = sapply(corpus, as.character), stringsAsFactors = FALSE)
#From this point on, you can:
#1. Explore your data (go through the tdm matrix)
#2. Remove sparse terms:  use removeSparseTerms (from tm package)
#3. Compute frequencies of the most and least occuring words
#4. Find frequent terms:  use findFreqTerms (from tm package)
#5. Plot word frequencies (e.g. plot words that appear at least 5 times)
#6. Find frequent words in each document
#7. Find relationships between terms: use findAssocs (from tm package)