from flask import Blueprint, render_template,flash, request,redirect,session,url_for
from flask_login import login_required,current_user
from .models import User,Post,Like,Comment
from .requests import find_quote
from .forms import UpdateProfile,PostForm
from . import db, photos

views = Blueprint("views",__name__)

@views.route('/',methods = ['POST','GET'])
def home():
   quote = find_quote()
   posts = Post.query.all()
   user = User.query.all()
   return render_template('index.html',quote = quote,posts=posts,user=user)


#user profile
@views.route('/user/<username>')
def profile(username):
   user = User.query.filter_by(username=username).first()

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

# write post
@views.route('/post/',methods=['GET','POST'])
@login_required
def post():

   form =PostForm()
   if form.validate_on_submit():
      title= form.title.data
      text =form.text.data
     
      post = Post(title=title,text=text)
      db.session.add(post)
      db.session.commit()
   
      return redirect(url_for('views.home'))

   return render_template('post.html',user=current_user,form =form)

# comments route
@views.route('/comment/<post_id>',methods=['POST'])
@login_required
def comment(post_id):
   text = request.form.get('text')

   if not text:
      flash('comment cannot be empty',category='error')
   else:
      post = Post.query.filter_by(id=post_id)
      if post:
         comment = Comment(text = text, author=current_user.id, post_id= post_id)
         db.session.add(comment)
         db.session.commit()
      else:
         flash('Post does not exist!',category='error')
       
   return redirect(url_for('views.home'))

# likes route
@views.route('/like/<post_id>',methods=['GET'])
@login_required
def like(post_id):
   post = Post.query.filter_by(id=post_id).first()
   like =Like.query.filter_by(author=current_user.id, post_id = post_id).first()
   
   if not post:
      flash('Post does not exist',category='error')
   elif like:
      db.session.delete(like)
      db.session.commit()
   else:
      like = Like(author=current_user.id, post_id=post_id)
      db.session.add(like)
      db.session.commit()

   return redirect(url_for('views.home'))
