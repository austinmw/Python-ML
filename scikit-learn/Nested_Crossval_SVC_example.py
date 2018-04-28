"""
 Nested cross-validation example

Nested cross-validation (CV) is often used to train a model in which hyperparameters also need to be optimized. 
Nested CV estimates the generalization error of the underlying model and its (hyper)parameter search. 
Choosing the parameters that maximize non-nested CV biases the model to the dataset, yielding an overly-optimistic score.

Model selection without nested CV uses the same data to tune model parameters and evaluate model performance. 
Information may thus “leak” into the model and overfit the data.
The magnitude of this effect is primarily dependent on the size of the dataset and the stability of the model.

To avoid this problem, nested CV effectively uses a series of train/validation/test set splits. 
In the inner loop, the score is approximately maximized by fitting a model to each training set, 
and then directly maximized in selecting (hyper)parameters over the validation set. 
In the outer loop, generalization error is estimated by averaging test set scores over several dataset splits.


Linear SVC with SGD training on 20 newsgroups text dataset
Includes 5-fold cross-validated grid-search on 8 parameter combinations and detailed performance analysis
"""
import numpy as np
import pandas as pd
import timeit
from sklearn.datasets import fetch_20newsgroups
from sklearn.pipeline import Pipeline
from sklearn.model_selection import cross_val_score, GridSearchCV
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.linear_model import SGDClassifier
from sklearn import metrics

# start timer
start = timeit.default_timer()

# load data
twenty_train = fetch_20newsgroups(subset='train', shuffle=True)
twenty_test = fetch_20newsgroups(subset='test', shuffle=True)

# build classifier pipeline
text_clf = Pipeline([('vect', CountVectorizer()), 
		         ('tfidf', TfidfTransformer()), 
		         ('clf', SGDClassifier(loss='hinge', penalty='l2',
					        alpha=1e-3, n_iter=5, 
					        random_state=42))
])

# grid search parameters (2^3 combinations)
parameters = {'vect__ngram_range': [(1, 1), (1, 2)], # words or bigrams
		  'tfidf__use_idf': (True, False), # with or without inverse-document-frequency reweighting
		  'clf__alpha': (1e-2, 1e-3), # penalty (smoothing) parameter
}

# cross-validate classifier model on  hyperparameter cross-validated gridsearch (5x(8x5)=5x40= 200 runs)
scores = cross_val_score(GridSearchCV(text_clf, parameters, 
	                                                      n_jobs=-1, # detect number of CPU's and use them all
	                                                      verbose=2, # higher = more verbose
	                                                      cv=5), # default is 3
	                               twenty_train.data, twenty_train.target, cv=5, scoring="accuracy")

# Unbiased estimate of the accuracy
print("%f +-%f" % (np.mean(scores), np.std(scores)))			


# Runtime
stop = timeit.default_timer()
total_time = stop - start
mins, secs = divmod(total_time, 60)
hours, mins = divmod(mins, 60)
print("\nTotal running time: %d:%02d:%02d\n" % (hours, mins, secs))
