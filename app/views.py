from flask import Blueprint, render_template,flash, request,redirect,session,url_for
from flask_login import login_required,current_user
from .models import User
from .requests import find_quote
from . import db

views = Blueprint("views",__name__)

@views.route('/',methods = ['POST','GET'])
def home():
    quote = find_quote()

    return render_template('index.html',quote = quote)


