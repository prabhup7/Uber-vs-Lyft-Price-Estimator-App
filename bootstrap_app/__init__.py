from flask import Flask, render_template
from flask_bootstrap import Bootstrap


def create_app(configfile=None):
    app = Flask(__name__)
    Bootstrap(app)

    @app.route('/', methods=('GET', 'POST'))
    def index():
        return render_template('index.html')

    return app
