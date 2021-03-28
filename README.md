## Query Expansion (Approach 3 - Joshua Erivwo

### Functionality
Expands the querys by adding synomys of the simalarities of the queries and then calls the functions from the assignment 1 to The reason for the result is due to not implementing the rocchio algorithms whichs deals mostly with the top relevent documents in the IR system. 
Query expansion performed the worse among the two other methods that was written


### Discussion (Compared to Assignment 1)
The query expansions seems worse compared to the previous assigment
The query expansions performed worse from the previous methods that was explored
The benefit for query expansion is that it can be implemented with any of the approach that was perfomed in this assignment. it only expands the query, the rest can be found


### Algorithm and Data structure

#### Project Main Files

##### `main.py`:

##### `preprocess.py`:

##### `result.py`:

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
- `pip3 install --spacy`
- `python3 -m spacy download en_core_web_lg1`
- `pip3 install --wordnet`


##### Run the program
- To run the QueryExpansion approach, call the `main.py` file inside the `/query-expansion` folder after set up steps have been completed with `python3 main.py`
