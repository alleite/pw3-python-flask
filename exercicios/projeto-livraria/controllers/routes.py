from flask import render_template, request, redirect, url_for # type: ignore

livrolist = [{
    'Título': 'Vermelho branco sangue azul',
    'Datapublicação': '2019-05-14',
    'Autor': 'Casey McQuiston',
    'Gênero': 'Romance juvenil',
    'QuantPáginas': '392',
    'Editora': 'Seguinte'
}]

clublist = [{
    'Nome': 'Ana Luisa Nardes',
    'Email': 'anardesmotta@gmail.com',
    'DataNascimento': '2008/06/17',
    'Telefone': '(13) 99791-8474',
    'GêneroLivro': 'Fantasia',
    'Senha': '#ana03'
}]

livroindicado =[{
    'Quemindicou': 'Ana Leite',
    'Nomelivro': 'Castelo Animado',
    'Nomeautor': 'Diana Wynnw Jones',
    'Gênero': 'Fantasia'
}]

def init_app(app):
    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/cadLivros', methods=['GET', 'POST'])
    def cadLivros():
        if request.method == 'POST':
            if (request.form.get('titulo') and request.form.get('ano') and
                request.form.get('autor') and request.form.get('genero') and
                request.form.get('paginas') and request.form.get('editora')):

                livrolist.append({
                    'Título': request.form.get('titulo'),
                    'Datapublicação': request.form.get('ano'),
                    'Autor': request.form.get('autor'),
                    'Gênero': request.form.get('genero'),
                    'QuantPáginas': request.form.get('paginas'),
                    'Editora': request.form.get('editora')
                })
                return redirect(url_for('cadLivros'))

        return render_template('cadLivros.html', livrolist=livrolist)
    
    @app.route('/cadClube', methods=['GET', 'POST'])
    def cadClube():
        if request.method == 'POST':
            if (request.form.get('nome') and request.form.get('email') and
                request.form.get('ano') and request.form.get('telefone') and
                request.form.get('genero') and request.form.get('senha')):

                clublist.append({
                    'Nome': request.form.get('nome'),
                    'Email': request.form.get('email'),
                    'DataNascimento': request.form.get('ano'),
                    'Telefone': request.form.get('telefone'),
                    'GêneroLivro': request.form.get('genero'),
                    'Senha': request.form.get('senha')
                })
                return redirect(url_for('cadClube'))

        return render_template('cadClube.html', clublist=clublist)
    
    @app.route('/indicacoes', methods=['GET', 'POST'])
    def indicacoes():
        if request.method == 'POST':
            if (request.form.get('nome2') and request.form.get('livronome') and 
                request.form.get('autornome') and request.form.get('livrogenero')):
                
                livroindicado.append({
                    'Quemindicou': request.form.get('nome2'),
                    'Nomelivro': request.form.get('livronome'),
                    'Nomeautor': request.form.get('autornome'),
                    'Gênero': request.form.get('livrogenero')
                })
                return redirect(url_for('indicacoes'))
        return render_template('indicacoes.html', livroindicado=livroindicado)
