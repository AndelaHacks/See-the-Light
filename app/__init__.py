from flask import Flask

def create_app():
    app = Flask(__name__)

    from app.api.v2.views.detect import news

    app.register_blueprint(news)

    return app

