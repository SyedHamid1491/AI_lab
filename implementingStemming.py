#importing the Stemming function from nltk library

from nltk.stem.porter import PorterStemmer

from nltk.stem import PorterStemmer 

from nltk.stem import SnowballStemmer

snowball = SnowballStemmer(language='english')
stemmer = PorterStemmer()

#defining the object for stemming

text= """Natural Language Processing with Python provides a practical introduction to programming for
language processing. Written by the creators of NLTK, it guides the reader through the fundamentals of
writing Python programs, working with corpora, categorizing text, analyzing linguistic structure, and more.
The online version of the book has been updated for Python 3 and NLTK 3."""

def stem_words(text):
    return " ".join([stemmer.stem(word) for word in text.split()])

stemmed_text=stem_words(text)

print("Actual text\n",text)

print("stemmed text\n:",stemmed_text)