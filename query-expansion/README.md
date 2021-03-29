#### Functionality
In this section of the assignment, we were given the task to implement a query expansion based on pre-trained word embeddings and using other methods such as adding synonyms to the query if there is a similarity with more than one word in the query. We created functions in our `main.py` that would help expand the query. We also used `NLP` for word embedding that would later be implemented in calculating the similarity between two or more query words.
After expanding the query, the words would now contain synonyms used to retrieve and rank the tweet documents. For example, given the query "human," we can identify "human nature, human being" as a synonym for that particular query word and then add it to the query, matching both human and human nature or human beings. 

After the query is expanded, we follow the exact implementation we did earlier in `assignment 1` to calculate the Cosine Similarity between each Document & Query, respectively, and then store them in a dictionary in our results. After finding the `cosSim`, we then rank the tweets in the `dict()` from the highest to the lowest.


#### Discussion (Compared to Assignment 1)
- From Assignment 1: MAP: 0.1679    ;      P@10: 0.1833
- From query expansion : MAP: 0.1272    ;      P@10: 0.1149

The MAP and P@10 result from assignment one score is much better than the query expansion score. When expanding a query using synonyms, the recall is increased at the expense of precision.  Studies have been made that show how synonym query expansion can degrade a query performance rather than make it better. 
In order to have achieved a better result, the Rocchio algorithm's implementation would have helped improve the query expansion, even if it's a little bit. The Rocchio algorithm is mainly referred to as the relevancy feedback where it gets the top relevant document and then implements the query expansion using the top document.

In conclusion, the query expansions performed worse compared to the methods that were explored in this assignment. However, the benefit is that query expansion can be implemented with any of the approaches performed in this assignment. After the query's expansion, we can implement relevancy feedback that can calculate the cosine similarity again using the relevant documents

#### Algorithm and Data structure
Our implementation of the IR system for `Query expansion` was based on expanding the query by adding synonyms to the query if there was a similarity with more than one word in the query. We used `word embeddings` to find the similarity between the query word. The word embedding uses `natural language processing` to see the similarity for the query word. Afterward, we used `wordnet` to find the synonyms of the word terms that have similarities. 

The expansion of the query functions was implemented in the `main.py` file. Using the previously implemented IR  system in `Assignment 1`, we could retrieve and rank the newly created query and tweet documents.
Project Main Files

#### Project Main Files

##### `main.py`:
The `main.py` contains the primary and essential functions for executing the IR system. Some of the helper functions include the Preprocess file, spacy, and wordnet. The `main function` also contains a loaded `NLP` (Natural Language Processing), which creates the similarity for the query's words. We started by importing the `tweets` and the `queries` from the `assert` folder. Preprocessing is then performed on the import functions using the `filterSentence`. The `filterSentence` remains the same as the previous assignment, with a bit of modification made to it. The next step was to implement the functions that would expand the query using wordnet and NLP. The functions include:
-  `getSim(word, syn)`: Calculates the `similarity` between two words in the query. Word embedding is performed in this function in order to get the similarity for each query word.
- `getSyns(queryList)`: Finds the synonyms for each word in the query list.
- `canExpand(syn, queryList)`:  An helper function for expanding the query. It checks the similarity for each word in the query using the `getSim` function.
- `expand(query)`:  This is where we perform the query expansion. We first start by creating a`newQuery` and `syns` variables. The next step was to create a loop that checks for each synonym word in the list and then run the `canExpand` function for the synonym word and the query and ensure that the synonym word was not in the `newQuery` variable that was already created earlier. After appending the result into the newQuery, the variable is then returned.

Once the query's expansion is done, the `main()` function is then performed, which follows the same step in the previous assignment for the IR system using the newly expanded `query` and the `tweets`. To understand what is happening in the `main()` function, we created a set of print statements that would notify the user when the query is expanded and when the document's ranking is done. The user then gets informed of the creation of the result file.

##### `preprocess.py`:
The preprocessing file remains the same as the previous implementation, with a few modifications made in the `filterSentence` and the `importQuery`. 
In the `filterSentence`, we created two tokens, one with stemmed words and the other doesn't. The words that are not stemmed, are used in the query expansion for finding the words' synonyms. While in the `importQuery`, we also created two sets of query lists containing stemmed words and no stemmed words.


##### `result.py`:
This file contains the function for calculating the Cosimilarity values for the set of documents against each query and then ranks the similarity scores in descending order. Dictionary was used as our primary source for storing the query_index, retrieval, and query_length values. The function comprises mainly loops. At the start, we first calculated the occurrences of the token in each query. We then moved to calculate the TF-IDF and the length of the query. After getting the necessary calculations needed, we then moved to solving the CosSimalarity values and then ranking the document according to the specified order.


##### `write.py`:
This file contains a helper function that creates a table for each of the results generated in the `main.py` and then stores it in the `dist/query-expansion` directory.


#### Additional Libraries

##### Prettytable (`prettytable.py`):  
A helper library to format the output for the `Results.txt` file. Used in the implementation of the `write.py`.

#### Results for Query 3 & 20

##### Query 3
```
 1         Q0  31466391706017792  1     0.1998567335243553     myRun 
 1         Q0  30407444110778369  2     0.1477653234454287     myRun 
 1         Q0  34948668163362816  3     0.1386547082201938     myRun 
 1         Q0  34073394068590592  4     0.1290845236479003     myRun 
 1         Q0  32629073276571648  5     0.12373671801125216    myRun 
 1         Q0  32229379287289857  6     0.12161781019700534    myRun 
 1         Q0  30493951110676480  7     0.11940217949497257    myRun 
 1         Q0  30216589932503040  8     0.1191833587731748     myRun 
 1         Q0  29514474415198208  9     0.11699618729082718    myRun 
 1         Q0  30198105513140224  10    0.11629882192090524    myRun 
```
##### Query 20
```
 20        Q0  30649815905869824  1     0.3105204557845766     myRun 
 20        Q0  29803547608481792  2     0.23929276345833797    myRun 
 20        Q0  33356942797701120  3     0.23695303696737582    myRun 
 20        Q0  34082003779330048  4     0.1964380192155871     myRun 
 20        Q0  34066620821282816  5     0.1964380192155871     myRun 
 20        Q0  33752688764125184  6     0.1964380192155871     myRun 
 20        Q0  33695252271480832  7     0.1964380192155871     myRun 
 20        Q0  33580510970126337  8     0.1964380192155871     myRun 
 20        Q0  32866366780342272  9     0.1964380192155871     myRun 
 20        Q0  32269178773708800  10    0.1964380192155871     myRun 
```
#### Setting up & Execution

##### Download necessary libraries
Run the following code below in the terminal to download the libaries:
- `pip3 install --user spacy`
- `pip3 install --user wordnet`
- `python3 -m spacy download en_core_web_lg`

##### Run the program
- To run the QueryExpansion approach, call the `main.py` file inside the `/query-expansion` folder after set up steps have been completed with `python3 main.py`
