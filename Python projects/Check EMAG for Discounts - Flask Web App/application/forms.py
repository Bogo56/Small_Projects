from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,BooleanField,SubmitField
from wtforms.validators import DataRequired,Email,URL


## CREATING FORMS USING FLASK-WTForms

class RegisterForm(FlaskForm):
    username=StringField("Username",validators=[DataRequired()])
    email=StringField("Email",validators=[DataRequired(),Email()])
    password=PasswordField("Password", validators=[DataRequired()])
    submit=SubmitField('Register')

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField('Log In')

class AddItemForm(FlaskForm):
    item = StringField("New Item", validators=[DataRequired(),URL()])
    submit = SubmitField('Add Item')
