from preprocess import importQuery, importTweets, buildIndex, lengthOfDocument
import spacy
from nltk.corpus import wordnet
# Import helper functions
from results import retrieve
from write import resultFileCreation

nlp = spacy.load('en_core_web_lg')

# Creating the Corpus  First section



documents = importTweets()

queries = importQuery()[1]

def getSim(word, syn):
    tokens = nlp(' '.join([word, syn]))
    simOne, simTwo = tokens[0], tokens[1]

    return simOne.similarity(simTwo)


    return similarity_matrix.inner_product(simOne, simTwo, normalized=(True, True))

def getSyns(queryList):
    synonyms=[]
    for word in queryList:
        synsOfWord = []
        for syn in wordnet.synsets(word):
            for l in syn.lemmas():
                if l.name() not in synsOfWord:
                    synsOfWord.append(l.name())
        synonyms.append(synsOfWord)
    return synonyms


def canExpand(syn, queryList):
    count = 0
    thresh = 0.1
    for word in queryList:

        sim = getSim(word, syn)
        if sim >= thresh:
            count += 1
    return count >=2

def expand(query):
    newQuery = query.copy()
    syns = getSyns(query)
    for synWordList in syns:
        for synWord in synWordList:
            if canExpand(synWord, query) and synWord not in newQuery:
                newQuery.append(synWord)
    return newQuery

#print('-'*10)
# newQueryDict = dict()
# for queryIndex in queries:
#     expanded = expand(queries[queryIndex])
#     newQueryDict[queryIndex] = expanded
    # print('Base Query')
    # print(queries[queryIndex])
    # print('-'*10, '\n Expanded')
    # print(expanded)
    # print('\n\n')

def main():
    print("\n CSI 4107 - Microblog information retrieval system \n")

    print("\n Preprocessing... \n")
    # Load the tweet list.
    # {'34952194402811904': 'Save BBC World Service from Savage Cuts http://www.petitionbuzz.com/petitions/savews', ...}


    # Load the list of queries.
    # {1: ['bbc', 'world', 'servic', 'staff', 'cut'], ...}

    newQueryDict = dict()
    for queryIndex in queries:
        expanded = expand(queries[queryIndex])
        newQueryDict[queryIndex] = expanded

    # Build the inverted index.
    index = buildIndex(documents)

    # Get the length of each document.
    document_length = lengthOfDocument(index, documents)

    print("\n Preprocessing Done! \n")
    print("\n Retrieval and Ranking... \n")
    # Get length of query.
    ranking = retrieve(newQueryDict, index, document_length)

    print("\n Retrieval and Ranking Done! \n")

    print("\n Starting to create Result File... \n")

    resultFileCreation(ranking)

    print("\n Result File Creation Done! \n")


if __name__ == "__main__":
    main()











