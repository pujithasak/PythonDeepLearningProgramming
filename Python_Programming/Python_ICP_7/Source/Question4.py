#!/usr/bin/env python
# coding: utf-8

# In[12]:


import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
from nltk.tokenize import sent_tokenize, word_tokenize

text = open('D:\Python & Deep Learning\PythonDeepLearningProgramming\Python_Programming\Python_ICP_7\Source\input.txt', encoding="utf8").read()

# Tokenization
stokens = nltk.sent_tokenize(text)
wtokens = nltk.word_tokenize(text)
print("\n Word Tokenization :\n")
print(wtokens)

print("\n Sentence Tokenization :\n")
print(stokens)


# In[6]:


# Parts of Speech
txt = nltk.word_tokenize(text)
print("POS:\n")
print(nltk.pos_tag(txt))


# In[7]:


# Stemming
print("Stremming:\n")
pStemmer = PorterStemmer()
lStemmer = LancasterStemmer()
sStemmer = SnowballStemmer('english')
for t in wtokens:
   print(pStemmer.stem(t), lStemmer.stem(t), sStemmer.stem(t))


# In[8]:


# Lemmatization

print("Lemmatization :\n")
lemmatizer = WordNetLemmatizer()
for t in wtokens:
    print(lemmatizer.lemmatize(t))


# In[9]:


# Trigram
print("Trigram:\n")
for s in stokens:
    token = nltk.word_tokenize(s)
    trigrams = list(ngrams(token, 3))
    print("The text:", s, "\nword_tokenize:", token, "\ntrigrams:", trigrams)


# In[10]:


# Named Entity Recognition
print("Named Entity Recognition: \n")
for s in stokens:
    print(ne_chunk(pos_tag(word_tokenize(s))))

