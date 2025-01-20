from flask import Flask, Blueprint, render_template, redirect, flash, url_for
from app import db
from app.forms import RegisterForm
from app.model import User

# Definição do Blueprint
main = Blueprint('main', __name__)

# Rota de registro
@main.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        # Salva o usuário no banco de dados
        user = User(
            username=form.username.data,
            password=form.password.data,
            email=form.email.data
        )
        db.session.add(user)
        db.session.commit()
        flash("Account created successfully!")

        # Redireciona o usuário para a tela de login
        return redirect(url_for('main.login'))
    return render_template('register.html', form=form)

# Rota de login
@main.route('/login', methods=['GET', 'POST'])
def login():
    # Aqui vai o código da função login
    return render_template('login.html')

# Criando o objeto Flask
app = Flask(__name__)

# Registrando o Blueprint
app.register_blueprint(main)

# Rota principal
@app.route('/')
def home():
    return render_template('index.html')

# Configuração do Flask (como chave secreta, banco de dados, etc.)
if __name__ == "__main__":
    app.run(debug=True)
