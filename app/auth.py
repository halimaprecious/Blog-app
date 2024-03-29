from flask import Blueprint,render_template,redirect,url_for,request,flash
from flask_login import login_user,logout_user,login_required,current_user
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth',__name__)


@auth.route('/sign-up',methods =['GET','POST'])
def signup():
    if request.method == 'POST':
      email= request.form.get("email")
      username = request.form.get("username")
      password1 = request.form.get("password1")
      password2 = request.form.get("password2")

      email_exists = User.query.filter_by(email=email).first()
      username_exists = User.query.filter_by(username=username).first()
      if email_exists:
         flash('Email is already in use.',category='error')
      elif username_exists:
         flash('Username is already in use.',category='error')
      elif password1 != password2:
         flash('Passsword didn\'t match!.',category='error')
      elif not email or not username and not password1:
         flash('Please fill in all fields!',category = 'error')
      else:
         new_user = User(email=email,username=username,password=generate_password_hash(password1,method='sha256'))
         db.session.add(new_user)
         db.session.commit()

         login_user(new_user,remember=True)
         flash('User created!')
         return redirect(url_for('auth.login'))
    
    return render_template("auth/sign-up.html", user = current_user)


@auth.route('/login',methods = ['GET','POST'])
def login(): 
   if request.method == 'POST':
      email = request.form.get("email")
      password = request.form.get("password")

      user = User.query.filter_by(email=email).first()
      if user:
         if check_password_hash(user.password,password):
            login_user(user,remember=True)
            return redirect(url_for('views.home'))
         else:
            flash("Password is incorrect",category='error')
      elif not email or not password:
         flash("Please enter email and password",category='error')
      else:
         flash('Email does not exist',category = 'error')
         
   return render_template('auth/login.html',user = current_user)

@auth.route('/logout')
@login_required
def logout():
   logout_user()
   return redirect(url_for('views.home'))