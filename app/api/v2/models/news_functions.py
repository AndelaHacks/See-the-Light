from flask import request, jsonify
import requests
from bs4 import BeautifulSoup
import socket
import requests
from textblob import TextBlob
from newspaper import Article
from sklearn.externals import joblib
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from math import fabs
from re import split as regex_split, sub as regex_sub, UNICODE as REGEX_UNICODE
from collections import Counter
from fuzzywuzzy import fuzz, process

# stop words etc from pyteaser
stopWords = set([
    "-", " ", ",", ".", "a", "e", "i", "o", "u", "t", "about", "above",
    "above", "across", "after", "afterwards", "again", "against", "all",
    "almost", "alone", "along", "already", "also", "although", "always",
    "am", "among", "amongst", "amoungst", "amount", "an", "and",
    "another", "any", "anyhow", "anyone", "anything", "anyway",
    "anywhere", "are", "around", "as", "at", "back", "be", "became",
    "because", "become", "becomes", "becoming", "been", "before",
    "beforehand", "behind", "being", "below", "beside", "besides",
    "between", "beyond", "both", "bottom", "but", "by", "call", "can",
    "cannot", "can't", "co", "con", "could", "couldn't", "de",
    "describe", "detail", "did", "do", "done", "down", "due", "during",
    "each", "eg", "eight", "either", "eleven", "else", "elsewhere",
    "empty", "enough", "etc", "even", "ever", "every", "everyone",
    "everything", "everywhere", "except", "few", "fifteen", "fifty",
    "fill", "find", "fire", "first", "five", "for", "former",
    "formerly", "forty", "found", "four", "from", "front", "full",
    "further", "get", "give", "go", "got", "had", "has", "hasnt",
    "have", "he", "hence", "her", "here", "hereafter", "hereby",
    "herein", "hereupon", "hers", "herself", "him", "himself", "his",
    "how", "however", "hundred", "i", "ie", "if", "in", "inc", "indeed",
    "into", "is", "it", "its", "it's", "itself", "just", "keep", "last",
    "latter", "latterly", "least", "less", "like", "ltd", "made", "make",
    "many", "may", "me", "meanwhile", "might", "mill", "mine", "more",
    "moreover", "most", "mostly", "move", "much", "must", "my", "myself",
    "name", "namely", "neither", "never", "nevertheless", "new", "next",
    "nine", "no", "nobody", "none", "noone", "nor", "not", "nothing",
    "now", "nowhere", "of", "off", "often", "on", "once", "one", "only",
    "onto", "or", "other", "others", "otherwise", "our", "ours",
    "ourselves", "out", "over", "own", "part", "people", "per",
    "perhaps", "please", "put", "rather", "re", "said", "same", "see",
    "seem", "seemed", "seeming", "seems", "several", "she", "should",
    "show", "side", "since", "sincere", "six", "sixty", "so", "some",
    "somehow", "someone", "something", "sometime", "sometimes",
    "somewhere", "still", "such", "take", "ten", "than", "that", "the",
    "their", "them", "themselves", "then", "thence", "there",
    "thereafter", "thereby", "therefore", "therein", "thereupon",
    "these", "they", "thickv", "thin", "third", "this", "those",
    "though", "three", "through", "throughout", "thru", "thus", "to",
    "together", "too", "top", "toward", "towards", "twelve", "twenty",
    "two", "un", "under", "until", "up", "upon", "us", "use", "very",
    "via", "want", "was", "we", "well", "were", "what", "whatever",
    "when", "whence", "whenever", "where", "whereafter", "whereas",
    "whereby", "wherein", "whereupon", "wherever", "whether", "which",
    "while", "whither", "who", "whoever", "whole", "whom", "whose",
    "why", "will", "with", "within", "without", "would", "yet", "you",
    "your", "yours", "yourself", "yourselves", "the", "reuters", "news",
    "monday", "tuesday", "wednesday", "thursday", "friday", "saturday",
    "sunday", "mon", "tue", "wed", "thu", "fri", "sat", "sun",
    "rappler", "rapplercom", "inquirer", "yahoo", "home", "sports",
    "1", "10", "2012", "sa", "says", "tweet", "pm", "home", "homepage",
    "sports", "section", "newsinfo", "stories", "story", "photo",
    "2013", "na", "ng", "ang", "year", "years", "percent", "ko", "ako",
    "yung", "yun", "2", "3", "4", "5", "6", "7", "8", "9", "0", "time",
    "january", "february", "march", "april", "may", "june", "july",
    "august", "september", "october", "november", "december",
    "government", "police"
])
ideal = 20.0


def apility(url_2):
    # return the domain part from news link
    # the check IP address reputation

    get_url = (url_2.split('/'))[2]
    IP_addr = socket.gethostbyname(get_url)
    Token_apility = '52a90970-cfa0-4536-91e5-f7148bb25c61'
    headers = {
        "Accept": "application/json",
        "X-Auth-Token": Token_apility
    }
    # request(method, url, body=None, headers={})
    # Apility API documentation here https://apility.io/apidocs/
    # get-full-ip-address-reputation-info
    # GET https://api.apility.net/v2.0/ip/<IP>
    ip_reputation = request.get('https://api.apility.net/v2.0/ip/' +
                                IP_addr, headers=headers)
    return ip_reputation.content


    '''import requests

        url = "https://api.apility.net/v2.0/ip/197.248.149.122"

        headers = {
            'accept': "application/json",
            'x-auth-token': "YOUR_API_KEY"
            }

        response = requests.request("GET", url, headers=headers)

        print(response.text)
        
        '''


def summarize(title, text):
    summaries = []

    sentences = split_sentences(text)
    keys = keywords(text)
    titleWords = split_words(title)

    if len(sentences) <= 1:
        return sentences
    # score setences, and use the top 5 sentences
    ranks = score(sentences, titleWords, keys).most_common(1)
    for rank in ranks:
        summaries.append(rank[0])

    return summaries


def split_words(text):
    # split a string into array of words
    try:
        # strip special xtrs
        text = regex_sub(r'[^\w ]', '', text, flags=REGEX_UNICODE)
        return [x.strip('.').lower() for x in text.split()]
    except TypeError:
        print("Error while splitting characters")
    return None


def split_sentences(text):
    sentences = regex_split(u'(?<![A-ZА-ЯЁ])([.!?]"?)(?=\s+\"?[A-ZА-ЯЁ])',
                            text, flags=REGEX_UNICODE)
    s_iter = zip(*[iter(sentences[:-1])] * 2)
    s_iter = [''.join(map(str, y)).lstrip() for y in s_iter]
    s_iter.append(sentences[-1])
    return s_iter


def keywords(text):
    text = split_words(text)
    numWords = len(text)  # of words before removing blacklist words
    freq = Counter(x for x in text if x not in stopWords)

    minSize = min(10, len(freq))  # get first 10
    keywords = {x: y for x, y in freq.most_common(minSize)}  # recreate a dict

    for k in keywords:
        articleScore = keywords[k]*1.0 / numWords
        keywords[k] = articleScore * 1.5 + 1

    return keywords


def score(sentences, titleWords, keywords):
    # score sentences based on different features

    senSize = len(sentences)
    ranks = Counter()
    for i, s in enumerate(sentences):
        sentence = split_words(s)
        titleFeature = title_score(titleWords, sentence)
        sentenceLength = length_score(sentence)
        sentencePosition = sentence_position(i+1, senSize)
        sbsFeature = sbs(sentence, keywords)
        dbsFeature = dbs(sentence, keywords)
        frequency = (sbsFeature + dbsFeature) / 2.0 * 10.0

        # weighted average of scores from four categories
        totalScore = (titleFeature*1.5 + frequency*2.0 +
                      sentenceLength*1.0 + sentencePosition*1.0) / 4.0
        ranks[s] = totalScore
    return ranks


def title_score(title, sentence):
    title = [x for x in title if x not in stopWords]
    count = 0.0
    for word in sentence:
        if (word not in stopWords and word in title):
            count += 1.0

    if len(title) == 0:
        return 0.0

    return count/len(title)


def length_score(sentence):
    return 1 - fabs(ideal - len(sentence)) / ideal


def sentence_position(i, size):

    normalized = i*1.0 / size
    if 0 < normalized <= 0.1:
        return 0.17
    elif 0.1 < normalized <= 0.2:
        return 0.23
    elif 0.2 < normalized <= 0.3:
        return 0.14
    elif 0.3 < normalized <= 0.4:
        return 0.08
    elif 0.4 < normalized <= 0.5:
        return 0.05
    elif 0.5 < normalized <= 0.6:
        return 0.04
    elif 0.6 < normalized <= 0.7:
        return 0.06
    elif 0.7 < normalized <= 0.8:
        return 0.04
    elif 0.8 < normalized <= 0.9:
        return 0.04
    elif 0.9 < normalized <= 1.0:
        return 0.15
    else:
        return 0


def sbs(words, keywords):
    score = 0.0
    if len(words) == 0:
        return 0
    for word in words:
        if word in keywords:
            score += keywords[word]
    return (1.0 / fabs(len(words)) * score)/10.0


def dbs(words, keywords):
    if (len(words) == 0):
        return 0

    summ = 0
    first = []
    second = []

    for i, word in enumerate(words):
        if word in keywords:
            score = keywords[word]
            if first == []:
                first = [i, score]
            else:
                second = first
                first = [i, score]
                dif = first[0] - second[0]
                summ += (first[1]*second[1]) / (dif ** 2)

    # number of intersections
    k = len(set(keywords.keys()).intersection(set(words))) + 1
    return (1/(k*(k+1.0))*summ)


def sentiment(text):
    blob = TextBlob(text)
    subjectivity = str(round(blob.sentiment.subjectivity*100, 1))
    polarity = str(round(blob.sentiment.polarity*100, 1))
    return [subjectivity, polarity]


def detector(url):
    try:
        a = Article(url)
        a.download()
        a.parse()
        r = request.get(url)
        page = r.text
        soup = BeautifulSoup(page, 'lxml')
    except:  # expression as identifier:
        return jsonify({"An Error has been detected, unable to scrape article\
                        text from": url})
    TXT = a.text
    TITLE = a.title
    use = summarize(TITLE, TXT)
    paras = soup.find_all('p')
    # lets compare similarity of the Title to Article
    # fuzzy = str(round((100-fuzz.ratio(TITLE, use))*1.0, 1))

    # # unpack and deploy trained count vectorizer
    # count_vect = joblib.load('vectorizer.pkl')
    # X_train_counts = count_vect.fit_transform([TXT])
    # tf_transformer = TfidfTransformer()
    # X_train_tfidf = tf_transformer.fit_transform(X_train_counts)
    # # Sentiment analysis is the automated process of
    # # understanding an opinion about a given subject
    # # from written or spoken language
    # senti = sentiment(TXT)
    # # unpack and run trained model
    # clf = joblib.load('stl_news_model.pkl')
    # pred = clf.predict(X_train_tfidf)
    # prob = clf.predict_proba(X_train_tfidf)
    # pred_out = pred[0].decode('utf-8')
    # if prob[0][0] >= .5:
    #     prob_out = str(round(prob[0][0]*100, 1))
    # else:
    #     prob_out = str(round(prob[0][1]*100, 1))
    # return jsonify({"Prediction": pred_out,
    #                 "percentage of confidence": prob_out,
    #                 "subjectivity": senti[0],
    #                 "polarity": senti[1],
    #                 "Title / Article Comparison": fuzzy})
    for i, paras in enumerate(paras)
        return jsonify (paras)