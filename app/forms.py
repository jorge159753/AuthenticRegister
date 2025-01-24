from flask_wtf import FlaskForm #FlaskForm: Class base para criação de Formulários com Flask-WTF
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Email, EqualTo, Length



class LoginForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email()]) #Entrada de texto
    password = PasswordField('Password', validators=[InputRequired()]) #Entrada da senha (O texto sai como asteriscos/bolinha)
    submit = SubmitField('Login') #Botão de envio do formulário

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=4, max=20)])
    email = StringField('Email', validators=[InputRequired(), Email()])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm_Password', validators=[InputRequired(), EqualTo(password)]) #EquaLto: Verifica se o campo selecionado "password" é igual ao que foi informado
    submit = SubmitField('Register')

