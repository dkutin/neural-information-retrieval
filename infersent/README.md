# Setup Process for InferSent

See: https://github.com/facebookresearch/InferSent

## Dependencies

This code is written in python. Dependencies include:

* Python 2/3
* [Pytorch](http://pytorch.org/) (recent version)
* NLTK >= 3

## Download word vectors

Download [GloVe](https://nlp.stanford.edu/projects/glove/) (V1):
```bash
mkdir GloVe
curl -Lo GloVe/glove.840B.300d.zip http://nlp.stanford.edu/data/glove.840B.300d.zip
unzip GloVe/glove.840B.300d.zip -d GloVe/
```

## Use our sentence encoder
We provide a simple interface to encode English sentences. **See [**demo.ipynb**](https://github.com/facebookresearch/InferSent/blob/master/demo.ipynb)
for a practical example.** Get started with the following steps:

*0.0) Download our InferSent models (V1 trained with GloVe, V2 trained with fastText)[147MB]:*
```bash
mkdir encoder
curl -Lo encoder/infersent1.pkl https://dl.fbaipublicfiles.com/infersent/infersent1.pkl
```
Note that infersent1 is trained with GloVe (which have been trained on text preprocessed with the PTB tokenizer) and infersent2 is trained with fastText (which have been trained on text preprocessed with the MOSES tokenizer). The latter also removes the padding of zeros with max-pooling which was inconvenient when embedding sentences outside of their batches.