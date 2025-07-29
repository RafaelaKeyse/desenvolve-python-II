from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from app.alquimias import create_user, get_user_by_email, create_post, get_timeline
from werkzeug.security import check_password_hash

routes = Blueprint('routes', __name__)

@routes.route('/')
def index():
    posts = []
    if current_user.is_authenticated:
        posts = get_timeline()
    return render_template('index.html', posts=posts)

@routes.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = get_user_by_email(email)
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('routes.index'))
        flash('Login ou senha incorretos.')
    return render_template('login.html')

@routes.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('routes.index'))

@routes.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        profile_pic = request.form['profile_pic']
        bio = request.form['bio']

        if get_user_by_email(email):
            flash('Email já cadastrado.')
            return redirect(url_for('routes.cadastro'))

        create_user(username, email, password, profile_pic, bio)
        flash('Cadastro realizado com sucesso! Faça login.')
        return redirect(url_for('routes.login'))

    return render_template('cadastro.html')

@routes.route('/post', methods=['GET', 'POST'])
@login_required
def post():
    if request.method == 'POST':
        body = request.form['body']
        create_post(body, current_user)
        return redirect(url_for('routes.index'))
    return render_template('post.html')
