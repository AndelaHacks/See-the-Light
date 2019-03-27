from flask import Blueprint, request, jsonify
from newspaper import Article
from sklearn.externals import joblib
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from fuzzywuzzy import fuzz, process
import app.api.v2.models.news_functions as kick
import requests


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



@news.route('/detect', methods=['POST'])
def verify():
    # get the url from user input to test for authenticity
    url = request.get_json()['url']
    try:
        a = Article(url)
        a.download()
        a.parse()
    except: #expression as identifier:
        return jsonify({"An Error has been detected, unable to scrape article text from,": url})
    TXT = a.text
    TITLE = a.title
    use = kick.summarize(TITLE,TXT)
    # lets compare similarity of the Title to Article
    fuzzy = str(round((100-fuzz.ratio(TITLE,use))*1.0,1))

    # unpack and deploy trained count vectorizer
    count_vect = joblib.load('vectorizer.pkl')
    X_train_counts = count_vect.fit_transform([TXT])
    tf_transformer = TfidfTransformer()
    X_train_tfidf = tf_transformer.fit_transform(X_train_counts)
    
    # Sentiment analysis is the automated process of 
    # understanding an opinion about a given subject from written or spoken language
    senti = kick.sentiment(TXT)
    #unpack and run trained model
    clf = joblib.load('stl_news_model.pkl')
    pred = clf.predict(X_train_tfidf)
    prob = clf.predict_proba(X_train_tfidf)
    pred_out = pred[0].decode('utf-8')
    if prob[0][0] >= .5:
        prob_out = str(round(prob[0][0]*100, 1))
    else:
        prob_out = str(round(prob[0][1]*100, 1))
    return jsonify({"Prediction": pred_out, "percentage of confidence": prob_out, "subjectivity": senti[0], "polarity": senti[1], "Title / Article Comparison": fuzzy})

@news.route('/get', methods=['GET'])
def post_news_link():
    # Kate is expecting this format - hence do a get request which will perform post again
    # link to be ("https://stl-v2.herokuapp.com/api/v2/get?url="+item.getText().toString());
    url = request.args.get('url')

    # # return jsonify({"The URL you entered is": link})
    
    try:
        a = Article(url)
        a.download()
        a.parse()
    except: #expression as identifier:
        return jsonify({"An Error has been detected, unable to scrape article text from,": url})
    TXT = a.text
    TITLE = a.title
    use = kick.summarize(TITLE,TXT)
    # lets compare similarity of the Title to Article
    fuzzy = str(round((100-fuzz.ratio(TITLE,use))*1.0,1))

    # unpack and deploy trained count vectorizer
    count_vect = joblib.load('vectorizer.pkl')
    X_train_counts = count_vect.fit_transform([TXT])
    tf_transformer = TfidfTransformer()
    X_train_tfidf = tf_transformer.fit_transform(X_train_counts)
    
    # Sentiment analysis is the automated process of 
    # understanding an opinion about a given subject from written or spoken language
    senti = kick.sentiment(TXT)
    #unpack and run trained model
    clf = joblib.load('stl_news_model.pkl')
    pred = clf.predict(X_train_tfidf)
    prob = clf.predict_proba(X_train_tfidf)
    pred_out = pred[0].decode('utf-8')
    if prob[0][0] >= .5:
        prob_out = str(round(prob[0][0]*100, 1))
    else:
        prob_out = str(round(prob[0][1]*100, 1))
    return jsonify({"Prediction": pred_out, "percentage of confidence": prob_out, "subjectivity": senti[0], "polarity": senti[1], "Title / Article Comparison": fuzzy})