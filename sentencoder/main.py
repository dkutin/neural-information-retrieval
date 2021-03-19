# Import numpy and torch.
import numpy as np
import torch
import nltk

from random import randint
from models import InferSent

# Import helper functions
from preprocess import importQuery, importTweets, buildIndex, lengthOfDocument

nltk.download('punkt')


V = 1
MODEL_PATH = 'encoder/infersent%s.pkl' % V
params_model = {'bsize': 64, 'word_emb_dim': 300, 'enc_lstm_dim': 2048,
                'pool_type': 'max', 'dpout_model': 0.0, 'version': V}
infersent = InferSent(params_model)
infersent.load_state_dict(torch.load(MODEL_PATH))

def main():
    print("\n CSI 4107 - Microblog information retrieval system \n")

    print("\n Preprocessing... \n")
    # Load the tweet list.
    # {'34952194402811904': 'Save BBC World Service from Savage Cuts http://www.petitionbuzz.com/petitions/savews', ...}
    tweets = importTweets()

    # Load the list of queries.
    # {1: ['bbc', 'world', 'servic', 'staff', 'cut'], ...}
    query_file = importQuery()

    infersent.build_vocab(tweets, tokenize=False)

    infersent.visualize('A man plays an instrument.', tokenize=True)

    print("\n Retrieval and Ranking Done! \n")


if __name__ == "__main__":
    main()
