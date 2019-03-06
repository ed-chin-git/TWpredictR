""" Main application and routing logic for TweetR """
from flask import Flask, request, render_template
from .models import DB, User, Tweet
from decouple import config


def create_app():
    """ create + config Flask app obj """
    app = Flask(__name__)

    #  after creatin models.py  run the follow
    #  configure the app object 
    app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URL')  # get db loc from .env
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['FLASK_ENV'] = config('ENV')
    DB.init_app(app)

    @app.route('/')
    def root():
        users = User.query.all()
        tweets = Tweet.query.all()
        return render_template('base.html', title='Home', users=users, tweets=tweets )
    
    @app.route('/reload')
    def reload():
        DB.drop_all()
        DB.create_all()
        return render_template('base.html', title='DB has been RESET', users=[], tweets=[])

    return app

#  to run from terminal : set FLASK_APP=TWpred:APP
#                   +     flask run   OR    flask shell

 