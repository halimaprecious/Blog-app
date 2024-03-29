from flask_wtf  import FlaskForm
from wtforms import SubmitField,TextAreaField,StringField,SelectField
from wtforms.validators import DataRequired


class UpdateProfile(FlaskForm):
    username =StringField("Username")
    bio = TextAreaField("Bio")
    email = StringField("Email")
    submit = SubmitField("Update") 

class PostForm(FlaskForm):
    title = StringField("Title")
    text = TextAreaField('Post', validators=[DataRequired()])
    submit = SubmitField('Post')
