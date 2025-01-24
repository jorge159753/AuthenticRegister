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
    return render_template('index.html')

# Rota de registro
@main.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if user.query.filter_by(email=form.email.data).first():
            flash("Email já existente!")
            return ("main.register")

        # Salva o usuário no banco de dados
        user = User(
            username=form.username.data,
            password=generate_password_hash(form.password.data, method='sha256'),
            email=form.email.data
        )

        db.session.add(user)
        db.session.commit()
        flash("Conta criada com sucesso!")

        # Redireciona o usuário para a tela de login
        return redirect(url_for('main.login'))
    return render_template('register.html', form=form)

@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()  
    if form.validate_on_submit():
        user = check_password_hash(email = form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            flash("Login realizado com sucesso!")
        
            # Redireciona o usuário para a tela de login
            return redirect(url_for('main.home'))
        flash("Email ou senha invalido!")
    return render_template('login.html', form=form)