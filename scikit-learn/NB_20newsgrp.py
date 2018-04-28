# Naive Bayes classifier on 20 newsgroups text dataset

import numpy as np
from sklearn.datasets import fetch_20newsgroups
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB

# load data
twenty_train = fetch_20newsgroups(subset='train', shuffle=True)
twenty_test = fetch_20newsgroups(subset='test', shuffle=True)

# build pipeline (vectorize words -> word frequencies -> fit NB model)
text_clf = Pipeline([('vect', CountVectorizer()), ('tfidf', TfidfTransformer()), ('clf', MultinomialNB())])

# apply pipeline to built classifier
text_clf.fit(twenty_train.data, twenty_train.target)

# evaluate performance
predicted = text_clf.predict(twenty_test.data)
ccr = np.mean(predicted == twenty_test.target)
print(ccr)