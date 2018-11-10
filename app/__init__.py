from flask import Flask, Blueprint
from app.api.views.news import news
# from app.api.v1.views.errors import errors


app = Flask(__name__)
app.register_blueprint(news, url_prefix='/news')
# app.register_blueprint(news, url_prefix='/')
# app.register_blueprint(news, url_prefix='/news')
# app.register_blueprint(errors)