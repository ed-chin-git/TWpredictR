""" Main application and routing logic for TweetR """
from flask import Flask, request, render_template
from .models import DB, User, Tweet


def create_app():
    """ create + config Flask app obj """
    app = Flask(__name__)

    #  after creatin models.py  run the follow
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tweetr.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['ENV'] = 'Debug'
    DB.init_app(app)

    @app.route('/')
    def root():
        users = User.query.all()
        tweets = Tweet.query.all()
        return render_template('base.html', title='Home', users=users, tweets=tweets )
    
    @app.route('/reset')
    def reset():
        DB.drop_all()
        DB.create_all()
        return render_template('base.html', title='DB has been RESET', users=[], tweets=[])

    return app

#  to run from terminal : set FLASK_APP=TweetR:APP
#                   +     flask run -h 0.0.0.0 -p 8000
