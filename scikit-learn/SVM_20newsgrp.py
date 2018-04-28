# Linear SVC with SGD training on 20 newsgroups text dataset
# Includes 3-fold cross-validated grid-search on 8 parameter combinations and detailed performance analysis
# (non-nested cross-validation)

import numpy as np
import pandas as pd
import timeit
from sklearn.datasets import fetch_20newsgroups
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
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

# create crossvalidating gridsearch classifier (3-fold, by default)
gs_clf = GridSearchCV(text_clf, parameters, 
	                           n_jobs=-1, # detect number of CPU's and use them all
	                           verbose=1) # higher = more verbose

# fit model														
gs_clf.fit(twenty_train.data, twenty_train.target)

# display best cv score and corresponding parameters 
print("\nBest score: ", gs_clf.best_score_ )
print("\nBest parameters: ")
for param_name in sorted(parameters.keys()):
	print("%s: %r" % (param_name, gs_clf.best_params_[param_name]))
	
# display detailed information on crossvalidated tuning parameters	
print('\n', pd.DataFrame(gs_clf.cv_results_))

# predict on test data
predicted = gs_clf.predict(twenty_test.data)

# calculate and display correct classification rate
print("\nTest CCR: ", metrics.accuracy_score(twenty_test.target, predicted))

# detailed performance analysis
print('\n', metrics.classification_report(twenty_test.target, predicted,
        target_names=twenty_test.target_names))
print('\n', metrics.confusion_matrix(twenty_test.target, predicted))			

# Runtime
stop = timeit.default_timer()
total_time = stop - start
mins, secs = divmod(total_time, 60)
hours, mins = divmod(mins, 60)
print("\nTotal running time: %d:%02d:%02d\n" % (hours, mins, secs))


# Results: 
# More accurate than naive bayes, but slower


# Example predictions for a couple of test documents
test_docs =  ["god religion stuff", "computers and tech graphics"]
pred = gs_clf.predict(test_docs)
print("Examples of document classifications:")
for i,p in enumerate(pred):
	print(' "%s"  => %s' % (test_docs[i], twenty_train.target_names[p]))

