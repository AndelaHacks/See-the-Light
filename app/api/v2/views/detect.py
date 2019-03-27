from flask import Blueprint, request, jsonify
import app.api.v2.models.news_functions as kick

"""The Levenshtein Distance
The Levenshtein distance is a metric to measure how apart are two sequences of words. In other words, 
it measures the minimum number of edits that you need to do to change a one-word sequence into the other. 
These edits can be insertions, deletions or substitutions. 
This metric was named after Vladimir Levenshtein, who originally considered it in 1965.

FuzzyWuzzy has, just like the Levenshtein package, a ratio function that computes the standard Levenshtein 
distance similarity ratio between two sequences:

Fuzzywuzzy process module allows you 
to calculate the string with the highest similarity out of a vector of strings.
"""

news = Blueprint('news', __name__, url_prefix='/api/v2')


@news.route('/')
def hello():
    return jsonify({"See The Light": "Detect Fake news app"})

@news.route('/detect', methods=['POST'])
def verify():
    # get the url from user input to test for authenticity
    
    url = request.get_json()['url']
    return kick.detector(url)

@news.route('/get', methods=['GET'])
def post_news_link():
    # Kate is expecting this format - hence do a get request which will perform post again
    # link to be ("https://stl-v2.herokuapp.com/api/v2/get?url="+item.getText().toString());
    url = request.args.get('url')
    return kick.detector(url)