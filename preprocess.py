import re

def preprocess_filter(sentList):
	# Stores all the filter sentences
	alphaStrings = []

	for sen in sentList:

	    # Removing html tags
		sentence = remove_tags(sen)

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

TAG_RE = re.compile(r'<[^>]+>')

def remove_tags(text):
    return TAG_RE.sub('', text)