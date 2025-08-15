# Comentário em Python
# Importando o pacote do Flask
from flask import Flask, render_template

# Carregando o Flask na variável app
app = Flask(__name__, template_folder='views')

# Criando a rota principal do site


@app.route('/')
# Criando função no Python
# View function - Função de visualização
def home():
    return render_template('index.html')


@app.route('/games')
# View function - Função de visualização
def games():
    # Dicionário no Python (objeto)
    game = {'Título': 'CS-GO',
            'Ano': 2012,
            'Categoria': 'FPS Online'}

    jogadores = ['iruah', 'davi_lambari', 'edsongf',
                 'kioto', 'black.butterfly', 'jujudopix']

    return render_template('games.html',
                           game=game,
                           jogadores=jogadores)


if __name__ == '__main__':
    # Rodando o servidor no localhost, porta 5000
    app.run(host='0.0.0.0', port=5000, debug=True)
