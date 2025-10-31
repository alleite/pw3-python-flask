from flask_sqlalchemy import SQLAlchemy
# Utilize o plugin do VSC SQL3Lite Editor para gerenciar o BD

db = SQLAlchemy()
        
# Classe para imagens
class Imagem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(120), unique=True, nullable=False)
    
    def __init__(self, filename):
        self.filename = filename