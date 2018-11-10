from flask import Flask, Blueprint
from app.api.views.news import news
app = Flask(__name__)
app.register_blueprint(news, url_prefix='/news')

