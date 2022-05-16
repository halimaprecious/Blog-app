from flask import Blueprint, render_template,flash, request,redirect,session,url_for
from flask_login import login_required,current_user
from .models import User,Post
from .requests import find_quote
from .forms import UpdateProfile
from . import db, photos

views = Blueprint("views",__name__)

@views.route('/',methods = ['POST','GET'])
def home():
    quote = find_quote()
    posts = Post.query.filter_by().all()
    
   
    return render_template('index.html',quote = quote,)


#user profile
@views.route('/user/<username>')
def profile(username):
   user = User.query.filter_by(username=username).first()
   if not user:
      flash("User does not exist!",category='error')

   return render_template("profile/profile.html", user = user)

#update profile
@views.route('/user/<username>/update',methods =['GET','POST'])
@login_required
def update_profile(username):
   user = User.query.filter_by(username = username).first()

   form = UpdateProfile()
   if form.validate_on_submit():
        
        username= form.username.data
        user.email = form.email.data
        user.bio = form.bio.data
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('.profile',username=user.username))

   return render_template('profile/update.html',form =form)

#profile pic
@views.route('/user/<username>/update/pic',methods=['POST'])
@login_required
def update_pic(username):
   user = User.query.filter_by(username=username).first()
   if 'photo' in request.files:
      filename = photos.save(request.files['photo'])
      path = f'photos/{filename}'
      user.profile_pic_path = path
      db.session.commit()
   return redirect(url_for('views.profile',username=username))