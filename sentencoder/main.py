# Import numpy and torch.
import numpy as np
import torch
import nltk

from random import randint
from models import InferSent

# Import helper functions
from preprocess import importQuery, importTweets
from write import resultFileCreation

nltk.download('punkt')

V = 1
MODEL_PATH = 'encoder/infersent%s.pkl' % V
W2V_PATH = 'GloVe/glove.840B.300d.txt'
params_model = {'bsize': 64, 'word_emb_dim': 300, 'enc_lstm_dim': 2048,
                'pool_type': 'max', 'dpout_model': 0.0, 'version': V}


def cosine(u, v):
    '''
    Calculate the Cosine Similarity between two Vectors

    :param u, v: Vectors to be compared.
    :return: The Cosine Similarity between u and v.
    :rtype: float
    '''
    return np.dot(u, v) / (np.linalg.norm(u) * np.linalg.norm(v))

def main():

    # Dictionary for Final Rankings.
    ranking = dict()

    print("\n CSI 4107 - Microblog information retrieval system \n")

    print("\n Importing Query Files and Documents... \n")

    # Load the tweet list.
    # {'34952194402811904': 'Save BBC World Service from Savage Cuts http://www.petitionbuzz.com/petitions/savews', ...}
    tweets_dict = importTweets()

    # Load the list of queries.
    # {1: ['bbc', 'world', 'servic', 'staff', 'cut'], ...}
    queries_dict = importQuery()

    print("\n Importing Done! \n")

    print("\n Initializing InferSent Model... \n")

    # Initialize InferSent Model.
    infersent = InferSent(params_model)

    # Load Infersent v1 Model Encoder.
    infersent.load_state_dict(torch.load(MODEL_PATH))

    # Load Pre-trained GloVe Model.
    infersent.set_w2v_path(W2V_PATH)

    print("\n InferSent Initialization Done! \n")

    print("\n Building Vocabulary from Tweets... \n")

    tweets = list(tweets_dict.values())
    infersent.build_vocab(tweets, tokenize=False)

    print("\n Vocabulary Completed! \n")

    print("\n Retrieval and Ranking... \n")
    embeddings = infersent.encode(tweets, bsize=128, tokenize=False, verbose=True)

    current_query = 1
    for query_id, query in queries_dict.items():
        dranking = dict()
        for document_id, tweet in tweets_dict.items():
            # Calculate the Cossine Sim
            dranking[document_id] = cosine(infersent.encode([tweet])[0], infersent.encode([query])[0])

        # Put the ranking of Documents in Descending order into ranking.
        ranking[query_id] = {k: v for k, v in sorted(dranking.items(), key=lambda dranking: dranking[1], reverse=True)[:1000]}

        print ("Query " + str(current_query) + " Done.")
        current_query += 1

    print("\n Retrieval and Ranking Done! \n")

    print("\n Creating Result File... \n")

    resultFileCreation(ranking)

    print("\n File Creation Done! Find the results in ./dist/Results.txt for further eval. \n")

if __name__ == "__main__":
    main()
