from flask import render_template, request

jogadores = ['iruah', 'davi_lambari', 'edsongf',
             'kioto', 'black.butterfly', 'jujudopix']
# array de objetos
gamelist = [{'Título': 'CS-GO',
             'Ano': 2012,
             'Categoria': 'FPS Online'},
            ]
consolelist = [{'Nome': 'Nintendo Switch',
                'Preco': 'R$ 2034.99',
                'Pais': 'Japão'}]


def init_app(app):
    # Criando a rota principal do site
    @app.route('/')
    # Criando função no Python
    # View function - Função de visualização
    def home():
        return render_template('index.html')

    @app.route('/games', methods=['GET', 'POST'])
    # View function - Função de visualização
    def games():
        # Dicionário no Python (objeto)
        # Acessando o primeiro jgo da lista de jogos
        game = gamelist[0]
        console = consolelist[0]
        if request.method == 'POST':
            if request.form.get('jogador'):  # name do input
                jogadores.append(request.form.get('jogador'))

        return render_template('games.html',
                               game=game,
                               jogadores=jogadores)

    @app.route('/cadgames', methods=['GET', 'POST'])
    def cadgames():
        if request.method == 'POST':
            if request.form.get('Título') and request.form.get('Ano') and request.form.get('Categoria'):
                gamelist.append({'Título': request.form.get('Título'), 'Ano': request.form.get(
                    'Ano'), 'Categoria': request.form.get('Categoria')})
        return render_template('cadgames.html',
                               gamelist=gamelist)

    @app.route('/consoles', methods=['GET', 'POST'])
    def consoles():
        if request.method == 'POST':
            if request.form.get('Nome') and request.form.get('Preco') and request.form.get('Pais'):
                consolelist.append({'Nome': request.form.get('Nome'), 'Preco': request.form.get(
                    'Preco'), 'Pais': request.form.get('Pais')})
        return render_template('consoles.html',
                               consolelist=consolelist)
