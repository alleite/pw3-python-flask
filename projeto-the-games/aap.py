# Importando o pacote do Flask
from flask import Flask, render_template

# Carregando o flask na variável app
app = Flask(__name__, template_folder='views')


# Criando a rota principal do site
@app.route('/')
# Criando função no python
# View Fuction - Função de visualização
def home():
    return render_template('index.html')


@app.route('/games')
def games():
    titulo = 'minecraft'
    ano = 2009
    categoria = 'sandbox e sobrevivencia'
    jogadores = ['queen' , 'bely' , 'pep' , 'luph', 'deca' ]
    jogosOnline = ['Fall Guys' , 'Mortal Kombat' , 'Street Figther' , 'Tekken', 'Super Mario', 'Tetris', 'HayDay' ]
    return render_template('games.html',titulo=titulo, ano=ano, categoria=categoria, jogadores=jogadores, jogosOnline=jogosOnline )


if __name__ == '__main__':
    # Rodando o servidor do localhost, porta 5000
    app.run(host='localhost', port=5000, debug=True)
