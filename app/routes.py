from flask import request
from flask import Blueprint, render_template, redirect, flash, url_for
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from app.forms import RegisterForm, LoginForm
from app.model import User

# Definição do Blueprint
main = Blueprint('main', __name__)

@main.route('/home')
@login_required
def home():
    # Verificar se o usuário está logado
    if current_user.is_authenticated:
        return render_template('index.html')
    else:
        flash("Você precisa estar logado para acessar esta página.", "warning")
        return redirect(url_for('main.login'))
    
# Rota de registro
@main.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        # Verifica se o email já existe
        if User.query.filter_by(email=form.email.data).first():
            flash("Email já existente!", 'danger')
            return redirect(url_for('main.register'))

        # Salva o usuário no banco de dados
        user = User(
            username=form.username.data,
            password=generate_password_hash(form.password.data, method='sha256'),
            email=form.email.data
        )

        db.session.add(user)
        db.session.commit()
        flash("Conta criada com sucesso!", 'success')

        # Redireciona o usuário para a tela de login após o registro
        return redirect(url_for('main.login'))
    return render_template('register.html', form=form)

@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()  
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            flash("Login realizado com sucesso!", 'success')

            # Debug: Verifique se o login foi bem-sucedido
            print(f'Usuário logado: {current_user.username}')

             # Redireciona para a página de destino após login
            next_page = request.args.get('next')
            if next_page:
                return redirect(next_page)
            else:
                return redirect(url_for('main.home'))  # Página inicial após login
        flash("Email ou senha inválidos!")
    return render_template('login.html', form=form)