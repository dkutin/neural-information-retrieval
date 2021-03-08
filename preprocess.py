# Main imports.
import re

def preprocess_filter(sentList):
	'''
	:param list of sentences: list of sentences from the queries or documents.
    	:return: the the input list with filtered sentences.
    	:rt list
    	'''

	# Stores all the filter sentences
	alphaStrings = []

	for sen in sentList:

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

	    	# Add the filter sentence to a list.
		alphaStrings.append(sentence)

	return alphaStrings
