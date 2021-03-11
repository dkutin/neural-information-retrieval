# Main imports.
import nltk
import types

# Import specific packages.
from preprocess import filterSentence
from nltk.corpus import stopwords
from scipy import spatial
from sent2vec.vectorizer import Vectorizer

def main():
	stop_word_list = ['n\'t', '\'d', 'http', 'https', '//', '...']
	with open('./assets/stop_words.txt', 'r') as f:
		stop_word_list = [line.strip() for line in f]
	sentences = [
	    "Thishttp://url.com/bla1/blah1/ is an awe3some  t book to  whereby learn NLP.",
	    "DistilBERT is  yourself an amaz445ing NLP model.",
	    "We can interchangeably use embedding, encoding, or  http://url.com/bla1/blah1/ vectorizing.",
	    "ReThink Group positive in outlook: Technology staffing specialist the ReThink Group expects revenues to be marg... https://bit.ly/hFjtmY"
	]

	vectorizer = Vectorizer()
	vectorizer.bert(sentences)
	vectors_bert = vectorizer.vectors

	dist_1 = spatial.distance.cosine(vectors_bert[0], vectors_bert[1])
	dist_2 = spatial.distance.cosine(vectors_bert[0], vectors_bert[2])
	print('dist_1: {0}, dist_2: {1}'.format(dist_1, dist_2))
	# dist_1: 0.043, dist_2: 0.192

	print(filterSentence("Thishttp://url.com/bla1/blah1/ is an awe3some  t book to  whereby learn NLP."))

if __name__ == "__main__":
    main()