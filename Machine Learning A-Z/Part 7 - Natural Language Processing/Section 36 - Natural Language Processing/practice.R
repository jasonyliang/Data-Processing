# Natural Language Processing

# Importing dataset
dataset = read.delim('Restaurant_Reviews.tsv', quote = '', stringsAsFactors = FALSE)

# Cleaning the text
library(tm)
corpus = VCorpus(VectorSource(dataset$Review))