from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from hades.model import User

class RegisterForm(FlaskForm):

    def validate_username(self, username):
        user= User.query.filter_by(user=username.data).first()
        if user:
            raise ValidationError ('Username already exists!. Please try a different name')

    def validate_email_address(self, email_address):
        email= User.query.filter_by(email_address=email_address.data).first()
        if email:
            raise ValidationError ('Email already exists!. Please try a different email address')


    username = StringField(label='User Name', validators=[Length(min=3, max=30), DataRequired()])
    email_address = StringField(label='Email Address', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Enter Password', validators=[Length(min=8), DataRequired()])
    password2 = PasswordField(label='Confirm Password', validators=[EqualTo("password1"), DataRequired()])
    submit = SubmitField(label='Register User')


class KeywordsForm(FlaskForm):
    keyword1 = StringField(label='Search Keyword')
    keyword2 = StringField(label='Second Search Keyword')
    submit = SubmitField(label='Search')
