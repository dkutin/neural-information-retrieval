# Main imports.
import types

# Import specific packages.
from preprocess import importTweets,importQuery
from nltk.corpus import stopwords
from scipy import spatial
from sent2vec.vectorizer import Vectorizer

def main():
	# "We can interchangeably use embedding, encoding, or  http://url.com/bla1/blah1/ vectorizing.",
	# "ReThink Group positive in outlook: Technology staffing specialist the ReThink Group expects revenues to be marg... https://bit.ly/hFjtmY"
	# sentences = [
	#     "bbc world servic savag cut ",
	#     "bbc world servic staff cut ",
	# ]
	# Load the tweet list.
    # {'34952194402811904': 'Save BBC World Service from Savage Cuts ', ...}
	tweets = importTweets(True)
	# print(tweets)
	queries = importQuery(True)
	# print(queries)

	# vectorizer = Vectorizer()
	# vectorizer.bert(sentences)
	# vectors_bert = vectorizer.vectors
	# dist = spatial.distance.cosine(vectors_bert[0], vectors_bert[1])
	# print(dist)

	# for tkey, tvalue in tweets.items():
	# 	for qkey, qvalue in queries.items():
	# 		print("(DOC):",tvalue)
	# 		print("(QUERY):",qvalue)
	# 		break
	# 	break
			# vectorizer_tweet = Vectorizer()
			# vectorizer_tweet.bert(tvalue)
			# vectors_bert_tweet = vectorizer_tweet.vectors

			# vectorizer_query = Vectorizer()
			# vectorizer_query.bert(qvalue)
			# vectors_bert_query = vectorizer_query.vectors

			# dist = spatial.distance.cosine(vectors_bert_tweet[0], vectors_bert_query[0])
	# 		# dist_2 = spatial.distance.cosine(vectors_bert[0], vectors_bert[2])
	# 		# print('dist_1: {0}, dist_2: {1}'.format(dist_1, dist_2))
	# 		# dist_1: 0.043, dist_2: 0.192
	# 		print("Doc_key", tkey," Query key" ,qkey, "Distance", dist)
	tlist = list(tweets.values())
	vectorizer_tweet = Vectorizer()
	vectorizer_tweet.bert(tlist)
	vectors_bert_tweet = vectorizer_tweet.vectors

	qlist = list(queries.values())
	vectorizer_query = Vectorizer()
	vectorizer_query.bert(qlist)
	vectors_bert_query = vectorizer_query.vectors

	dist = spatial.distance.cosine(vectors_bert_tweet[0], vectors_bert_query[0])
	print(dist)
if __name__ == "__main__":
    main()