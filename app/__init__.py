from flask import Flask, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
import os


# Instanciar objetos globais
db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'chave-secreta-padrao')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


    @app.route('/')
    def index():
        return redirect(url_for('main.home'))  # Certifique-se de que 'main.home' exista

    # Inicializar extensões
    db.init_app(app)
    login_manager.init_app(app)
    migrate = Migrate(app, db)

    login_manager.login_view = 'main.login' 

    # Configuração do Flask-Login
    login_manager.login_view = 'main.login'  # Redireciona para a rota de login
    login_manager.login_message = "Por favor, faça login para acessar esta página."
    login_manager.login_message_category = "info"

    @login_manager.user_loader
    def loader_user(user_id):
        return User.query.get(int(user_id))

    @login_manager.unauthorized_handler
    def unauthorized():
        flash("Você precisa estar logado para acessar esta página.", "warning")
        return redirect(url_for('main.login'))

    # Importar e registrar Blueprints
    from app.routes import main
    app.register_blueprint(main)

    # Importa os modelos (Após a inicializar o db)
    from app.model import User

    return app
