from flask import render_template, redirect, flash, url_for
from app import db
from app.forms import ResgisterForm
from app.model import User

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = ResgisterForm()
    if form.validate_on_submit(): #Verifica se todos os dados foram enviados (method POST) e se passaram por todas as validações

        #Salva o usúario no Banco de dados
        user = User (
            User = form.username.data,
            password = form.password.data,
            email = form.email.data   
        )

        db.session.add(user)
        db.session.commit()
        flash("Account created successfuly!")

        # Redireciona o usuário para a tela de login
        return redirect(url_for('login'))
    return render_template('register.html', form=form)