from flask import render_template, request, url_for, redirect
import urllib
import json  


def init_app(app):

    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/apicats', methods=['GET', 'POST'])
    @app.route('/apicats/<string:id>', methods=['GET', 'POST'])
    def apicats(id=None):
        url = 'https://api.thecatapi.com/v1/breeds'
        response = urllib.request.urlopen(url)
        apiData = response.read()
        catsList = json.loads(apiData)

        if id:
            catInfo = next((cat for cat in catsList if cat['id'] == id), None)
            if catInfo:
                return render_template('catinfo.html', catInfo=catInfo)
            else:
                return f'O gato com id {id} não foi encontrado.'
        else:
            return render_template('apicats.html', catsList=catsList)
