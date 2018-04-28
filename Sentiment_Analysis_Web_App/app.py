
# First half:
# import python modules and objects, code to unpickle and set up classification model

from flask import Flask, render_template, request
from wtforms import Form, TextAreaField, validators
import pickle
import sqlite3
import os
import numpy as np
# import HashingVectorizer from local dir
from vectorizer import vect

app = Flask(__name__)

###### PREPARING THE CLASSIFIER
cur_dir = os.path.dirname(__file__)
# Note: clf object will be reset to original pickled state if web app restarts
clf = pickle.load(open(os.path.join(cur_dir, 'pkl_objects/classifier.pkl'), 'rb'))
db = os.path.join(cur_dir, 'reviews.sqlite')

# return predicted class label and corresponding probability
def classify(document):
    label = {0: 'negative', 1: 'positive'}
    X = vect.transform([document])
    y = clf.predict(X)[0]
    proba = np.max(clf.predict_proba(X))
    return label[y], proba

# used to update the classifier provided a document and class label
def train(document, y):
    X = vect.transform([document])
    clf.partial_fit(X, [y], classes=np.unique(y))
    
    
# store submitted movie review in SQLite database along with label and timestamp for record    
def sqlite_entry(path, document, y):
    conn = sqlite3.connect(path)
    c = conn.cursor()
    c.execute("INSERT INTO review_db (review, sentiment, date)"\
              " VALUES (?, ?, DATETIME('now'))", (document, y))
    conn.commit()
    conn.close()
    
# Second half:
# ReviewForm class instantiates a TextAreaField which will be rendered in reviewform.html
# template file (landing page) which will be rendered by index function. 
# validators.length(min=15) to require at least 15 characters
# results function fetches contents of submitted web form and passes it to classifier to predict
# gets displayed in rendered results.html template
# feedback function getches predicted class label from results.html template if user clicked on
# correct/incorrect feedback button, then transforms predicted sentiment back into int class 
# label to use used to update classifier via train function implemented above.
# new entry to SQLite db  made via sqlite_entry function if feedback provided
# thanks.html template rendered to thank user for feedback

class ReviewForm(Form):
    moviereview = TextAreaField('', [validators.DataRequired(), validators.length(min=15)])
    
@app.route('/')    
def index():
    form = ReviewForm(request.form)
    return render_template('reviewform.html', form=form)

@app.route('/results', methods=['POST'])
def results():
    form = ReviewForm(request.form)
    if request.method == 'POST' and form.validate():
        review = request.form['moviereview']
        y, proba = classify(review)
        return render_template('results.html', 
                               content=review, 
                               prediction=y, 
                               probability=round(proba*100, 2))
    return render_template('reviewform.html', form=form)

@app.route('/thanks', methods=['POST'])
def feedback():
    feedback = request.form['feedback_button']
    review = request.form['review']
    prediction = request.form['prediction']
    inv_label = {'negative': 0, 'positive': 1}
    y = inv_label[prediction]
    if feedback == 'Incorrect':
        y = int(not(y))
    train(review, y)
    sqlite_entry(db, review, y)
    return render_template('thanks.html')

if __name__ == '__main__':
    app.run(debug=True)