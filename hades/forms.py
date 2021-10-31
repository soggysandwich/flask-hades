from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired
class RegisterForm(FlaskForm):
    username=StringField(label='User Name',validators=[Length(min=3,max=30),DataRequired()])
    email_address= StringField(label='Email Address',validators=[Email(),DataRequired()])
    password1= PasswordField(label='Enter Password',validators=[Length(min=8),DataRequired()])
    password2=PasswordField(label='Confirm Password', validators=[EqualTo("password1"),DataRequired()])
    submit = SubmitField(label='Register User')





class KeywordsForm(FlaskForm):
    keyword1=StringField(label='Search Keyword')
    keyword2 = StringField(label='Second Search Keyword')
    submit = SubmitField(label='Search')

