# Main imports.
import re

def importTweets():
    ''' 
    Import tweets from collection.

    :return: the tokenized list of queries.
    :rtype: list
    '''
    tweet_list = dict()
    # Splits tweet list at newline character.
    tweets = (line.strip('\n') for line in open('./assets/tweet_list.txt', 'r', encoding='utf-8-sig'))

    # Build the dictionary.
    for tweet in tweets:
        key, value = tweet.split('\t')
        # Tokenize each tweet, and put back in list.
        tweet_list[key] = filterSentence(value)

    return tweet_list

def filterSentence(sen):
	'''
	:param list of sentences: list of sentences from the queries or documents.
	:return: the the input list with filtered sentences.
	:rt string
	'''

    # Removing html tags
	TAG_RE = re.compile(r'<[^>]+>')
	sentence = TAG_RE.sub('', sen)

	# Remove stop words
	with open('./assets/stop_words.txt', 'r') as f:
		stopWords = [line.strip() for line in f]
	sentWords = sentence.split()
	nonStopwords  = [word for word in sentWords if word.lower() not in stopWords]
	sentence = ' '.join(nonStopwords)

	# Remove links
	sentence = re.sub(r'http\S+', '', sentence)

    # Remove numbers
	sentence = re.sub(r'[0-9]', '', sentence)

	# Remove punctuation
	sentence = re.sub(r'[^\w\s]', '', sentence)

    # Single character removal
	sentence = re.sub(r"\s+[a-zA-Z]\s+", ' ', sentence)

    # Removing multiple spaces
	sentence = re.sub(r'\s+', ' ', sentence)


	return sentence
