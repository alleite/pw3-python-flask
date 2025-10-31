from flask import render_template, request, url_for, redirect, flash, session
from models.database import db, Imagem
import urllib
import json
import os
import uuid


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

    # Definindo tipos de arquivos permitidos
    FILE_TYPES = set(['png', 'jpg', 'jpeg', 'gif'])
    def arquivos_permitidos(filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in FILE_TYPES
        
    # UPLOAD DE IMAGENS
    @app.route('/galeria', methods=['GET', 'POST'])
    def galeria():
        # Seleciona os nomes dos arquivos de imagens no banco
        imagens = Imagem.query.all()
        if request.method == 'POST':
            file = request.files['file']
            # Verifica se o tipo de arquivo é permitido
            if not arquivos_permitidos(file.filename):
                flash("Utilize os tipos de arquivos referentes a imagem.", 'danger')
                return redirect(request.url)
            
            # Criando um nome aleatório para o arquivo
            filename = str(uuid.uuid4())
            
            # Gravando o nome do arquivo no banco
            img = Imagem(filename)
            db.session.add(img)
            db.session.commit()
            
            # Gravando o arquivo na pasta de uploads
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash("Imagem enviada com sucesso!", 'success')
            
        return render_template('galeria.html', imagens=imagens)