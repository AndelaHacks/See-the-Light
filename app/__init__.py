from flask import Flask, Blueprint
from app.api.views.news import news
# from app.api.v1.views.sales import sales
# from app.api.v1.views.products import products
# from app.api.v1.views.errors import errors


app = Flask(__name__)
app.register_blueprint(news, url_prefix='/news')
# app.register_blueprint(news, url_prefix='/')
# app.register_blueprint(news, url_prefix='/news')
# app.register_blueprint(products, url_prefix='/api/v1')
# app.register_blueprint(errors)
