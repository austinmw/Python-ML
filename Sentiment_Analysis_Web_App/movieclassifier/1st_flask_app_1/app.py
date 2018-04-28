
from flask import Flask, render_template

app = Flask(__name__) # initialize a new Flask instance (template in same directory)

@app.route('/') # route decorator to specify the URL to trigger execution of the index function
def index(): # renders the HTML file frist_app.html located in templates folder
    return render_template('first_app.html')

if __name__ == '__main__': # ensure below
    app.run() # only run app on server when this script is directly executed by Py interpreter