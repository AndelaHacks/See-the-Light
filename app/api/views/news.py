from flask import Flask, Blueprint, jsonify, request
import requests

news = Blueprint('news', __name__)
app = Flask(__name__)

from app.api.models import news_model
import json
import socket
import requests
# from app import app
# from app.api.v1.models.news_model import Sale
# from app.api.v1.models.store_model import Store
news = Blueprint('news', __name__)
app = Flask(__name__)


@news.route('/')
def hello():
    return "This is a project by team STL: sample link(http://127.0.0.1:5000/news/get?link=https://www.bbc.com/news/uk-politics-46155403)"

@news.route('/get', methods = ['GET'])
def post_news_link():
    link = request.args.get('link')
    print('######## THIS IS THE LINK FROM GET METHOD', link)
    response = requests.post('http://newsbreakers.herokuapp.com',
                             data={"text": link}
                             # content_type='application/json'
                             )
    print("###########", response.content)
    return (response.content)

       data= {"text":link}
            # content_type='application/json'
        )
    print("###########", response.content)
    return (response.content)

@news.route('/url', methods = ['GET'])
def post_url_link():
    link = request.args.get('link')
    get_url = (link.split('/'))[2]
    IP_addr = socket.gethostbyname(get_url)
    Token_Charles = '52a90970-cfa0-4536-91e5-f7148bb25c61'
    Token_Simon = '6ca9c9de-3b1e-4300-b85b-6501bf44717a'

    headers = {
    "Accept": "application/json",
    "X-Auth-Token": Token_Simon,
    }

    fullip = requests.get('https://api.apility.net/v2.0/' +
                        IP_addr, headers=headers)
    print(fullip)

    return fullip.content
