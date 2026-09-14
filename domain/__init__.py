from flask import Flask, render_template

def create_podcast():
    list_of_podcasts = [{
    'title': '',
    'img_url': '',
    'categories': '',
    'author': '',
    'language': '',
    'about': '',
    'website': '',
    'itunes_id': ''
    }, {
    'title': '',
    'img_url': '',
    'categories': '',
    'author': '',
    'language': '',
    'about': '',
    'website': '',
    'itunes_id': ''
    }]
def create_app():
    app = Flask(__name__)

    @app.route('/')
    def home():
        return render_template('layout.html')

    @app.route('/podcasts')
    def show_podcasts():
        return render_template('catalogue.html')
    return app
