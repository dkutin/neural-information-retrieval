# Functionality of the BERT program
Our task for this assignment was to implement improved versions of the Information Retrieval (IR) system we created in Assignment 2, for a collection of documents (Twitter messages). A quick recap of what our BERT code does as a whole is as follows:

1. We import both the data files, one with the test queries and the other with the list of tweets to format the information to a Python code readable manner and to organize the words for our functions to read (we used dictionaries to store the data). This step also runs the words through a stemming and stop word removal process that basically stems all the words and handles the removal of stop words from the list of words.

2. We use a BERT model to embed the Query and Document words (tweets) within each sentence. This step is done in batches to soften the load on the CPU when running the whole data set, especially for the 40,000+ documents.

3. We calculate the CosSim similarity using the Cosine similairty calculator from the Scipy dictionary to calculate the `CosSim` for the tweets, to find their similarity score to the query. We order the tweets in a dictionary from highest to lowest similarity score and pass this information to step 4.

4. We organize the data created from step 3 and writes the information of the top 1000 for each query in the right order to a .txt file (dist/bert/bert_results.txt).

# Discussion if our BERT program achieved better results than in Assignment 1.
- Our BERT program did not perform as well as our results in Assignment 1, scoring a p_10 TREC score of 0.1769 in comparison to 0.1833 which was the score we got for Assignment 1. The MAP value for Assignment 1 was 0.1679 and the BERT approach MAP value is 0.0880. We belive this makes sense due to how BERT calculates the similairity of the different sentences. Firstly, BERT's evaluation changes based on the sequence or order of the words in the sentecen since it looks as the words beside the word, on the left and right during the evaluation, whereas in Assignment 1 the order didn't matter. As long as the document had all the words the query had, it was consider 100% similar, specailly when calculation the cosine similarity. This is the biggest reason we came to based on the final results.

- Furthermore there is always possibilities the model misinterpreted the words within the sentences as other developers have mentioned when using the BERT model. Where the BERT approach may result in good scores but its sensitivitly of the answer or understanding in a commonsense scenario as not the same as a person would have when creating the whole picture.

# Algorithms, data structures and optimizations used. 
  Our implementation of the information retrieval system was based on the guidelines provided in assignment 2. The bert folder contains four python files containing the functions used in implementing BERT Neural IR system. 

## Project Specific Files

### `main.py`:
In the `main()` function, we started by importing the important functions that were used for implementing the IR system. The first step was to import the tweets and the queries from the `assert folder`. By importing the tweets and queries from the `asset folder`, `step1: preprocessing` was being done using the `filterSentence` that was implemented directly in the `import` function. After importing the tweets and queries from the text and then filtering them.
Next, 'step2: word embedding' is done where we embed the words from the queries and documents with the BERT model. Once the embedding is done we calculate the Cosine Similarity scores for the word embedded Documents and Queries. To understand what was happening in the `main()` function, we created a set of print statements that would notify the user when the preprocessing and the embedding of the document and queries are done. The user then gets informed of the creation of the BERT result file. 

### `Preprocess.py`:
 This file contains the process of developing `step1:Preprocessing` using python. Below are the functions implemented in the `preprocess.py`

 - importTweets(bertMode = False): imports the tweets from the collection. We first started by opening the text files, then we filter the file using our filterSentence function. The bertMode variable is for then thw filterSentence function is called.

 - importQuery(bertMode = False): imports query from the collection. Same process as the importTweet(). The bertMode variable is for then thw filterSentence function is called.

 - filterSentence(sen, bertMode = False): Filters sentences from tweets and queries. This function builds a list of `stopwords` and then `tokenizes` each word in the sentences by removing any numerics, links, single characters, punctuation, extra spaces or stopwords contained in the list. Each imported tweet and query runs through the `NLTK's stopword list`, our `custom stopword list` that included the `URLs and abbreviations`, and the provided `stopword list`. After this step, each word is tokenized and stemmed with `Porter stemmer`. Under the `additional libraries` section, we discussed in-depth the use of `tokenization`, `stopwords`, and `porter stemmer`. If this function is in bertMode a string in returned with all thr remaining words otherwise a tokenized list of all the remaining words are returned.

 - listToString(list): Converts a list of words into a string.

### write.py:
  This file contains the procedure for implementing `step4`. The function creates a table for each of the results generated in the `bert_results.py` and then stores it in the `dist/bert folder` as a text file.

## Additional Libraries

### Prettytable (`prettytable.py`):  
A helper library to format the output for the `Results.txt` file. Used in the implementation of the `write.py`.

## Provide the first 10 answers to query 3 and 20
### First 10 answer for Query 3
Topic_id  Q0  docno              rank  score                tag 
3         Q0  34410414846517248  1     0.9017896056175232   myRun 
3         Q0  35088534306033665  2     0.9016108512878418   myRun 
3         Q0  32910196598636545  3     0.8939297199249268   myRun 
3         Q0  35032969643175936  4     0.8846487402915955   myRun 
3         Q0  34728356083666945  5     0.8838127851486206   myRun 
3         Q0  33254598118473728  6     0.8827221989631653   myRun 
3         Q0  34982904220237824  7     0.8695272207260132   myRun 
3         Q0  33711164877701120  8     0.8682869672775269   myRun 
3         Q0  34896269163896832  9     0.8675245046615601   myRun 
3         Q0  32809006015713280  10    0.867477297782898    myRun 
### First 10 answer for Query 20
Topic_id  Q0  docno              rank  score                tag 
20        Q0  33356942797701120  1     0.9473576545715332   myRun 
20        Q0  32672996137111552  2     0.9401946067810059   myRun 
20        Q0  33983287403745281  3     0.9358925223350525   myRun 
20        Q0  34048315318345728  4     0.9331563711166382   myRun 
20        Q0  29958466130939904  5     0.9306454658508301   myRun 
20        Q0  29394885203206144  6     0.930182933807373    myRun 
20        Q0  34137228087136256  7     0.9294392466545105   myRun 
20        Q0  33290743200092160  8     0.9288673400878906   myRun 
20        Q0  29105489178529792  9     0.9250818490982056   myRun 
20        Q0  29341073989967872  10    0.9246830940246582   myRun 

# Installation and run instructions
## Download the BERT model
- Run the following code  below in the terminal to download the BERT model
- pip3 install --user sentence_transformers

## Download the other necessary libraries
- Run the following code below in the terminal to download the libaries
- pip3 install --user numpy
- pip3 install --user torch

## Run the program
- To run the BERT approach, call the main.py file inside the `/bert` folder.