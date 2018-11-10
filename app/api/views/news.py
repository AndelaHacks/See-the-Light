from flask import Flask, Blueprint, jsonify, request
from app.api.models import news_model
import json
import requests
# from app import app
# from app.api.v1.models.news_model import Sale
# from app.api.v1.models.store_model import Store
news = Blueprint('news', __name__)
app = Flask(__name__)

@news.route('/')
def hello():
    return "This is a project by team STL"

# @news.route('/news', methods = ['GET'])
# def get_all_news():
#     all_news = Store.get_all_news()
#     if all_news:
#         return jsonify(all_news)
#     else:
#         return "The sale records are empty"

@news.route('/news', methods = ['POST'])
def post_news():
    
    #reading the request
    req_data = request.get_json()
    # sale_id = req_data['sale_id']
    # sale_id = "S" + str(len(Store.news) + 1)
    # product_id = req_data['product_id']
    # quantity_sold = req_data['quantity_sold']
    # amount = req_data['amount']
    link = req_data['link']
    # response = app.test_client.post('/api/v1/products')


    #creating sale object
    # sale = Sale(sale_id, product_id, quantity_sold, amount)
    # store = Store()
    # response = sale.post_sale()
    # if response == 'success':
    #     #update the records of the products by substracting sold qty
    #     try:
    #         Store.update_product(product_id, -(int(quantity_sold)))
    #     except:
    #         print ("No such record-temp error message")
    #     return 'sale transaction successfully processed', 201
    # else:
    #     return 'the sale transaction did not go through, possible invalid request', 400

    response = requests.post('http://newsbreakers.herokuapp.com',
        data= {"text":"https://www.bbc.com/news/uk-politics-46155403"}
            # content_type='application/json'
        )

    # response = app.test_client().post(
    #     'newsbreakers.herokuapp.com/',
    #     data=json.dumps(
    #         dict(
    #             text = 'https://www.bbc.com/news/uk-politics-46155403'
    #             )
    #         ),
    #         content_type='application/json'
    #     )
    print("###########", response.content)
    return ("Done", response.status_code)