from flask import render_template, request, redirect, url_for, abort
from . import main
from flask_login import login_required, current_user
from ..models import Post, User, Comment
from .forms import CommentForm, PostForm
from flask.views import View, MethodView
from .. import db
from app import requests
import markdown
from .. import requests


# views
@main.route('/', methods=['GET', 'POST'])
@main.route("/index")
def index():
    """"""
    page = request.args.get('page', 1, type=int)

    return render_template('index.html')


@main.route('/posts/new', methods=['GET', 'Post'])
def new_post():
    form = PostForm

    if form.validate_on_submit():
        description = form.description.data
        title = form.title.data
        owner_id = current_user
        category = form.category.data
        print(current_user._get_current_object().id)
        new_post = Post(owner_id=current_user._get_current_object().id, title=title, description=description)
        db.session.add(new_post)
        db.session.commit()

        return redirect(url_for('main.index'))
    return render_template('posts.html', form=form)


@main.route("/quote")
def about():
    quote = requests.get_quote()
    return render_template('quote.html', title='About', quote=quote)


@main.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@main.route("/quotes")
def quote():
    quote = requests.get_quote()
    return render_template('quote.html',quote=quote)