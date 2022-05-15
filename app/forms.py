from flask_wtf  import FlaskForm
from wtforms import SubmitField,TextAreaField,StringField,SelectField
from wtforms.validators import DataRequired


class UpdateProfile(FlaskForm):
    first_name = StringField("First name")
    last_name = StringField("Last Name")
    bio = TextAreaField("Bio")
    email = StringField("Email")
    submit = SubmitField("Update") 