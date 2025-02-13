from app import db
from flask_login import UserMixin



class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True) # Teste de Verificaçáo de usúario
    username = db.Column(db.String(150), nullable = False, unique = True)
    email = db.Column(db.String(150), nullable = False, unique = True)
    password = db.Column(db.String(150), nullable = False, unique = True)
    post = db.relationship('Post', backref = 'Author', lazy = True) # Relacionamento com o Post

    def __repr__(self):
        return f"<User {self.username}>"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(150), nullable = False)
    content = db.Column(db.Text, nullable = False)
    data_Created = db.Column(db.DateTime, default = db.func.now()) # Data de criação do Post
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False) # ID do Autor do post (User)

    def __repr__(self):
        return f"<Post {self.title}>"