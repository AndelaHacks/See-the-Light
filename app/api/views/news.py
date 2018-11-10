from flask import Flask, Blueprint, jsonify, request
# from app.api.models import news_model
# import json
import requests

news = Blueprint('news', __name__)
app = Flask(__name__)


@news.route('/')
def hello():
    return "This is a project by team STL: sample link(http://127.0.0.1:5000/news/get?link=https://www.bbc.com/news/uk-politics-46155403)"


@news.route('/get', methods=['GET'])
def post_news_link():
    link = request.args.get('link')
    print('######## THIS IS THE LINK FROM GET METHOD', link)
    response = requests.post('http://newsbreakers.herokuapp.com',
                             data={"text": link}
                             # content_type='application/json'
                             )
    print("###########", response.content)
    return (response.content)

    # return "This is a project by team STL"

#     # response = app.test_client().post(
#     #     'newsbreakers.herokuapp.com/',
#     #     data=json.dumps(
#     #         dict(
#     #             text = 'https://www.bbc.com/news/uk-politics-46155403'
#     #             )
#     #         ),
#     #         content_type='application/json'
#     #     )
#     print("###########", response.content)
#     return (response.content)
