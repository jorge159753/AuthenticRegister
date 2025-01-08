from app import db
from flask_login import UserMixin

class User(UserMixin, db.model):
    id = db.Column(db.Integer, primary_Key = True) # Teste de Verificaçáo de usúario
    username = db.Column(db.String(150), nullabel = False, unique = True)
    email = db.Column(db.String(150), nullabel = False, unique = True)
    password = db.Column(db.String(150), nullabel = False, unique = True)
    post = db.relationship('Post', backref = 'Author', lazy = True) # Relacionamento com o Post

    def __repr__(self):
        return f"<User {self.username}>"

class Post(db.model):
    id = db.Column(db.Integer, primary_Key = True)
    title = db.Column(db.String(150), nullabel = False)
    content = db.Column(db.Text, nullabel = False)
    data_Created = db.Column(db.DateTime, default = db.func.now()) # Data de criação do Post
    user_id = db.Column(db.Integer, db.ForeignKey('user_id'), nullabel = False) # ID do Autor do post (User)

    def __repr__(self):
        return f"<Post {self.title}>"