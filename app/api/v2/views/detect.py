from flask import Blueprint, request, jsonify

news = Blueprint('news', __name__, url_prefix='/api/v2')

@news.route('/detect', methods=['POST'])
def verify():
    pass

@news.route('/', methods=['GET'])
def hello():
    return "This is a project by team STL:"